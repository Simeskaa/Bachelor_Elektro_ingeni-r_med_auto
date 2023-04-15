from include.Geometrisk_retnig_og_avstands_estimering import angle_cord_estimation as ace
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
    print(m1_buffer)

    fill_buff()

    print(m1_buffer)

if __name__ == "__main__":
    main()



