from numpy import sin, cos, pi, exp, empty, mean, abs, angle # Sentrale matematiske funksjoner
import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"
from scipy.io import wavfile
from QT_plot_statisc import Example, cordinate, polar_to_cartesian
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

def angle_calc3(tdoas: list, spd_sound: float, spacing: float):
    tdoas_temp = copy.copy(tdoas)
    tdoas_temp = tdoas_temp[1:]
    print(tdoas_temp)
    ref = np.argmin(tdoas_temp[1:])
    if ref == 0:
        print("t2 is ref")

    elif ref == 1:
        print("t3 is ref")
    diff = (max(tdoas_temp[0], tdoas_temp[1]) - min(tdoas_temp[0], tdoas_temp[1]))
    dist = diff * spd_sound
    angle = np.arccos(dist / spacing) * 180 / np.pi
    return angle

def angle_calc4(tdoas: list, spd_sound: float, spacing: float):
    tdoas_temp = copy.copy(tdoas)
    tdoas_temp = tdoas_temp[1:]
    time_diff = tdoas_temp[2] - tdoas_temp[1]
    dist = time_diff * spd_sound
    angle = np.arccos(dist / spacing) * 180 / np.pi

    "if mic1 >= mic 2 or mic 1>= mic2:" \
    "angle + nåe"
    return angle


print("samplerate:", samplerate)
print("Antall sampler:", len(xn_rx_1))


yn1 = convolve(xn_rx_1)
yn2 = convolve(xn_rx_2)
yn3 = convolve(xn_rx_3)

sample1 = np.argmax(yn1)-len(pulse)+1
sample2 = np.argmax(yn2)-len(pulse)+1
sample3 = np.argmax(yn3)-len(pulse)+1

t1 = sample_to_time(sample1)
t2 = sample_to_time(sample2)
t3 = sample_to_time(sample3)

print("Mic1 starter:", sample1, "time:", round(t1, 3), "offsett(s):", 0)
print("Mic2 starter:", sample2, "time:", round(t2, 3), "offsett(ms):", round(t2-t1, 4)*10**3)
print("Mic3 starter:", sample3, "time:", round(t3, 3), "offsett(ms):", round(t3-t1, 4)*10**3)



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

#toa = [t1, t2, t3]
toa = [t1, t2, t3]
print(f't1 = {t1} t2 = {t2} t3 = {t3}')
ref = np.argmin(toa)
tdoas = [float(toa[0] - toa[ref]), float(toa[1] - toa[ref]), float(toa[2]- toa[ref])]
print("angle from", toa, "is:", angle_calc3(toa, 434.0, 12))

#print("ANGLE:", angle_calc2(tdoas, 434.0, 12))
#vinkel = angle_calc2(tdoas, 434.0, 12)



# app = QApplication(sys.argv)
# ex = Example()
# print(vinkel)
# vinkel_rad = vinkel*(np.pi/180)
# print(vinkel_rad)
# x,y = polar_to_cartesian(200, vinkel_rad)
# print(f'x er {x}, y er {y}')
# x, y = cordinate(x,y)
# print(f'x er {x}, y er {y}')
# ex.testUI(x, y)
# #ex.show()
# sys.exit(app.exec())
