import socket
import json


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
        data, addr = self.sock.recvfrom(buf_size)
        data = data.decode('utf-8')
        return data


if __name__ == "__main__":
    get = True
    if get:
        UDP = UDP(ip_adress="localhost", port=5004, receive_msg=True)
        while True:
            msg = UDP.get_message(4096)
            message = json.loads(msg)
            print(message['mic 1'])

    if not get:
        UDP = UDP(ip_adress="192.168.0.101", port=5004, receive_msg=False)
        n = 0
        msg = [[0, 1, 2, 3], [3, 2, 1, 0]]
        while True:
            # print(UDP.get_message(4096))
            message = json.dumps({'mic 1': msg[n]})
            UDP.send_message(message)
            n += 1
            n %= 2
            print(message)
