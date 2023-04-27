import numpy as np
from numpy import cos, pi
import scipy.signal as sig

class processing():
    def __init__(self, Fs: int):
        self.Fs = Fs

    # A filter that can be used in order to delay a signal by a certain amount,
    # based on the distance specified
    def add_delay(self, xn, dist, fs):
        D = dist/343*fs # Avstand delt på lydhastighet
        D_int = round(D)
        D_frac = D-D_int
        L = 129
        n = np.arange(L)
        hn = np.sinc(n-(L-1)/2-D_frac)
        hn *= sig.hamming(L)
        hn = np.concatenate((np.zeros(D_int), hn))

        return sig.lfilter(hn, [1], xn)

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
    def cross_correlation(self, xn_1, xn_2, we):
        # Convert to frequency domain
        X1_k = np.fft.fft(xn_1)
        X2_k = np.fft.fft(xn_2)

        # Cross correlation
        #R_12 = X1_k*np.convolve(X2_k)                             # Cross correlation (Cc)
        #R_12 = X1_k*np.conjugate(X2_k)/(abs(X1_k)*abs(X2_k))      # Cc + noise whitening (nw)
        R_12 = (we*X1_k*np.conjugate(X2_k))/(abs(X1_k)*abs(X2_k))  # Cc + nw + weights

        # Convert to time domain by inverse FFT (IFFT)
        r_12 = np.fft.ifft(R_12)

        # Calculate time delay between the two signals and distance
        sample_delay = np.argmax(r_12)

        # In case there is a peak and the wrong side of the correlation
        if sample_delay > len(xn_1)/2:
            sample_delay -= len(xn_1)

        # Calculate the time and distance
        time_delay = sample_delay/self.samplerate
        distance = time_delay*343
        return time_delay, distance

    def spectral_weighing(self, mic, a, y):
        nr_mics = len(mic)       #  Amount of microphones
        nr_samples = len(mic[0]) #  This can be created with only 0, since all mics are same length

        # Empty arrays
        X_k = [0]*nr_samples
        Xn_k = [0]*nr_samples
        wk = [0]*nr_samples
        we_k = [0]*nr_samples

        # Convert the input values to frequency domain
        for j in range(nr_mics):
            mic[j] = np.fft.fft(mic[j])

        # Calculate values for every sample between all microphones
        for i in range(nr_mics):
            X_k[i] = (mic[0][i] + mic[1][i] + mic[2][i] + mic[3][i]) / nr_mics    # Average
            Xn_k[i] = max(0.01, np.sqrt( ((mic[0][i] - X_k[i]) +
                                          (mic[1][i] - X_k[i]) +
                                          (mic[2][i] - X_k[i]) +
                                          (mic[3][i] - X_k[i]))**2 / nr_mics ) )  # Std (noise)

            wk[i] = max(0.1, ((X_k[i] - (a * Xn_k[i])) / (X_k[i])) )              # Weight

            # based on function 5 in pdf: https://ieeexplore.ieee.org/document/1248813
            # we_k (weights with limits)
            if X_k[i] <= Xn_k[i]:
                we_k[i] = wk[i]
            elif X_k[i] > Xn_k[i]:
                we_k[i] = wk[i] * ( (X_k[i])/(Xn_k[i]) )**y

        return we_k

    # [0, -2, -4, 2]
    def norm_values(self, toad):
        norm_toad = [0]*len(toad)
        low_val = min(toad)  # Lowest value

        for i in range(len(toad)):
            norm_toad[i] = toad[i] + abs(low_val)

        return norm_toad

    @property
    def samplerate(self):
        return self.Fs
