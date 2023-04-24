from include.direction_and_distance_estimation import angle_cord_estimation as ace
from include.signal_processing import processing
from include.UDP_class import UDP
from include.filter import DC_remover
import json
import copy
import numpy as np
from numpy import cos, pi
import scipy.signal as sig
import matplotlib.pyplot as plt
import time


buffer_size = 1024
list_mic_1 = []
list_mic_2 = []
filter_m1 = []
filter_m2 = []


def recv():
    msg = UDP.get_message(65508)
    inc_msg = json.loads(msg)
    return inc_msg

def norm_data(data):


    #data.T / 0x1000
    m_1 = data['mic 1']
    m_2 = data['mic 2']

    #for i in range(len(m_1)):
    #    m_1[i] /= 0x1000
    #    m_2[i] /= 0x1000

    return m_1, m_2

if __name__ == "__main__":
    UDP = UDP(ip_adress="192.168.0.101", port=5005, receive_msg=True)
    print('ready to get')
    pro = processing(216)
    DC = DC_remover(alpha=0.95)
    while time.perf_counter() > time.perf_counter()+30:
        inc_msg = recv()
        x_1, x_2 = norm_data(inc_msg)
        fake_x1 = copy.copy(x_1)
        fake_x2 = copy.copy(x_2)
        filter_x1 = DC.block_data_DC_reomver(x_1)
        filter_x2 = DC.block_data_DC_reomver(x_2)
        list_mic_1.extend(fake_x1)
        list_mic_2.extend(fake_x2)
        filter_m1.extend(filter_x1)
        filter_m2.extend(filter_x2)
        # print(x_1, "\n", x_2)
        # print(pro.hps(x_1), pro.hps(x_2), "\n")
    fig, ax1 = plt.subplots(2,1)
    ax1.plot(list_mic_1, 'r')
    ax1.plot(list_mic_2, 'b')

    fig, ax2 = plt.subplots(2, 2)
    ax2.plot(filter_m1, 'r')
    ax2.plot(filter_m2, 'b')