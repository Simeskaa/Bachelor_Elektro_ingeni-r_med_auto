import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"
from scipy.io import wavfile
from Triangulator import Triangulator

samplerate, data = wavfile.read('lyd_filer/shhtut_10.wav')
xn_rx_1 = data.T[0] / 0x7FFF
xn_rx_2 = xn_rx_1[117:]
xn_rx_3 = xn_rx_1
xn_rx_1 = xn_rx_1[502:]

samplerate, data = wavfile.read('lyd_filer/tutut_2.wav')
pulse = data.T[0]/0x7FFF

# Define the side length of the equilateral triangle
triangle_side_length = 12.0  # in meters

# Define the positions of the three microphones as 3D coordinates
mic_positions = np.array([
    [0.0, 0.0, 0.0],  # Microphone 1 at the origin
    [triangle_side_length, 0.0, 0.0],  # Microphone 2 at (1, 0, 0)
    [triangle_side_length/2, triangle_side_length*np.sqrt(3)/2, 0.0],  # Microphone 3 at (0.5, sqrt(3)/2, 0)
])

def angle_calculator(deg, length):
    angle = deg % 180
    angle %= 60
    hyp = length - (length * (angle/60))
    mot = hyp * np.sin(30 * np.pi / 180)
    hos = hyp * np.cos(30 * np.pi / 180)
    dist = np.sqrt(np.square(length-mot) + np.square(hos))
    print("angle:", angle)
    # print("dist:", dist)
    # print("hyp:", hyp)
    # print("mot:", mot)
    # print("hos:", hos)
    if deg <= 60:
        time3 = round(dist/434, 3)
        time2 = round(hyp/434, 3)
        time1 = round((length-hyp)/434, 3)
    elif 60 < deg <= 120:
        time3 = round(hyp/434, 3)
        time2 = round((length-hyp)/434, 3)
        time1 = round(dist/434, 3)
    else:
        time3 = round((length-hyp)/434, 3)
        time2 = round(dist/434, 3)
        time1 = round(hyp/434, 3)

    return time1, time2, time3

def convolve(signal):
    yn = sig.correlate(signal, pulse)
    return yn

def sample_to_time(sample):
    t = sample/samplerate
    return t

def angle_of_arrival_calculator(time1, time2, time3, length):
    c = 343  # Speed of sound in m/s
    t1 = time1 * c
    t2 = time2 * c
    t3 = time3 * c

    if t1 < t2 and t1 < t3:
        x = t1 / length
        y = np.sqrt(t2**2 - length**2 * x**2)
        angle = np.arctan2(y, length * x) * 180 / np.pi
    elif t2 < t1 and t2 < t3:
        x = (length - t2) / length
        y = np.sqrt(t3**2 - length**2 * (1 - x)**2)
        angle = np.arctan2(y, length * (1 - x)) * 180 / np.pi
    else:
        x = (length - t3) / length
        y = np.sqrt(t2**2 - length**2 * (1 - x)**2)
        angle = 180 - np.arctan2(y, length * (1 - x)) * 180 / np.pi

    return angle


yn1 = convolve(xn_rx_1)
yn2 = convolve(xn_rx_2)
yn3 = convolve(xn_rx_3)

sample1 = np.argmax(yn1)-len(pulse)+1
sample2 = np.argmax(yn2)-len(pulse)+1
sample3 = np.argmax(yn3)-len(pulse)+1

t1 = sample_to_time(sample1)
t2 = sample_to_time(sample2)
t3 = sample_to_time(sample3)

print(angle_calculator(15, 12))
#angle = angle_calc(t1, t2, t3)
#print("Angle of arrival:", angle)

print("Mic1 starter:", sample1, "time:", round(t1, 3), "offsett(s):", round(t1, 1))
print("Mic2 starter:", sample2, "time:", round(t2, 3), "offsett(ms):", round(t2-t1, 4)*10**3)
print("Mic3 starter:", sample3, "time:", round(t3, 3), "offsett(ms):", round(t3-t1, 4)*10**3)

print(angle_of_arrival_calculator(0, t2-t1, t3-t1, 12))
