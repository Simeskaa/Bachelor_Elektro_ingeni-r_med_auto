import socket
import json
import struct
import sys


class UDP:
    def __init__(self, ip_adress: str, port: int, receive_msg: bool):
        # declaring it is a UDP and defining server address
        self.server_address = (ip_adress, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"Serving connections on port {self.server_address[1]}")
        if receive_msg:
            self.sock.bind(self.server_address)

    def send_message(self, server_msg):
        self.sock.sendto(server_msg.encode(), self.server_address)

    def get_message(self, buf_size):
        data, addr = self.sock.recvfrom(buf_size) #Have to configure the spacing between the ints.
        return data


if __name__ == "__main__":
    get = True
    if get:
        UDP = UDP(ip_adress="192.168.1.50", port=5001, receive_msg=True)
        while True:
            data = UDP.get_message(65536)
            a0 = []
            a1 = []
            a2 = []
            a3 = []
            if data is not None:
                for i in range(0, len(data), 2):
                    b1 = data[i].to_bytes(1, "little")
                    b2 = data[i+1].to_bytes(1, "little")
                    #b2 = struct.unpack("b", bytearray(data[0]))
                    if (i % 8) == 0:
                        a0.append(int.from_bytes(b1 + b2, byteorder='little'))
                    elif (i % 8) == 2:
                        a1.append(int.from_bytes(b1 + b2, byteorder='little'))
                    elif (i % 8) == 4:
                        a2.append(int.from_bytes(b1 + b2, byteorder='little'))
                    elif (i % 8) == 6:
                        a3.append(int.from_bytes(b1 + b2, byteorder='little'))
            print(a0)


    if not get:
        UDP = UDP(ip_adress="192.168.1.50", port=5001, receive_msg=False)
        n = 0
        msg = [[0, 1, 2, 3], [3, 2, 1, 0]]
        while True:
            # print(UDP.get_message(4096))
            message = json.dumps({'mic 1': msg[n]})
            UDP.send_message(message)
            n += 1
            n %= 2
            print(message)