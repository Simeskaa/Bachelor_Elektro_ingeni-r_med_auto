from include.direction_and_distance_estimation import angle_cord_estimation as ace
from include.signal_processing import processing
from include.UDP_class import UDP
#from include.GUI import GUI
import json
import numpy as np
import scipy.signal as sig
import sys
#from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import time
import logging
from include.Pipeline import Pipeline
import threading
import concurrent.futures

from scipy.io import wavfile

# TEST FILE:-----------------------------------
samplerate, data = wavfile.read("D:\BACHELOR\misc\lydfiler\Piano_440Hz.wav")
x = data.T
# TEST FILE:-----------------------------------

buffer_size = 4096
mics = [0]*4
toad = [0.0]*4
shift = 0


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
    return ready


def producer(pipeline, event):
    global shift
    """Pretend we're getting array from the network."""
    while not event.is_set():
        shift += buffer_size
        mics = [mic1[samplerate + shift: samplerate+buffer_size + shift],
                mic2[samplerate + shift: samplerate+buffer_size + shift],
                mic3[samplerate + shift: samplerate+buffer_size + shift],
                mic4[samplerate + shift: samplerate+buffer_size + shift]]

        message = mics
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    """Using the received message, in calculations"""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )
        # Signal verification
        desired_Hz = '440'
        start = verify_signals(mics, des_Hz=int(desired_Hz), width=20)

        # Signal processing
        if start:
            we, wk = pro.spectral_weighing(mics, a=0.3, y=0.4)
            t12, d12 = pro.cross_correlation(mics[0], mics[1], we)
            t13, d13 = pro.cross_correlation(mics[0], mics[2], we)
            t14, d14 = pro.cross_correlation(mics[0], mics[3], we)

            toad = [0.0, t12, t13, t14]
            toad = ace.norm_values(toad)

            # Conversion from time delays to position
            boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule = ace.timestamp_2_cord(toad)
            print(average_angle)
    logging.info("Consumer received EXIT event. Exiting")



if __name__ == "__main__":
    # Instancing of classes
    #UDP = UDP(ip_adress="192.168.0.69", port=5005, receive_msg=True)
    pro = processing(samplerate)
    ace = ace(dist_short_mic=27.56*10**-2, max_distance=100)
    #app = QApplication(sys.argv)
    #GUI = GUI(max_dist=100, delay= 1000)

    pipeline = Pipeline()
    event = threading.Event()


    # Logging of threads
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        #time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()


    # TEST FILE: ------------------------------------------------------------------------------------------------------
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

    # Receive signal from FPGA
    # Not ready yet


