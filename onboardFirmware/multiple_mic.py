import math
import time
from grove.adc import ADC
from lpfilt import filter_sample

def main():
    from grove.helper import SlotHelper
    pin0 = 0
    pin1 = 2

    adc = ADC()

    while True:
        # Sampled like this the delay between a sample from the mics are about 1370312 ns.
        mic0 = adc.read_raw(pin0)
        mic0 = filter_sample(mic0)

        mic1 = adc.read_raw(pin1)
        mic1 = filter_sample(mic1)
        print(f'Sound from channel 0: {mic0} ==== Sound from channel 2: {mic1}')

        time.sleep(0.01)


if __name__ == '__main__':
    main()

