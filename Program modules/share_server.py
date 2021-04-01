import socket
import os

size = os.path.getsize(r"C:\Users\indu\Desktop\announ.exe")		#get the size of the file
file_format = "pdf"
s = socket.socket()
s.bind(("", 9999),)		#bind the ip and the port address to give unique address
s.listen(3)		#set the maximum queue for the clients to connect
print ("listening...")
c, add = s.accept()		#accept the connections form the client
print (f"{add} has connected")

c.send(bytes(str(size), 'utf-8'))		#send the size of the file in encoded format
c.send(bytes(file_format, 'utf-8'))

file = open(r"C:\Users\indu\Desktop\KNIT\5th _sem\CAO\CF_cards.pdf", "rb")		#open the file in read binary mode
data = file.read()
c.send(data)		#send whole file
print ("The file has been sent")
c.close()		#close the client
s.close()		#close the socket