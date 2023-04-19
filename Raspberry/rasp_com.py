from include.UDP_class import UDP
from include.microphones import mic_read
import json

buffer_size = 1024
m1_buffer = [0]*buffer_size
m2_buffer = [0]*buffer_size
mic = mic_read(0, 2)

def fill_buff():
    global m1_buffer, m2_buffer
    for i in range(buffer_size):
        x_1, x_2 = mic.read_mic()
        m1_buffer.insert(0, x_1)
        m1_buffer.pop(-1)

        m2_buffer.insert(0, x_2)
        m2_buffer.pop(-1)

def send(msg: list):
    message = json.dumps({'mic 1': msg[0], 'mic 2': msg[1]})
    UDP.send_message(message)


if __name__ == '__main__':

    UDP = UDP(ip_adress="192.168.0.100", port=5004, receive_msg=False)
    while True:
        fill_buff()
        send_array = [m1_buffer, m2_buffer]
        send(send_array)



