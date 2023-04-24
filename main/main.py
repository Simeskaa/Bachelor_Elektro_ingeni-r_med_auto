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

list_raw_values_m1 = []
list_raw_values_m2 = []
list_block_filter_m1 = []
list_block_filter_m2 = []
holding_list_lp_filter_m1 = []
holding_list_lp_filter_m2 = []
list_lp_filter_m1 = []
list_lp_filter_m2 = []
holding_list_kai_lp_filter_m1 = []
holding_list_kai_lp_filter_m2 = []
list_kai_lp_filter_m1 = []
list_kai_lp_filter_m2 = []



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
    pro = processing(500)
    DC0 = DC_remover(alpha=0.95)
    DC1 = DC_remover(alpha=0.95)
    DC2 = DC_remover(alpha=0.95)
    DC3 = DC_remover(alpha=0.95)

    time_endpoint = time.perf_counter() + 15.
    current_time = time.perf_counter()
    while current_time < time_endpoint:
        #hente value
        current_time = time.perf_counter()
        inc_msg = recv()
        x_1, x_2 = norm_data(inc_msg)

        #til plotting av RAW values
        fake_x1_0 = copy.copy(x_1)
        fake_x2_0 = copy.copy(x_2)
        list_raw_values_m1.extend(fake_x1_0)
        list_raw_values_m2.extend(fake_x2_0)

        #plotting av yn filtrert av blokk filter
        fake_x1_1 = copy.copy(x_1)
        fake_x2_1 = copy.copy(x_2)
        filter_x1 = DC0.block_data_DC_reomver(fake_x1_1)
        filter_x2 = DC1.block_data_DC_reomver(fake_x2_1)
        list_block_filter_m1.extend(filter_x1)
        list_block_filter_m2.extend(filter_x2)

        #plotting av yn filtrert av lp filter
        fake_x1_2 = copy.copy(x_1)
        fake_x2_2 = copy.copy(x_2)
        for i in range(len(fake_x1_2)):
            holding_list_lp_filter_m1.append(DC0.nett_filter(fake_x1_2[i]))
        for i in range(len(fake_x2_2)):
            holding_list_lp_filter_m2.append(DC1.nett_filter(fake_x2_2[i]))
        list_lp_filter_m1.extend(holding_list_lp_filter_m1)
        list_lp_filter_m2.extend(holding_list_lp_filter_m2)

        #plotting av yn filtrert av kai lp filter
        fake_x1_3 = copy.copy(x_1)
        fake_x2_3 = copy.copy(x_2)
        for i in range(len(fake_x1_3)):
            holding_list_kai_lp_filter_m1.append(DC2.kai_filter(fake_x1_3[i]))
        for i in range(len(fake_x2_3)):
            holding_list_kai_lp_filter_m2.append(DC3.kai_filter(fake_x2_3[i]))
        list_kai_lp_filter_m1.extend(holding_list_kai_lp_filter_m1)
        list_kai_lp_filter_m2.extend(holding_list_kai_lp_filter_m2)

        print(f'hps xn {pro.hps(fake_x1_0)}, hps yn BLOKK {pro.hps(filter_x1)}, hps yn LP {(pro.hps(holding_list_lp_filter_m1))}, hps yn Kai LP {(pro.hps(holding_list_kai_lp_filter_m1))}', "\n")
        # itte litt testing ser eg at hps alltid gir 0 på RAW og blokk filtrerte signalet
        # men på begge lp filtran så blir frekvensen alltid signalet/10

    #  lage variabla for fft
    LIST_RAW_VALUES_MIC_1 = np.fft.fft(list_raw_values_m1)
    LIST_RAW_VALUES_MIC_2 = np.fft.fft(list_raw_values_m2)
    LIST_BLOCK_FILTER_M1 = np.fft.fft(list_block_filter_m1)
    LIST_BLOCK_FILTER_M2 = np.fft.fft(list_block_filter_m2)
    LIST_LP_FILTER_M1 = np.fft.fft(list_lp_filter_m1)
    LIST_LP_FILTER_M2 = np.fft.fft(list_lp_filter_m2)
    LIST_KAI_LP_FILTER_M1 = np.fft.fft(list_kai_lp_filter_m1)
    LIST_KAI_LP_FILTER_M2 = np.fft.fft(list_kai_lp_filter_m2)
    #print(f'RAW m1 {list_mic_1}')
    #print(f'BLOKK m1 {filter_m1}')
    #print(f'LP m1 {lp_filter_m1}')

#plotting av data
    if False:
        plt.close(1); plt.figure(1, figsize=(10, 6))
        plt.subplot(4, 1, 1); plt.plot(list_raw_values_m1, color ='r'); plt.plot(list_raw_values_m2, color ='b'); plt.title(f'RAW signal'); plt.grid(True)
        plt.subplot(4, 1, 2); plt.plot(list_block_filter_m1, color='r'); plt.plot(list_block_filter_m2, color='b'); plt.title(f'blokk filtrert signal'); plt.grid(True)
        plt.subplot(4, 1, 3); plt.plot(list_lp_filter_m2, 'b');plt.plot(list_lp_filter_m1, 'r'); plt.xlabel("lp filtrert signal"); plt.grid(True)
        plt.subplot(4, 1, 4); plt.plot(list_kai_lp_filter_m1, 'b');plt.plot(list_kai_lp_filter_m2, 'r'); plt.xlabel("kai lp filtrert signal"); plt.grid(True)

    if False:
        plt.close(1);plt.figure(1, figsize=(10, 6))
        plt.subplot(4, 1, 1);plt.semilogy(np.real(LIST_RAW_VALUES_MIC_1), color='r');plt.semilogy(np.real(LIST_RAW_VALUES_MIC_2), color='b');plt.title(f'RAW signal'); plt.grid(True)
        plt.subplot(4, 1, 2);plt.semilogy(np.real(LIST_BLOCK_FILTER_M1), color='r');plt.semilogy(np.real(LIST_BLOCK_FILTER_M2), color='b');plt.title(f'blokk filtrert signal'); plt.grid(True)
        plt.subplot(4, 1, 3);plt.semilogy(np.real(LIST_LP_FILTER_M1), 'b');plt.semilogy(np.real(LIST_LP_FILTER_M2), 'r');plt.xlabel("lp filtrert signal"); plt.grid(True)
        plt.subplot(4, 1, 4);plt.semilogy(np.real(LIST_KAI_LP_FILTER_M1), 'b');plt.semilogy(np.real(LIST_KAI_LP_FILTER_M2), 'r');plt.xlabel("kai lp filtrert signal"); plt.grid(True)

    plt.tight_layout()
    plt.show()