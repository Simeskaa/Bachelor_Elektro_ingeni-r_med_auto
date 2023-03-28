import math
import time
from grove.adc import ADC

def main():
    from grove.helper import SlotHelper
    pin0 = 2
    pin1 = 6

    adc = ADC()

    while True:
        mic0 = adc.read_voltage(pin0)
        mic1 = adc.read_voltage(pin1)
        print(f'Sound from channel 2: {mic0} ==== Sound from channel 6: {mic1}')
        time.sleep(.1)


if __name__ == '__main__':
    main()
