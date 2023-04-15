from include.direction_and_distance_estimation import angle_cord_estimation as ace
from include.lpfilt import base_filter
from include.microphones import mic_read
from include.signal_processing import processing


buffer_size = 4096
m1_buffer = [0]*buffer_size
m2_buffer = [0]*buffer_size
mic = mic_read(0, 2)

#  Read data until the buffer is full
def fill_buff():
    global m1_buffer, m2_buffer
    for i in range(buffer_size):
        x_1, x_2 = mic.read_mic()
        m1_buffer.insert(0, x_1)
        m1_buffer.pop(-1)

        m2_buffer.insert(0, x_2)
        m2_buffer.pop(-1)

def main():
    fill_buff()

if __name__ == "__main__":
    main()



