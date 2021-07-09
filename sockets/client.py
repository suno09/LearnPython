import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 32009))
s.connect()
y = c.recv(1024).decode('utf-8')
