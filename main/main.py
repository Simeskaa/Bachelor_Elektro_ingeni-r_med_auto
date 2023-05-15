from include.direction_and_distance_estimation import angle_cord_estimation as ace
from include.signal_processing import processing
from include.UDP_class import UDP
from include.GUI import GUI
from include.DC_remover import DC_remover
import json
import numpy as np
import scipy.signal as sig
import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import time
import logging
import threading
from threading import Lock
from copy import copy
import queue
from scipy.io import wavfile
from scipy.io.wavfile import write

# Logging of threads
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
#logging.getLogger().setLevel(logging.DEBUG)

# TEST FILE:-----------------------------------
#samplerate, data = wavfile.read("/Users/dawid/Documents/NTNU/BACHELOR/Sound_triangulation/misc/lydfiler/Piano_440Hz.wav")
#x = data.T
# TEST FILE:-----------------------------------

buffer_size = 4410
mics = [0.0]*4
toad = [0.0]*4
#shift = samplerate
q = queue.Queue()
lock = Lock()
gathered_data = list()
samplerate = 43706



def verify_signals(signals, des_Hz: float = 270.0, width: int = 10):
    top = des_Hz + width
    bot = des_Hz - width
    verified_array = list()
    freq_array = [0]*len(signals)

    # Populate the detected frequency array
    for i in range(len(signals)):
        freq = pro.hps(signals[i])
        freq_array.insert(0, freq)
        freq_array.pop(-1)

        # If frequency within range, consider it verified
        if bot <= freq <= top:
            verified_array.insert(0, freq)

    # If there are enough verified values, return ready
    if len(verified_array) >= len(signals):
        ready = True
    else:
        ready = False
    logging.info(f'worker: Frequencies detected -> {freq_array}')
    return ready

def prod(lock):
    global gathered_data
    a0_tot = []
    a1_tot = []
    a2_tot = []
    a3_tot = []
    stop_time = time.perf_counter() + 2
    while True:
        if time.perf_counter() >= stop_time:
            gathered_data.append(a0_tot)
            gathered_data.append(a1_tot)
            gathered_data.append(a2_tot)
            gathered_data.append(a3_tot)
            break
        data = UDP.get_message(65507)
        a0 = []
        a1 = []
        a2 = []
        a3 = []
        if data is not None:
            for i in range(0, len(data), 2):
                b1 = data[i].to_bytes(1, "little")
                b2 = data[i+1].to_bytes(1, "little")
                if (i % 8) == 0:
                    a0.append(int.from_bytes(b1 + b2, byteorder='little'))#/0xffff)
                elif (i % 8) == 2:
                    a1.append(int.from_bytes(b1 + b2, byteorder='little'))#/0xffff)
                elif (i % 8) == 4:
                    a2.append(int.from_bytes(b1 + b2, byteorder='little'))#/0xffff)
                elif (i % 8) == 6:
                    a3.append(int.from_bytes(b1 + b2, byteorder='little'))#/0xffff)
        #a0 = DC0.mean_value_filter(a0)
        #a0 = DC0.lp_filter_start(a0)
        #a1 = DC0.mean_value_filter(a1)
        #a1 = DC1.lp_filter_start(a1)
        #a2 = DC0.mean_value_filter(a2)
        #a2 = DC2.lp_filter_start(a2)
        #a3 = DC0.mean_value_filter(a3)
        #a3 = DC3.lp_filter_start(a3)
        mics = [a0, a1, a2, a3]
        a0_tot.extend(mics[0])
        a1_tot.extend(mics[1])
        a2_tot.extend(mics[2])
        a3_tot.extend(mics[3])
        logging.debug(f"prod  : length of gathered_data: {len(gathered_data)}")
        with lock:
            logging.debug("prod  : Got lock")
            q.put(mics)
            logging.debug(f'prod  : Put {round(mics[0][0],2)}, {round(mics[1][0],2)}, {round(mics[2][0],2)}, {round(mics[3][0],2)} in queue')
        logging.debug("prod  : lock is free")
        time.sleep(0.001)

def consumer(lock):
    empty_vals_array = []
    """Looping the code"""
    while True:
        """Attempt to use the data, if error, give error and kill the while loop"""
        try:
            logging.debug("worker: About to ask for lock")
            """As long as there are values in queue, go through"""

            if not q.empty():
                empty_vals_array = []
                """Receive the data from queue with lock"""
                with lock:
                    logging.debug("worker: Got lock")
                    item = copy(q.get())
                    logging.debug(f'worker: Received {round(item[0][0], 2)} from queue')
                logging.debug("worker: lock is free")
                logging.debug("worker: starting signal processing")

                mics = item
                """Signal verification"""
                desired_Hz = '440'
                start = verify_signals(mics, des_Hz=int(desired_Hz), width=20)
                logging.info(f'worker: Signal verification determined state {start}')

                """Signal processing"""
                if start:
                    logging.debug(f'worker: About to calculate weights')
                    we, wk = pro.spectral_weighing(mics, a=0.3, y=0.4)
                    logging.debug(f'worker: About to calculate correlation')
                    t12, d12 = pro.cross_correlation(mics[0], mics[1], we)
                    t13, d13 = pro.cross_correlation(mics[0], mics[2], we)
                    t14, d14 = pro.cross_correlation(mics[0], mics[3], we)

                    toad = [0.0, t12, t13, t14]
                    toad = ace.norm_values(toad)
                    logging.debug(f'worker: toad estimated to be {toad}')


                    # Conversion from time delays to position
                    logging.debug(f'worker: about to calculate angle and distance')
                    boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule = ace.timestamp_2_cord(toad)
                    logging.info(f'worker: Angle {round(average_angle*180/np.pi,2)} degrees')
                logging.debug(f'worker: signal processing is done')
            else:
                empty_vals = 1
                empty_vals_array.append(empty_vals)
                if len(empty_vals_array) > 50:
                    logging.debug(f'worker:  Too many empty values, EXITING thread')
                    break
                #logging.debug(f'worker: queue was empty, amount of empty {len(empty_vals_array)}')
        except Exception as e:
            logging.info(f'worker: Error occurred, terminating thread')
            logging.info(f'worker: Error {e}')
            break
        time.sleep(0.01)

def hps_local(xn, samplerate):
    # Creating variables
    L = len(xn)
    Xk_mag = np.abs(np.fft.fft(xn))

    N = L//8
    Yk = Xk_mag[0:N]
    Yk2 = Yk * Xk_mag[0:2:2*N]
    Yk3 = Yk2 * Xk_mag[0:3:3*N]
    Yk4 = Yk3 * Xk_mag[0:4:4*N]

    peak_location = np.argmax(Yk)
    frequency = peak_location/L*samplerate

    return Yk, Yk2, Yk3, Yk4, peak_location, frequency

def spectral_weighing(mic, a, y):
        nr_mics = len(mic)       #  Amount of microphones
        nr_samples = len(mic[0]) #  This can be created with only 0, since all mics are same length

        mic_fft = [0]*4
        mic_fft[0] = np.fft.fft(mic[0])
        mic_fft[1] = np.fft.fft(mic[1])
        mic_fft[2] = np.fft.fft(mic[2])
        mic_fft[3] = np.fft.fft(mic[3])

        # Empty arrays
        X_k = [0]*nr_samples
        Xn_k = [0]*nr_samples
        wk = [0]*nr_samples
        we_k = [0]*nr_samples

        # Convert the input values to frequency domain
        #for j in range(nr_mics):
        #    mic_fft[j] = np.fft.fft(mic_fft[j])

        # Calculate values for every sample between all microphones
        for i in range(nr_samples):
            X_k[i] = (mic_fft[0][i] + mic_fft[1][i] + mic_fft[2][i] + mic_fft[3][i]) / nr_mics    # Average
            Xn_k[i] = max(0.01, np.sqrt( ((mic_fft[0][i] - X_k[i]) +
                                          (mic_fft[1][i] - X_k[i]) +
                                          (mic_fft[2][i] - X_k[i]) +
                                          (mic_fft[3][i] - X_k[i]))**2 / nr_mics ) ) # Std (noise)

            wk[i] = max(0.1, ((X_k[i] - (a * Xn_k[i])) / (X_k[i])) )              # Weight

            # based on function 5 in pdf: https://ieeexplore.ieee.org/document/1248813
            # we_k (weights with limits)
            if X_k[i] <= Xn_k[i]:
                we_k[i] = wk[i]
            elif X_k[i] > Xn_k[i]:
                we_k[i] = wk[i] * ( (X_k[i])/(Xn_k[i]) )**y

        return we_k, wk

def cross_correlation(xn_1, xn_2, we, samplerate):
    # Convert to frequency domain
    X1_k = np.fft.fft(xn_1)
    X2_k = np.fft.fft(xn_2)

    # Cross correlation
    R_12_CC = X1_k*np.conjugate(X2_k)                            # Cross correlation (Cc)
    R_12_NW = X1_k*np.conjugate(X2_k)/(abs(X1_k)*abs(X2_k))      # Cc + noise whitening (nw)
    R_12 = (we*X1_k*np.conjugate(X2_k))/(abs(X1_k)*abs(X2_k))  # Cc + nw + weights

    # Convert to time domain by inverse FFT (IFFT)
    r_12 = np.fft.ifft(R_12)

    # Calculate time delay between the two signals and distance
    sample_delay = np.argmax(r_12)

    # In case there is a peak and the wrong side of the correlation
    if sample_delay > len(xn_1)/2:
        sample_delay -= len(xn_1)

    # Calculate the time and distance
    time_delay = sample_delay/samplerate
    distance = time_delay*343
    return X1_k, X2_k, R_12_CC, R_12_NW, R_12, r_12, time_delay, distance


if __name__ == "__main__":
    # Instancing of classes
    UDP = UDP(ip_adress="192.168.1.50", port=5001, receive_msg=True)
    DC0 = DC_remover()
    DC1 = DC_remover()
    DC2 = DC_remover()
    DC3 = DC_remover()
    pro = processing(samplerate)
    ace = ace(dist_short_mic=27.56*10**-2, max_distance=100)
    #app = QApplication(sys.argv)
    #GUI = GUI(max_dist=100, delay= 1000)

    # Turning on threads
    t1 = threading.Thread(target=prod, args=(lock,), daemon=True)
    t2 = threading.Thread(target=consumer, args=(lock,), daemon=True)
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()


    gathered_data[0] = DC0.mean_value_filter(gathered_data[0])
    gathered_data[1] = DC0.mean_value_filter(gathered_data[1])
    write("Live_data.wav", samplerate, np.array(gathered_data[0]).astype(np.int16))

    if True:
        if True:
            # FFT raw file
            raw_file = gathered_data[0]
            fft_file = np.fft.fft(np.abs(gathered_data[0]))
            plt.figure(1, figsize=(12,8))
            plt.subplot(2, 1, 1)
            plt.plot(raw_file)
            plt.xlabel('Raw file')
            plt.subplot(2, 1, 2)
            plt.semilogy(fft_file)
            plt.xlabel('Raw FFT')
            plt.tight_layout()

        if True:
            # HPS
            Yk1, Yk2, Yk3, Yk4, peak_location, frequency = hps_local(gathered_data[0], samplerate)
            plt.figure(2, figsize=(12,8))
            plt.subplot(4, 1, 1)
            plt.plot(Yk1)
            plt.xlabel('Yk1')
            plt.subplot(4, 1, 2)
            plt.plot(Yk2)
            plt.xlabel('Yk2')
            plt.subplot(4, 1, 3)
            plt.plot(Yk3)
            plt.xlabel('Yk3')
            plt.subplot(4, 1, 4)
            plt.plot(Yk4)
            plt.xlabel('Yk4')
            plt.plot(peak_location, Yk4[peak_location], 'rs')
            plt.tight_layout()

        if True:
            # Weights
            we_k, wk = spectral_weighing(gathered_data, 0.1, 0.4)
            wk = wk
            we_k = we_k
            plt.figure(3, figsize=(12,8))
            plt.subplot(2,1,1)
            plt.plot(wk)
            plt.xlabel('wk')
            plt.subplot(2,1,2)
            plt.plot(we_k)
            plt.xlabel('we_k')
            plt.tight_layout()

        if True:
            # Cross correlation
            # Input signals
            X1_k, X2_k, R_12_CC, R_12_NW, R_12, r_12, time_delay, distance = cross_correlation(gathered_data[0], gathered_data[1], we_k, samplerate)
            plt.figure(4, figsize=(12,8))
            plt.subplot(2, 1, 1)
            plt.semilogy(np.abs(X1_k))
            plt.xlabel('Sig1 in fft')
            plt.subplot(2, 1, 2)
            plt.semilogy(np.abs(X2_k))
            plt.xlabel('Sig2 in fft')
            plt.tight_layout()

        if True:
            # Crosscorrelation
            plt.figure(5, figsize=(12,8))
            plt.subplot(3, 1, 1)
            plt.semilogy(np.abs(R_12_CC))
            plt.xlabel('Standard correlation')
            plt.subplot(3, 1, 2)
            plt.semilogy(np.abs(R_12_NW))
            plt.xlabel('CC with noise whitening')
            plt.subplot(3, 1, 3)
            plt.semilogy(np.abs(R_12))
            plt.xlabel('CC with noise whitening + weights')
            plt.tight_layout()

        if True:
            # time domain
            plt.figure(6, figsize=(12,8))
            plt.plot(r_12)
            plt.xlabel('result in time domain')
            peak = np.argmax(r_12)
            plt.plot(peak, r_12[peak], 'rs')

        plt.show()

    """
    v live data
    v HPS
    v fft
    v weights
    v fft with weights
    v cross correlation in fft
    v cross correlation in time
    """

    logging.info("Main: Program finished")

