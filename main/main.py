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

from scipy.io import wavfile

# TEST FILE:-----------------------------------
samplerate, data = wavfile.read('/Users/dawid/Documents/NTNU/BACHELOR/Sound_triangulation/misc/lydfiler/Piano_440Hz.wav')
x = data
# TEST FILE:-----------------------------------

buffer_size = 4096
ready = False
mics = [0]*4
toad = [0]*4

def recv():
    #msg = UDP.get_message(65508)
    #inc_msg = json.loads(msg)
    #return msg
    pass

def verify_signals(signals: list, des_Hz: int = 440, width: int = 10):
    ready = False
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
        # If not enough values, return false
        ready = False

        #print(f'Not Ready, one of the frequencies was out of range:{freq_array}')

    return ready

if __name__ == "__main__":
    # Instancing of classes
    #UDP = UDP(ip_adress="192.168.0.69", port=5005, receive_msg=True)
    pro = processing(samplerate)
    ace = ace()
    #app = QApplication(sys.argv)
    #GUI = GUI()


    # TEST FILE: -----------------------------------
    toad_78 = [0, 0.029, 0.019, 0.048]
    mic1 = pro.add_delay(x, 0, fs=samplerate)+\
           np.random.randn(len(x))*0.05
    mic2 = pro.add_delay(x, toad_78[1]*343, fs=samplerate)+\
           np.random.randn(len(x))*0.05
    mic3 = pro.add_delay(x, toad_78[2]*343, fs=samplerate)+\
           np.random.randn(len(x))*0.05
    mic4 = pro.add_delay(x, toad_78[3]*343, fs=samplerate)+\
           np.random.randn(len(x))*0.05
    mics = [mic1[100000:100000+buffer_size], mic2[100000:100000+buffer_size], mic3[100000:100000+buffer_size], mic4[100000:100000+buffer_size]]
    # TEST FILE: -----------------------------------

    # Receive signal from FPGA
    #msg = recv()
    #for i in range(len(mics)):
    #    mics[i] = msg[i] # mics[0] has data from mic 1

    # Signal verification
    start = verify_signals(signals=mics, des_Hz=440, width=20)
    print(start)


    # Signal processing
    if start:
        we = pro.spectral_weighing(mics, a=0.3, y=0.4)
        for i in range(len(mics)-1):
            toad[i] = pro.cross_correlation(mics[0], mics[i+1], we)
        print(toad)
        #toad = pro.norm_values(toad)

        # Convertion from time delays to position
        #boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule = ace.timestamp_2_cord(toad)

        # Troubleshooting
        if True:
            # RAW
            if False:
                plt.close(1); plt.figure(1, figsize=(4,3))
                plt.plot(mics[0], color='b', label='RAW signal 1')
                plt.plot(mics[1], color='tab:orange',label="RAW signal 2 (behind)")
                plt.plot(mics[2], color='r', label='RAW signal 1')
                plt.plot(mics[3], color='g' ,label="RAW signal 2 (behind)")

            # Weights
            if False:
                plt.close(2); plt.figure(2, figsize=(4,3))
                plt.plot(we)

            plt.show()

        # GUI representation



        # These have to bo threaded
        GUI.show()
        GUI.update_GUI(x= boat_coords_x, y=boat_coords_y, hz= 440, angle_overrule= angle_overrule)
        print("GUI about to go")
        app.exec()
        print("GUI NOT")
