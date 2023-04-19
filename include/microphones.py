from grove.adc import ADC
from include.lpfilt import base_filter

class mic_read():
    def __init__(self, pin0: int, pin1: int):
        self.pin0 = pin0
        self.pin1 = pin1
        self.adc = ADC()
        self.filt = base_filter()

    def read_mic(self):
        mic0 = self.adc.read_raw(self.pin0)
        mic1 = self.adc.read_raw(self.pin1)
        mic0 = self.filt.filter_sample(mic0)
        mic1 = self.filt.filter_sample(mic1)
        return mic0, mic1

