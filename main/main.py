from include.direction_and_distance_estimation import angle_cord_estimation as ace
from include.signal_processing import processing
from include.UDP_class import UDP
from include.GUI import GUI
import json
import numpy as np
import scipy.signal as sig
import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import time
import logging
from include.Pipeline import Pipeline
import threading
import concurrent.futures
from threading import Lock
from copy import copy
import queue
from scipy.io import wavfile

# Logging of threads
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
#logging.getLogger().setLevel(logging.DEBUG)

# TEST FILE:-----------------------------------
samplerate, data = wavfile.read("/Users/dawid/Documents/NTNU/BACHELOR/Sound_triangulation/misc/lydfiler/Piano_440Hz.wav")
x = data.T
# TEST FILE:-----------------------------------

buffer_size = 4096
mics = [0.0]*4
toad = [0.0]*4
shift = samplerate
q = queue.Queue()
lock = Lock()


def verify_signals(signals, des_Hz: int = 440, width: int = 10):
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
    """
    Receiving data here
    until FPGA is ready, test data will be used
    """
        # TEST FILE: ------------------------------------------------------------------------------------------------------
    shift = samplerate
    dist_mics = [0.0, 15.012*10**-2, 23.116*10**-2, 38.128*10**-2]
    #  1 quadrant
    mic1 = pro.add_delay(x, dist_mics[0], fs=samplerate)+\
           np.random.randn(len(x))*0.05
    mic2 = pro.add_delay(x, dist_mics[1], fs=samplerate)+\
           np.random.randn(len(x))*0.05
    mic3 = pro.add_delay(x, dist_mics[2], fs=samplerate)+\
           np.random.randn(len(x))*0.05
    mic4 = pro.add_delay(x, dist_mics[3], fs=samplerate)+\
           np.random.randn(len(x))*0.05
    # TEST FILE: ------------------------------------------------------------------------------------------------------
    while True:
        if samplerate+shift >= len(mic1):
            logging.debug(f'prod  : quitting thread')
            break
        logging.debug("prod  : About to ask for lock")
        with lock:
            logging.debug("prod  : Got lock")
            mics = \
                [mic1[samplerate+shift:samplerate+buffer_size+shift],
                 mic2[samplerate+shift:samplerate+buffer_size+shift],
                 mic3[samplerate+shift:samplerate+buffer_size+shift],
                 mic4[samplerate+shift:samplerate+buffer_size+shift]]
            q.put(mics)
            logging.debug(f'prod  : Put {round(mics[0][0],2)} in queue')
        logging.debug("prod  : lock is free")
        shift = shift + buffer_size
        time.sleep(0.01)

def worker(lock):
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
                logging.debug(f'worker: Signal verification determined state {start}')

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
                    logging.debug(f'worker: Angle {round(average_angle*180/np.pi,2)} degrees')
                logging.debug(f'worker: signal processing is done')
            else:
                empty_vals = 1
                empty_vals_array.append(empty_vals)
                if len(empty_vals_array) > 5:
                    logging.debug(f'worker:  Too many empty values, EXITING thread')
                    break
                logging.debug(f'worker: queue was empty, amount of empty {len(empty_vals_array)}')
        except:
            logging.debug(f'worker: Error occurred, terminating thread')
            break
        time.sleep(0.01)



if __name__ == "__main__":
    # Instancing of classes
    #UDP = UDP(ip_adress="192.168.0.69", port=5005, receive_msg=True)
    pro = processing(samplerate)
    ace = ace(dist_short_mic=27.56*10**-2, max_distance=100)
    app = QApplication(sys.argv)
    GUI = GUI(max_dist=100, delay= 1000)

    # Turning on threads
    t1 = threading.Thread(target=prod, args=(lock,), daemon=True)
    t2 = threading.Thread(target=worker, args=(lock,), daemon=True)
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()
    logging.info("Main: Program finished")


    # TEST FILE: ------------------------------------------------------------------------------------------------------
    # dist_mics = [0.0, 15.012*10**-2, 23.116*10**-2, 38.128*10**-2]

    #  1 quadrant
    # mic1 = pro.add_delay(x, dist_mics[0], fs=samplerate)+\
    #        np.random.randn(len(x))*0.05
    # mic2 = pro.add_delay(x, dist_mics[1], fs=samplerate)+\
    #        np.random.randn(len(x))*0.05
    # mic3 = pro.add_delay(x, dist_mics[2], fs=samplerate)+\
    #        np.random.randn(len(x))*0.05
    # mic4 = pro.add_delay(x, dist_mics[3], fs=samplerate)+\
    #        np.random.randn(len(x))*0.05
    #
    # mics = \
    #     [mic1[samplerate+shift:samplerate+buffer_size+shift],
    #      mic2[samplerate+shift:samplerate+buffer_size+shift],
    #      mic3[samplerate+shift:samplerate+buffer_size+shift],
    #      mic4[samplerate+shift:samplerate+buffer_size+shift]]
    # TEST FILE: ------------------------------------------------------------------------------------------------------

    # Receive signal from FPGA
    # Not ready yet

    # Signal verification
    # desired_Hz = '440'
    # start = verify_signals(mics, des_Hz=int(desired_Hz), width=20)

    # # Signal processing
    # if start:
    #     we, wk = pro.spectral_weighing(mics, a=0.3, y=0.4)
    #     t12, d12 = pro.cross_correlation(mics[0], mics[1], we)
    #     t13, d13 = pro.cross_correlation(mics[0], mics[2], we)
    #     t14, d14 = pro.cross_correlation(mics[0], mics[3], we)
    #
    #     toad = [0.0, t12, t13, t14]
    #     toad = ace.norm_values(toad)
    #
    #     # Conversion from time delays to position
    #     boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule = ace.timestamp_2_cord(toad)
    #     print(f'Angle Estimate: {round(average_angle*180/np.pi,2)} degrees')

