from numpy import sin, cos, pi, exp, empty, mean, abs, angle # Sentrale matematiske funksjoner
import numpy as np                          # Importer funksjonalitet fra numpy biblioteket med prefiks "np"
import scipy.signal as sig                  # Importerer signalbehandlingsmodulen til scipy
import matplotlib.pyplot as plt             # Importer pyplot modulen i matplotlib med prefiks "plt"
from scipy.io import wavfile
import wave


samplerate, data = wavfile.read('lyd_filer/tutut.wav')
print()

plt.close(0), plt.figure(1)
plt.plot(data)
plt.show()


print(samplerate)



