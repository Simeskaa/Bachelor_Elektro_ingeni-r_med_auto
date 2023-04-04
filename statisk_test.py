from numpy import sin, cos, pi, exp, empty, mean, abs, angle # Sentrale matematiske funksjoner
import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"
from scipy.io import wavfile
from QT_plot_statisc import Example, cordinate, polar_to_cartesian, polar_to_cartesian_list_version, cordinate_list_version
import sys
from PySide6.QtWidgets import *
import copy

samplerate, data = wavfile.read('lyd_filer/shhtut_10.wav')
xn_rx_1 = data.T[0] / 0x7FFF
xn_rx_2 = xn_rx_1[117:]
xn_rx_3 = xn_rx_1
xn_rx_1 = xn_rx_1[502:]

samplerate, data = wavfile.read('lyd_filer/tutut_2.wav')
pulse = data.T[0]/0x7FFF

# Define the side length of the equilateral triangle
triangle_side_length = 1.0  # in meters

# Define the positions of the three microphones as 3D coordinates
mic_positions = np.array([
    [0.0, 0.0, 0.0],  # Microphone 1 at the origin
    [triangle_side_length, 0.0, 0.0],  # Microphone 2 at (1, 0, 0)
    [triangle_side_length/2, triangle_side_length*np.sqrt(3)/2, 0.0],  # Microphone 3 at (0.5, sqrt(3)/2, 0)
])

def convolve(signal):
    yn = sig.correlate(signal, pulse)
    return yn

def sample_to_time(sample):
    t = sample/samplerate
    return t

#function created by chatgpt
def convert_range(value, old_min, old_max, new_min, new_max):
    """Converts a value from an old range to a new range."""
    old_range = old_max - old_min
    new_range = new_max - new_min
    scaled_value = (((value - old_min) * new_range) / old_range) + new_min
    return scaled_value

def angle_calc(tdoas: list, spd_sound: float, spacing: float):
    diff = max(tdoas[2], tdoas[1]) - min(tdoas[2], tdoas[1])
    dist = diff * spd_sound
    angle = 90 - np.arccos(dist/spacing) * 180/np.pi
    return angle

def angle_calc2(tdoas: list, spd_sound: float, spacing: float):
    tdoas_temp = copy.copy(tdoas)
    ref = np.argmin(tdoas_temp)
    if ref == 0:
        offsett = 90
        print("ref: front")
    elif ref == 1:
        offsett = 270
        print("ref: right")
    elif ref == 2:
        offsett = 360
        print("ref: left")
    else:
        print("ref: multiple or error")

    print(tdoas_temp)
    tdoas_temp.remove(tdoas_temp[ref])
    #print(tdoas_temp)
    diff = (max(tdoas_temp[1], tdoas_temp[0]) - min(tdoas_temp[1], tdoas_temp[0])) # *10**-3 uncomment if in millis
    #print("diff:", diff)
    dist = diff * spd_sound
    #print("dist:", dist)
    angle = np.arccos(dist/spacing) * 180/np.pi
    print(angle)
    return angle

def angle_calc4(tdoas: list, spd_sound: float, spacing: float):
    #tdoas_temp = copy.copy(tdoas)
    #tdoas_temp = tdoas_temp[1:]
    #print(tdoas_temp)
    time_diff = tdoas[2] - tdoas[1]
    dist = time_diff * spd_sound
    angle = np.arccos(dist / spacing)
    #print(dist)
    #print(angle)
    if tdoas[0] > tdoas[3]:
        angle = 2*np.pi - angle
    return angle

def angle_calc5(tdoas: dict, spd_sound: float, spacing_big: float, spacing_little: float):
    angle_m2_m3 = np.arccos((tdoas['m2'] - tdoas['m3'])*spd_sound/spacing_big)
    angle_m1_m4 = np.arccos((tdoas['m1'] - tdoas['m4']) * spd_sound / spacing_big)
    angle_m2_m4 = np.arccos((tdoas['m2'] - tdoas['m4']) * spd_sound / spacing_little)
    angle_m1_m3 = np.arccos((tdoas['m1'] - tdoas['m3']) * spd_sound / spacing_little)
    angle_m2_m1 = np.arccos((tdoas['m2'] - tdoas['m1']) * spd_sound / spacing_little)
    angle_m4_m3 = np.arccos((tdoas['m4'] - tdoas['m3']) * spd_sound / spacing_little)

    list_angles = [angle_m2_m3, angle_m1_m4, angle_m2_m4, angle_m1_m3, angle_m2_m1, angle_m4_m3]
    # if tdoas['m1'] > tdoas['m4']: #denna if setningen føkke meg
    #     for i in range(len(list_angles)):
    #         list_angles[i] = 2 * np.pi - list_angles[i]
    angle = {}
    for i in range( 6):
        name = f'angle {i+1}'
        angle[name] = list_angles[i]


    for i in range(len(list_angles)):
        list_angles[i] = list_angles[i] * 180/np.pi

    print(list_angles)
    #print(angle)
    return angle

#print("samplerate:", samplerate)
#print("Antall sampler:", len(xn_rx_1))


# yn1 = convolve(xn_rx_1)
# yn2 = convolve(xn_rx_2)
# yn3 = convolve(xn_rx_3)
#
# sample1 = np.argmax(yn1)-len(pulse)+1
# sample2 = np.argmax(yn2)-len(pulse)+1
# sample3 = np.argmax(yn3)-len(pulse)+1
#
# t1 = sample_to_time(sample1)
# t2 = sample_to_time(sample2)
# t3 = sample_to_time(sample3)

#print("Mic1 starter:", sample1, "time:", round(t1, 3), "offsett(s):", 0)
#print("Mic2 starter:", sample2, "time:", round(t2, 3), "offsett(ms):", round(t2-t1, 4)*10**3)
#print("Mic3 starter:", sample3, "time:", round(t3, 3), "offsett(ms):", round(t3-t1, 4)*10**3)



#--------------------------------------------------------------------------

if False:
    plt.close(2); plt.figure(2, figsize=(9, 3))
    plt.plot(yn1, color='blue')
    plt.plot(yn2, color='red')
    plt.plot(yn3, color='green')
    plt.xlabel(r'Tid ($s$)')
    plt.title(r'Filtrert innkommende signal $y(t_n)$')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#--------------------------------------------------------------------------

#hånd generert timestamps
t1 = 0.0
t2 = 0.019
t3 = 0.029
t4 = t3 + t2

toa = [t1, t2, t1, t3]
mic = {'m1':t1, 'm2':t3, 'm3':t2, 'm4':t4}

angle_list = angle_calc5(mic, 343.0, 12.*np.sqrt(2.), 12.)
#print(polar_to_cartesian_list_version(2000., angle_list))

#print(f't1 = {toa[0]}, t2 = {toa[1]}, t3 = {toa[2]}, t4 = {toa[3]}, angle = {angle_calc4(toa, 343.0, 12.*np.sqrt(2.))*180/(np.pi)}')
"""
ref = np.argmin(toa)
tdoas = [float(toa[0] - toa[ref]), float(toa[1] - toa[ref]), float(toa[2]- toa[ref])]
"""
#vinkel beregning
#vinkel = angle_calc4(toa, 343.0, 12.*np.sqrt(2.))

#plotting av vinkel
app = QApplication(sys.argv)
ex = Example()
#x,y = polar_to_cartesian(200, vinkel)
#x, y = cordinate(x,y)

#print(angle_list)
cart_cord = polar_to_cartesian_list_version(1000, angle_list)
print(cart_cord)
center_cord = cordinate_list_version(cart_cord)
start_cord = {'x_1': 6*np.sqrt(2), 'y_1': 0, 'x_2': 6*np.sqrt(2), 'y_2': 0, 'x_3': 3*np.sqrt(2), 'y_3': -3*np.sqrt(2), 'x_4': 9*np.sqrt(2), 'y_4': 3*np.sqrt(2), 'x_5': 3*np.sqrt(2), 'y_5': 3*np.sqrt(2), 'x_6': 9*np.sqrt(2), 'y_6': -3*np.sqrt(2)}
center_start_cord = cordinate_list_version(start_cord)
#print(cart_cord)
#print(center_cord)
test = ex.make_line(start_cord= center_start_cord, end_cord= center_cord)
print(test)
ex.testUI(358, 359)

#ex.show()
#sys.exit(app.exec())
