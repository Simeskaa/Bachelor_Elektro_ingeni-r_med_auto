from numpy import sin, cos, pi, exp, empty, mean, abs, angle # Sentrale matematiske funksjoner
import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"
from scipy.io import wavfile



samplerate, data = wavfile.read('lyd_filer/shhtut_10.wav')
xn_rx = data.T[0]/0x7FFF
samplerate, data = wavfile.read('lyd_filer/tutut_2.wav')
pulse = data.T[0]/0x7FFF

Fs = samplerate
t_pulse = np.arange(len(pulse))/Fs
t_x = np.arange(len(xn_rx))/Fs


# plt.close(0), plt.figure(1)
# plt.subplot(2, 1, 1)
# plt.plot(t_pulse*10**6, pulse)
# plt.xlim([t_x[0], t_x[-1]*10**6])
# plt.xlabel(r'Tid ($\mu s$)')
# plt.title(r'Utgående signalpuls $x_{pulse}(t)$')
# plt.grid(True)
#
# plt.subplot(2, 1, 2)
# plt.plot(t_x*10**6, xn_rx)
# plt.xlim([t_x[0], t_x[-1]*10**6])
# plt.xlabel(r'Tid ($\mu s$)')
# plt.title(r'Innkommende signal $x_{rx}(t)$')
# plt.grid(True)
# plt.show()
# plt.tight_layout()

#--------------------------------------------------------------------------
N = len(pulse)
n = np.arange(N)
#hn = pulse[::-1]
#print(hn.shape)
#yn = sig.convolve(xn_rx, hn)
yn = sig.correlate(xn_rx, pulse)

plt.close(2); plt.figure(2, figsize=(9, 3))

plt.plot(yn)

#plt.xlim([t_x[0], t_x[-1]*10**6])
plt.xlabel(r'Tid ($s$)')
plt.title(r'Filtrert innkommende signal $y(t_n)$')
plt.grid(True)
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------