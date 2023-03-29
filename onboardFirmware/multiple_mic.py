import math
import time
from grove.adc import ADC

def main():
    from grove.helper import SlotHelper
    pin0 = 0
    pin1 = 2

    adc = ADC()

    while True:
        # Sampled like this the delay between a sample from the mics are about 1370312 ns.
        mic0 = adc.read_voltage(pin0)
        t0 = time.time_ns()
        mic1 = adc.read_voltage(pin1)
        t1 = time.time_ns()
        print(f'Sound from channel 0: {mic0} ==== Sound from channel 2: {mic1}')
        #print(f'Time delay between mic readings: {t1 - t0}')
        #time.sleep(.1)


if __name__ == '__main__':
    main()
