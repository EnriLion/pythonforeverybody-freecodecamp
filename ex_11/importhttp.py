#An http request in python

import socket #the socket import the conection

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # we connect across the website(web server) in the port 80 (like a phone call)
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.1\n\n'.encode()# we encode the string through the network
mysock.send(cmd) # we send the cmd socket through the network

while True:#we create a loop 
    data = mysock.recv(512)#the characters that we receive in the file
    if (len(data) < 1):# if we get 0 characters 
        break
    print(data.decode())#we decode
mysock.close()#we close the socket

#technically this represents an entire web browser

