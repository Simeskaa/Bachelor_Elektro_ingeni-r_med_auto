import math
import time
from grove.adc import ADC

def main():
    from grove.helper import SlotHelper
    pin0 = 2
    pin1 = 6

    adc = ADC()

    numOfSamples = 1000
    recorded_sound = ([0]*numOfSamples, [0]*numOfSamples)
    for i in range(numOfSamples):
        mic0 = adc.read_raw(pin0)
        mic1 = adc.read_raw(pin1)
        recorded_sound[0][i] = mic0
        recorded_sound[1][i] = mic1
        print(f'Sound from channel 2: {mic0} ==== Sound from channel 6: {mic1}')
        time.sleep(0.01)

    f = open('soundArray.txt', 'w')
    f.write(str(recorded_sound))

    f.close()
    # f = open('soundArray.txt', 'r')
    # print(f.read())

if __name__ == '__main__':
    main()
