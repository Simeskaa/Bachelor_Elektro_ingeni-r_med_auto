import numpy as np
from numpy import cos, pi
import scipy.signal as sig
import copy
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

    def HPS2(self, xn, samplerate=44100):
        L = len(xn)
        hps_array = []
        spectrum = np.abs(np.fft.rfft(xn))
        hps_spectrum = np.copy(spectrum)
        hps_array.append(spectrum)

        for h in range(2, 5):  # Harmonics from 2 to 4 (adjust as needed)
            downsampled_spectrum = np.copy(spectrum[::h])
            hps_array.append(downsampled_spectrum)
            hps_spectrum[:len(downsampled_spectrum)] *= downsampled_spectrum

        peak_location = np.argmax(hps_spectrum)
        frequency = peak_location/L*samplerate

        return frequency, hps_array, hps_spectrum

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
        #R_12 = X1_k*np.conjugate(X2_k)                            # Cross correlation (Cc)
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

        mic_fft = [0]*4
        mic_fft[0] = np.fft.fft(mic[0])
        mic_fft[1] = np.fft.fft(mic[1])
        mic_fft[2] = np.fft.fft(mic[2])
        mic_fft[3] = np.fft.fft(mic[3])

        # Empty arrays
        X_k = [0]*nr_samples
        Xn_k = [0]*nr_samples
        wk = [0]*nr_samples
        we_k = [0]*nr_samples

        # Convert the input values to frequency domain
        #for j in range(nr_mics):
        #    mic_fft[j] = np.fft.fft(mic_fft[j])

        # Calculate values for every sample between all microphones
        for i in range(nr_samples):
            X_k[i] = (mic_fft[0][i] + mic_fft[1][i] + mic_fft[2][i] + mic_fft[3][i]) / nr_mics    # Average
            Xn_k[i] = max(0.01, np.sqrt( ((mic_fft[0][i] - X_k[i]) +
                                          (mic_fft[1][i] - X_k[i]) +
                                          (mic_fft[2][i] - X_k[i]) +
                                          (mic_fft[3][i] - X_k[i]))**2 / nr_mics ) )  # Std (noise)

            wk[i] = max(0.1, ((X_k[i] - (a * Xn_k[i])) / (X_k[i])) )              # Weight

            # based on function 5 in pdf: https://ieeexplore.ieee.org/document/1248813
            # we_k (weights with limits)
            if X_k[i] <= Xn_k[i]:
                we_k[i] = wk[i]
            elif X_k[i] > Xn_k[i]:
                we_k[i] = wk[i] * ( (X_k[i])/(Xn_k[i]) )**y

        return we_k, wk


    @property
    def samplerate(self):
        return self.Fs
