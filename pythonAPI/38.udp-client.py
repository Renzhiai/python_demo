import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['Xiaoming','Xiaohong','Xiaohua']:
    s.sendto(data.encode(),('127.0.0.1',9999))
    print(s.recv(1024).decode())
s.close()