from include.direction_and_distance_estimation import angle_cord_estimation as ace
from include.signal_processing import processing
from include.UDP_class import UDP
from include.GUI import GUI
import json
import numpy as np
import scipy.signal as sig
import sys
from PySide6.QtWidgets import QApplication


buffer_size = 4096
ready = False
mics = [0]*4
toad = [0]*4

def recv():
    msg = UDP.get_message(65508)
    #inc_msg = json.loads(msg)
    return msg

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
    UDP = UDP(ip_adress="192.168.0.69", port=5005, receive_msg=True)
    pro = processing(216)
    ace = ace()
    GUI = GUI()

    # Receive signal from FPGA
    msg = recv()
    for i in range(len(mics)):
        mics[i] = msg[i] # mics[0] has data from mic 1

    # Signal verification
    start = verify_signals(signals=mics, des_Hz=440, width=10)

    # Signal processing
    if start:
        we = pro.spectral_weighing(mics, a=0.3, y=0.4)
        for i in range(len(mics)):
            toad[i] = pro.cross_correlation(mics[0], mics[i], we)
    # toad = [0, 0, 42, 42]

    # Convertion from time delays to position
    boat_coords_x, boat_coords_y, dist, average_angle, angle_overrule = ace.timestamp_2_cord(toad)

    # GUI representation
    if False:
        GUI.update_GUI(x= boat_coords_x, y=boat_coords_y, hz= 440, angle_overrule= angle_overrule)

        # These have to bo threaded
        #app = QApplication(sys.argv)
        #window = GUI()
        #window.show()
        #app.exec()
