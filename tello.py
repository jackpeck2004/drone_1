#!/usr/bin/env python3.7

import socket
import keys
import time

class Tello:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AD_INET, socket.SOCK_DGRAM)
        message = "command"
        sock.sendto(message.encode('utf-8'), (keys.UDP_IP, keys.UDP_PORT))

        time.sleep(2)


    def send_command(self, command):
        self.socket.sendto(command.encode('utf-8'), (self.ip, self.port))


# message = "command"
# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.sendto(message.encode('utf-8'), (keys.UDP_IP, keys.UDP_PORT))
# time.sleep(2)

tello = Tello(keys.UDP_IP, keys.UDP_PORT)
tello.send_command("takeoff")

