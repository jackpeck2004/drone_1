#!/usr/bin/env python3

from flask import Flask, render_template, url_for
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
        # sock.bind((keys.UDP_IP, keys.UDP_PORT))
        # message = "command"
        # sock.sendto(message.encode('utf-8'), (keys.UDP_IP, keys.UDP_PORT))
        # time.sleep(2)

    def send_command(self, command):
        sock.sendto(command.encode('utf-8'), (self.ip, self.port))


tello = Tello(keys.UDP_IP, keys.UDP_PORT)

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command/<command>')
def send_command(command=None):
    tello.send_command(command)
    return "done"

