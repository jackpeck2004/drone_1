#!/usr/bin/env python3.7

import socket
import keys
import time

message = "command"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.sendto(message.encode('utf-8'), (keys.UDP_IP, keys.UDP_PORT))

time.sleep(2)

message = "takeoff"

sock.sendto(message.encode('utf-8'), (keys.UDP_IP, keys.UDP_PORT))

