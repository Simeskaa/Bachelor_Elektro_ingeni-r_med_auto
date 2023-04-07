from numpy import sin, cos, pi, exp, empty, mean, abs, angle # Sentrale matematiske funksjoner
import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"
from scipy.io import wavfile
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
        offsett = 180
        print("ref: right")
    elif ref == 2:
        offsett = 270
        print("ref: left")
    else:
        print("ref: multiple or error")

    #print(tdoas_temp)
    print(f"temp:{tdoas_temp}, norm:{tdoas}")
    tdoas_temp.remove(tdoas_temp[ref])
    print(f"temp:{tdoas_temp}, norm:{tdoas}")
    #print(tdoas_temp)
    diff = (max(tdoas_temp[1], tdoas_temp[0]) - min(tdoas_temp[1], tdoas_temp[0])) # *10**-3 uncomment if in millis
    #print("diff:", diff)
    dist = diff * spd_sound
    #print("dist:", dist)
    angle = offsett - np.arccos(dist/spacing) * 180/np.pi
    return angle


# print("samplerate:", samplerate)
# print("Antall sampler:", len(xn_rx_1))


yn1 = convolve(xn_rx_1)
yn2 = convolve(xn_rx_2)
yn3 = convolve(xn_rx_3)

plt.close(); plt.figure(1)
plt.subplot(2,1,1)
plt.title('Filtered Signal')
plt.plot(yn1)

plt.subplot(2,1,2)
plt.title('Raw Signal')
plt.plot(xn_rx_1)
plt.tight_layout()
plt.show()

sample1 = np.argmax(yn1)-len(pulse)+1
sample2 = np.argmax(yn2)-len(pulse)+1
sample3 = np.argmax(yn3)-len(pulse)+1

t1 = sample_to_time(sample1)
t2 = sample_to_time(sample2)
t3 = sample_to_time(sample3)

# print("Mic1 starter:", sample1, "time:", round(t1, 3), "offsett(s):", 0)
# print("Mic2 starter:", sample2, "time:", round(t2, 3), "offsett(ms):", round(t2-t1, 4)*10**3)
# print("Mic3 starter:", sample3, "time:", round(t3, 3), "offsett(ms):", round(t3-t1, 4)*10**3)



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
# toa = [t1, t2, t3]
# ref = np.argmin(toa)
# print("ref:", ref)
# tdoas2 = [float(t1 - toa[ref]), float(t2 - toa[ref]), float(t3 - toa[ref])]
# print("angle from", tdoas2, "is:", angle_calc2(tdoas=tdoas2, spd_sound=434.0, spacing=12))
#
# print(angle_calc2(tdoas2, 434.0, 12))


