import numpy as np
from numpy import cos, pi
import scipy.signal as sig

class processing():
    def __init__(self, Fs: int):
        self.Fs = Fs

    # Harmonic Product Spectrum
    # Is used in order to find the dominating frequency in a signal
    def hps(self, xn):
        # Creating variables 
        L = len(xn)
        Xk_mag = np.abs(np.fft.fft(xn))

        N = L//8
        Yk = Xk_mag[0:N]

        for i in range(2,5):
            Yk *= Xk_mag[0:i:i*N]

        peak_location = np.argmax(Yk)
        frequency = peak_location/L*self.Fs

        return frequency

    # Correlation between two signals, with Fast Fourier Transformation (FFT)
    def cross_correlation(self, xn_1, xn_2):
        # Convert to frequency domain
        X1_k = np.fft.fft(xn_1)
        X2_k = np.fft.fft(xn_2)

        # Cross correlation
        R_12 = X1_k*np.convolve(X2_k)

        # Convert to time domain by inverse FFT (IFFT)
        r_12 = np.fft.ifft(R_12)

        # Calculate time delay between the two signals and,
        # the estimated distance between the two (mostly for debugging)
        time_delay = round((np.argmax(r_12)/self.Fs)*10**3, 2)  # present the result in milliseconds (ms)
        distance = np.argmax(r_12)/self.Fs*343  # 343m/s is the speed of sound
        return time_delay, distance

    def spectral_weighing(self, mic, a, y):
        # Empty arrays
        X_k = [0]*len(mic[0])
        Xn_k = [0]*len(mic[0])
        wk = [0]*len(mic[0])
        we_k = [0]*len(mic[0])

        # Find average between mics, std, and thereafter weight
        for i in range(len(mic[0])):
            X_k[i] = (mic[0][i] + mic[1][i])/len(mic) # Avg
            # If this is removed, in some cases the program divide by zero,
            # And values become Nan
            #if X_k[i] == 0:
            #    X_k[i] = 0.1

            Xn_k[i] = max(0.01, np.sqrt(  ((mic[0][i] - X_k[i]) + (mic[1][i] - X_k[i]) )**2 /len(mic) ) ) # Std
            wk[i] = max(0.1, ((X_k[i] - (a * Xn_k[i])) / (X_k[i])) )  # Weight

            # based on function 5 in pdf: https://ieeexplore.ieee.org/document/1248813
            # we_k has to be created
            if X_k[i] <= Xn_k[i]:
                we_k[i] = wk[i]
            elif X_k[i] > Xn_k[i]:
                we_k[i] = wk[i] * ( (X_k[i])/(Xn_k[i]) )**y

            # Debugging purposes
            if False:
                print("Raw:{}, {}".format(round(mic[0][i],2), round(mic[1][i],2)),
                      "\nAvg:{}".format(round(X_k[i], 2)),
                      "\nStd:{}".format(round(Xn_k[i], 2)),
                      "\nwk :{}\n".format(round(wk[i], 2))
                     )
        return we_k, wk, X_k, Xn_k

    @property
    def samplerate(self):
        return self.Fs
