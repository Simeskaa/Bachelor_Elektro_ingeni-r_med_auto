from include.direction_and_distance_estimation import angle_cord_estimation as ace
from include.signal_processing import processing
from include.UDP_class import UDP
import json
import numpy as np
from numpy import cos, pi
import scipy.signal as sig


buffer_size = 1024


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

    UDP = UDP(ip_adress="192.168.0.69", port=5005, receive_msg=True)
    pro = processing(216)
    while True:
        inc_msg = recv()
        x_1, x_2 = norm_data(inc_msg)
        print(x_1, "\n", x_2)
        print(pro.hps(x_1), pro.hps(x_2), "\n")






