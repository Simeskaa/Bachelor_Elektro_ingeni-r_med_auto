from numpy import sin, cos, pi, exp, empty, mean, abs, angle # Sentrale matematiske funksjoner
import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"


b = [0.000000000000000,
     0.004405638449924,
     0.015023539657151,
     0.003217890179612]

a = [1.000000000000000,
     -2.376802064798698,
     1.932937224176488,
     -0.533488091091103]

M = 3
x_buffer = [0] * M
y_buffer = [0] * M

fs = 4000
fzero = 100
L= fs//fzero
hn_lp = np.ones(L)/L
w_bp = pi/14

hn_bp = cos(w_bp*np.arange(L))*2*sig.hamming(L) #multipliser med 2 for å svare på spørmål b)

w, Hw = sig.freqz(b = hn_bp, fs=fs, worN=512)  # Regn ut frekvensresponsen til filteret

Hw_amp = np.abs(Hw)
Hw_phase = (np.angle(Hw))

# Presenter frekvensresponsen grafisk.
plt.close(1); plt.figure(1)
plt.subplot(2,1,1)
plt.title(r'Frekvensrespons til digitalt filter')
plt.plot(w, Hw_amp)
plt.grid(True)
plt.ylabel(r'Styrkegrad')
plt.subplot(2,1,2)
plt.plot(w, Hw_phase)
plt.grid(True)
plt.xlabel(r'Digital Frekvens (Hz)')
plt.ylabel(r'Fase')


plt.show()

def IIR_filter(x: float):
    # Regn ut verdien av y
    y = x * b[0]
    for i in range(M):
        y += b[i + 1] * x_buffer[i]
        y -= a[i + 1] * y_buffer[i]
    y /= a[0]

    #Oppdatere buffere
    x_buffer.remove(x_buffer[0])
    x_buffer.append(x)

    y_buffer.remove(y_buffer[0])
    y_buffer.append(y)
    return y

def FIR_filter(x: float):
    pass
