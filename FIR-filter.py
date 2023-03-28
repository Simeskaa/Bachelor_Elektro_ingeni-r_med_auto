from numpy import sin, cos, pi, exp, empty, mean, abs, angle # Sentrale matematiske funksjoner
import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"
from scipy.io import wavfile

samplerate, data = wavfile.read('lyd_filer/shhtut_10.wav')
xn_rx = data.T[0] / 0x7FFF
samplerate, data = wavfile.read('lyd_filer/tutut_2.wav')
pulse = data.T[0]/0x7FFF
Fs = samplerate

# Generer tids-arrays for de to signalene for bruk i plot
t_pulse = np.arange(len(pulse))/Fs
t_x = np.arange(len(xn_rx))/Fs

if False:
    # Vis pulsform og mottatt signal i to subplot
    plt.close(1); plt.figure(1, figsize=(9, 5))

    plt.subplot(2, 1, 1)
    plt.plot(t_pulse, pulse)
    plt.xlim([t_x[0], t_x[-1]])
    plt.xlabel("Tid(s)")
    plt.title(r'Utgående signalpuls $x_{pulse}(t)$')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(t_x, xn_rx)
    plt.xlim([t_x[0], t_x[-1]])
    plt.xlabel("Tid(s)")
    plt.title(r'Innkommende signal $x_{rx}(t)$')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

hn = pulse[::-1]
yn = np.convolve(hn, xn_rx)

if False:
    plt.close(2); plt.figure(2,figsize=(9, 3))

    plt.plot(t_x, yn[0:len(xn_rx)])
    plt.xlim([t_x[0], t_x[-1]])
    plt.xlabel("Tid(s)")
    plt.title(r'Filtrert innkommende signal $y(t_n)$')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

f, Hw = sig.freqz(b = hn, fs=Fs, worN = 1024)  # Regn ut frekvensresponsen til filteret
Hw_amp = np.abs(Hw)

if True:
    # Presenter frekvensresponsen grafisk.
    plt.close(2); plt.figure(2)
    plt.plot(f, Hw_amp)


    #plt.close(3); plt.figure(3)
    #plt.semilogy(np.fft.fft(np.abs(xn_rx)))
    plt.show()
    #print(np.argmax(Hw))
