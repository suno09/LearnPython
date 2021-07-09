import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 32009))
s.listen()
c, addr = s.accept()
y = c.recv(1024).decode('utf-8')
