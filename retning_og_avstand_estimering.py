import numpy as np
import copy
from QT_plot_statisc import Example, polar_to_cartesian_list_version, cordinate_list_version
import sys
from PySide6.QtWidgets import *


def angle_calc6(tdoas:list, spd_sound: float, spacing_big: float, spacing_little: float):
    fake_mics = []
    tdoas_temp = copy.copy(tdoas)

    #snur koordinatsystemet
    for i in range(4):
        ref = np.argmin(tdoas_temp)
        fake_mics.append(tdoas_temp[ref])
        tdoas_temp.remove(tdoas_temp[ref])

    m2_m1 = tdoas[2] - tdoas[0]
    m2_m3 = tdoas[2] - tdoas[1]
    m2_m4 = tdoas[2] - tdoas[3]
    m1_m4 = tdoas[0] - tdoas[3]
    m1_m3 = tdoas[0] - tdoas[1]
    m4_m3 = tdoas[3] - tdoas[1]

    sound_diff_1 = ((m2_m1 >= 0) and (m2_m3 >= 0 ) and (m4_m3 >= 0)) and ((m2_m4 < 0) and (m1_m4 < 0) and (m1_m3 < 0))
    sound_diff_2 = ((m2_m1 < 0) and (m2_m3 < 0) and (m2_m4 < 0) and (m1_m4 < 0) and (m1_m3 < 0) and (m4_m3 < 0))
    sound_diff_3 = ((m2_m1 < 0) and (m2_m3 < 0 ) and (m4_m3 < 0)) and ((m2_m4 >= 0) and (m1_m4 >= 0) and (m1_m3 >= 0))
    sound_diff_4 = ((m2_m1 >= 0) and (m2_m3 >= 0) and (m2_m4 >= 0) and (m1_m4 >= 0) and (m1_m3 >= 0) and (m4_m3 >= 0))

    if ( sound_diff_1 or sound_diff_2 or sound_diff_3 or sound_diff_4):

        fma = {'m1': fake_mics[0], 'm2': fake_mics[2], 'm3': fake_mics[1], 'm4': fake_mics[3]}
    else:
        fma = {'m1': fake_mics[1], 'm2': fake_mics[3], 'm3': fake_mics[0], 'm4': fake_mics[2]}

    #beregne vinkla
    angle_m2_m3 = np.arccos((fma['m2'] - fma['m3']) * spd_sound / spacing_big) + 0
    angle_m1_m4 = np.arccos((fma['m1'] - fma['m4']) * spd_sound / spacing_big) - np.pi/2
    angle_m2_m4 = np.arccos((fma['m2'] - fma['m4']) * spd_sound / spacing_little) - np.pi/4
    angle_m1_m3 = np.arccos((fma['m1'] - fma['m3']) * spd_sound / spacing_little) - np.pi/4
    angle_m2_m1 = np.arccos((fma['m2'] - fma['m1']) * spd_sound / spacing_little) + np.pi/4
    angle_m4_m3 = np.arccos((fma['m4'] - fma['m3']) * spd_sound / spacing_little) + np.pi/4

    list_angles = [angle_m2_m3, angle_m1_m4, angle_m2_m4, angle_m1_m3, angle_m2_m1, angle_m4_m3]

    #gjør det øve te ein dictonary
    angle = {}
    for i in range(6):
        name = f'angle {i+1}'
        angle[name] = list_angles[i]


    #negativ vinkel fix te problem vinklan
    if fma['m1'] > fma['m3']:
        angle['angle 5'] = np.pi/2 - angle['angle 5']
        angle['angle 6'] = np.pi/2 - angle['angle 6']

    #bestemme kvadrant

    tdoas_temp2 = copy.copy(tdoas)

    for i in range(2):
        ref = np.argmax(tdoas_temp2)
        tdoas_temp2.remove(tdoas_temp2[ref])

    #print(fake_mics)

    #bestemme kvadrant
    if (tdoas_temp2 == [tdoas[0],tdoas[1]]):
        #print("Kvadrant 1, + 0deg")
        pass

    elif(tdoas_temp2 == [tdoas[0],tdoas[2]]):
        #print("Kvadrant 2, + 90deg")
        for i in range(6):
            name = f'angle {i + 1}'
            angle[name] = angle[name] + np.pi/2
    elif (tdoas_temp2 == [tdoas[2], tdoas[3]]):
        #print("Kvadrant 3, + 180deg")
        for i in range(6):
            name = f'angle {i + 1}'
            angle[name] = angle[name] + np.pi
    elif (tdoas_temp2 == [tdoas[1], tdoas[3]]):
        #print("Kvadrant 4, + 270deg")
        for i in range(6):
            name = f'angle {i + 1}'
            angle[name] = angle[name] + np.pi*3/2

    angle_read = {}
    #gjør radiana øve te grade
    #for i in range(len(list_angles)):
   #     name = f'angle {i + 1}'
   #     angle_read[name] = angle[name] * 180 / np.pi

    #print(angle_read)
    return angle

def anglechenanigens():
    toad_78 = [0, 0.019, 0.029, 0.048]
    toad_45 = [0.0, 0.0, 0.03498542274, 0.03498542274]
    toad_34 = [0., (1.37 + 0.92) / 343, (1.37 + 0.92 + 9.506) / 343, (1.37 + 0.92 + 9.506 + 1.438 + 0.809) / 343]

    nummer = 2

    if nummer == 0:
        # alt ser ut te å fungera her
        t1 = toad_78[0]
        t2 = toad_78[1]
        t3 = toad_78[2]
        t4 = toad_78[3]
        mic = {'m1': t1, 'm2': t3, 'm3': t2, 'm4': t4}

    if nummer == 1:
        t1 = toad_45[0]
        t2 = toad_45[1]
        t3 = toad_45[2]
        t4 = toad_45[3]
        mic = {'m1': t3, 'm2': t4, 'm3': t1, 'm4': t2}

    if nummer == 2:
        # må finna ein bære måte å beregna 45 gradaren på
        t1 = toad_34[0]
        t2 = toad_34[1]
        t3 = toad_34[2]
        t4 = toad_34[3]
        mic = {'m1': t2, 'm2': t4, 'm3': t1, 'm4': t3}

    # print("")
    # print(mic)

    toad = [mic['m1'], mic['m3'], mic['m2'], mic['m4']]
    angle = angle_calc6(toad, 343.0, 12. * np.sqrt(2.), 12.)

    return angle

def main():
    angle_list = anglechenanigens()
    app = QApplication(sys.argv)
    ex = Example()
    #print('1')
    #print(angle_list['angle 1']*180/np.pi)

    cart_cord = polar_to_cartesian_list_version(2000, angle_list)
    #print('2')
    #print(cart_cord)

    #center_cord = cordinate_list_version(cart_cord)
    #print('3')
    #print(center_cord['x_1'], center_cord['y_1'])
    # start_cord = {'x_1': 6 * np.sqrt(2), 'y_1': 0, 'x_2': 6 * np.sqrt(2), 'y_2': 0,
    #               'x_3': 3 * np.sqrt(2), 'y_3': -3 * np.sqrt(2), 'x_4': 9 * np.sqrt(2), 'y_4': 3 * np.sqrt(2),
    #               'x_5': 3 * np.sqrt(2), 'y_5': 3 * np.sqrt(2), 'x_6': 9 * np.sqrt(2), 'y_6': -3 * np.sqrt(2)}

    # start_cord = {'x_1': 0, 'y_1': 0, 'x_2': 6 * np.sqrt(2), 'y_2': 6 * np.sqrt(2), #HUSK AT START KORD MÅ FLYTTAS TE VENSTRE
    #               'x_3': 0, 'y_3': 0, 'x_4': 6 * np.sqrt(2), 'y_4': 6 * np.sqrt(2),
    #               'x_5': 0, 'y_5': 0, 'x_6': 6 * np.sqrt(2), 'y_6': -6 * np.sqrt(2)}

    start_cord = {'x_1': -6 * np.sqrt(2), 'y_1': 0, 'x_2': 0, 'y_2': 6 * np.sqrt(2),
                  'x_3': -6 * np.sqrt(2), 'y_3': 0, 'x_4': 0, 'y_4': 6 * np.sqrt(2),
                  'x_5': -6 * np.sqrt(2), 'y_5': 0, 'x_6': 0, 'y_6': -6 * np.sqrt(2)}

    #print('4')
    #print(start_cord)
    #center_start_cord = cordinate_list_version(start_cord)
    #print('5')
    #print(center_start_cord['x_1'], center_start_cord['y_1'])
    test = ex.make_line(start_cord= start_cord, end_cord= cart_cord)
    #print('7')
    #print(test)
if __name__ == '__main__':
   main()