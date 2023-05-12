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
#samplerate, data = wavfile.read("/Users/dawid/Documents/NTNU/BACHELOR/Sound_triangulation/misc/lydfiler/Piano_440Hz.wav")
#x = data.T
# TEST FILE:-----------------------------------

buffer_size = 4410
mics = [0.0]*4
toad = [0.0]*4
#shift = samplerate
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

    while True:
        data = UDP.get_message(65536)
        a0 = []
        a1 = []
        a2 = []
        a3 = []
        if data is not None:
            for i in range(0, len(data), 2):
                b1 = data[i].to_bytes(1, "little")
                b2 = data[i+1].to_bytes(1, "little")
                if (i % 8) == 0:
                    a0.append(int.from_bytes(b1 + b2, byteorder='little'))
                elif (i % 8) == 2:
                    a1.append(int.from_bytes(b1 + b2, byteorder='little'))
                elif (i % 8) == 4:
                    a2.append(int.from_bytes(b1 + b2, byteorder='little'))
                elif (i % 8) == 6:
                    a3.append(int.from_bytes(b1 + b2, byteorder='little'))
        a0 = DC.mean_value_filter(a0)
        a1 = DC.mean_value_filter(a1)
        a2 = DC.mean_value_filter(a2)
        a3 = DC.mean_value_filter(a3)
        mics = [a0, a1, a2, a3]
        with lock:
            logging.debug("prod  : Got lock")
            q.put(mics)
            logging.info(f'prod  : Put {round(mics[0][0],2)}, {round(mics[1][0],2)}, {round(mics[2][0],2)}, {round(mics[3][0],2)} in queue')
        logging.debug("prod  : lock is free")
        time.sleep(0.01)

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
                logging.debug(f'worker: queue was empty, amount of empty {len(empty_vals_array)}')
        except:
            logging.info(f'worker: Error occurred, terminating thread')
            break
        time.sleep(0.01)



if __name__ == "__main__":
    # Instancing of classes
    UDP = UDP(ip_adress="192.168.1.50", port=5001, receive_msg=True)
    DC = DC_remover()
    pro = processing(44100)
    ace = ace(dist_short_mic=27.56*10**-2, max_distance=100)
    app = QApplication(sys.argv)
    GUI = GUI(max_dist=100, delay= 1000)

    # Turning on threads
    t1 = threading.Thread(target=prod, args=(lock,), daemon=True)
    t2 = threading.Thread(target=consumer, args=(lock,), daemon=True)
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()
    logging.info("Main: Program finished")

