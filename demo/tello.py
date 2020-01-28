import socket
import time

ip = "drone-001.h-farm.com"
port = 8889

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "command"

sock.sendto(message.encode('utf-8'), (ip, port))

time.sleep(2)


takeoff = "takeoff"

sock.sendto(takeoff.encode('utf-8'), (ip, port))

time.sleep(4)

land = "land"

sock.sendto(land.encode('utf-8'), (ip, port))
