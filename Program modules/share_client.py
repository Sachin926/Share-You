import socket

s = socket.socket()
s.connect(("192.168.43.98", 9999),)

size = s.recv(1024)
name = s.recv(1024)
name = name.decode('utf-8')

data = s.recv(int(size.decode('utf-8')))
print (name)
name = name[name.rindex('/') + 1 : ]
file = open(name, "wb")
file.write(data)
file.close()
print ("file received...")
s.close()