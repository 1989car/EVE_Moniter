'''
Created on 2012-8-27

@author: Administrator
'''
import socket

host = "211.144.214.68"
port = 26000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( (host,port))

print s.recv(1024) 

s.close()