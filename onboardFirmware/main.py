import numpy as np
import time
from grove.adc import ADC
from lpfilt import filter_sample


class live_mic:
    def __init__(self, pin0, pin1):
        self.pin0 = pin0
        self.pin1 = pin1
        self.data = np.array([])

        self.adc = ADC()

    def get_sample(self):
        mic0 = self.adc.read_raw(self.pin0)
        mic1 = self.adc.read_raw(self.pin1)
        self.update_array(mic0, mic1)

    def update_array(self, mic0, mic1):
        self.data = np.append(self.data, mic0)
        print(f'After append:: {len(self.data)}')
        #self.data[1] = np.append(self.data[1], mic1)
        if len(self.data) > 5:
            self.data = np.delete(self.data, 0)
            print(f'After delete: {len(self.data)}')
            #self.data[1] = np.delete(self.data[1], len(self.data[1]))

    def return_data(self):
        return self.data


def main():
    live = live_mic(0, 2)

    while True:
        live.get_sample()
        datA = live.return_data()
        print(f'newest data: {datA} ====== Length of lists: {len(datA)} \n')


if __name__ == '__main__':
    main()
