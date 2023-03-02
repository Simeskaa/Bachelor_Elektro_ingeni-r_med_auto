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

def angle_calc(deg, length):
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

yn1 = convolve(xn_rx_1)
yn2 = convolve(xn_rx_2)
yn3 = convolve(xn_rx_3)

sample1 = np.argmax(yn1)-len(pulse)+1
sample2 = np.argmax(yn2)-len(pulse)+1
sample3 = np.argmax(yn3)-len(pulse)+1

t1 = sample_to_time(sample1)
t2 = sample_to_time(sample2)
t3 = sample_to_time(sample3)

print(angle_calc(75, 12))

print("Mic1 starter:", sample1, "time:", round(t1, 3), "offsett(s):", 0)
print("Mic2 starter:", sample2, "time:", round(t2, 3), "offsett(ms):", round(t2-t1, 4)*10**3)
print("Mic3 starter:", sample3, "time:", round(t3, 3), "offsett(ms):", round(t3-t1, 4)*10**3)

