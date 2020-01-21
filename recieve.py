#!/usr/bin/env python3.7

import socket
import keys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((keys.UDP_IP, keys.UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print(data)

