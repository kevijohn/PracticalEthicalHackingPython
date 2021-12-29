# Author: Kevin Johnson
# Created: DEC 29 2021

import socket

#HOST = '127.0.0.1'
HOST = '192.168.239.128'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

