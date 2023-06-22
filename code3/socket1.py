import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))# works with the telnet
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()#there are strings inside of Python that are Unicode(UTF-8)
mysock.send(cmd) #with the socker while using a method we send the direction

while True:# 
    data = mysock.recv(512)#create a variable with recieve of 512 characters
    if len(data) < 1: #if this is the end of the file we are going to stop with a break
        break
    print(data.decode())# Converts into the unicode that runs inside

mysock.close() #open a socket and retrieve the data
