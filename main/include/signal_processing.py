import numpy as np
from numpy import cos, pi
import scipy.signal as sig

class processing():
    def __init__(self, samplerate: int = 44100):
        self.samplerate = samplerate

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
        frequency = peak_location/L*self.samplerate

        return frequency

    # Finite Iteration Filter
    # Simple filter that reduces unwanted frequencies
    def FIR_filter(self, xn, desired_hz: int = 140):
        width = 50
        L = self.samplerate//width
        w_bp = desired_hz/self.samplerate*2*pi

        hn_bp = cos(w_bp*np.arange(L))*2*sig.hamming(L)
        y = sig.convolve(xn, hn_bp)
        return y

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
        time_delay = round((np.argmax(r_12)/self.samplerate)*10**3, 2)  # present the result in milliseconds (ms)
        distance = np.argmax(r_12)/self.samplerate*343  # 343m/s is the speed of sound
        return time_delay, distance

    @property
    def samplerate(self):
        return self.samplerate
