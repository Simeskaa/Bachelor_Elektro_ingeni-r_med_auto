from grove.adc import ADC

class mic_read():
    def __init__(self, pin0: int, pin1: int):
        self.pin0 = pin0
        self.pin1 = pin1
        self.adc = ADC()

    def read_mic(self):
        mic0 = self.adc.read_raw(self.pin0)/0x1000
        mic1 = self.adc.read_raw(self.pin1)/0x1000
        return mic0, mic1

