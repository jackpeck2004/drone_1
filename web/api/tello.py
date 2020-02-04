#!/usr/bin/env python3.8

import socket
import keys
import time

class Tello:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        global sock
        global receive_sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((keys.UDP_IP, keys.UDP_PORT))
        message = "command"
        sock.sendto(message.encode('utf-8'), (keys.UDP_IP, keys.UDP_PORT))
        time.sleep(2)

    def send_command(self, command):
        sock.sendto(command.encode('utf-8'), (self.ip, self.port))


tello = Tello(keys.UDP_IP, keys.UDP_PORT)

# while True:
    # command = input("> ")
    # tello.send_command(command)
    # time.sleep(2)

# while True:
    # data, addr = sock.recvform(1024)
    # print(data)


