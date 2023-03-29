import math
import time
from grove.adc import ADC


def recordSterio(num_of_samples):
    recorded_sound = ([0] * num_of_samples, [0] * num_of_samples)
    for i in range(num_of_samples):
        mic0 = adc.read_raw(pin0)
        mic1 = adc.read_raw(pin1)
        recorded_sound[0][i] = mic0
        recorded_sound[1][i] = mic1
        print(f'Sound from channel 2: {mic0} ==== Sound from channel 6: {mic1}')
        # time.sleep(0.01)
    return recorded_sound

def recordMono(num_of_samples):
    recorded_sound = [0] * num_of_samples
    for i in range(num_of_samples):
        mic0 = adc.read_raw(pin0)
        recorded_sound[i] = mic0
        print(f'Sound from channel 0: {mic0}')
        # time.sleep(0.01)
    return recorded_sound


def main():
    from grove.helper import SlotHelper
    numOfSamples = 7000

    data = recordMono(numOfSamples)

    f = open('soundArray.txt', 'w')
    f.write(str(data))

    f.close()
    # f = open('soundArray.txt', 'r')
    # print(f.read())


if __name__ == '__main__':
    adc = ADC()
    pin0 = 0
    pin1 = 2

    main()
