import socket # Import socket module
import os
import time

#python time init

from functools import wraps
p_start_time = time.time()
print("--- %s seconds ---" % (time.time() - p_start_time))


print '########################You are Client streaming#################'
ip=raw_input('Enter server ip address:')
port = input('Enter server port no.:')
file = raw_input('Enter file to stream with extenstion.:')

file_size=os.path.getsize(file)
file_size = file_size/1024
print 'File size',file_size,'KB'

print 'File size',file_size/1024,'MB'
s = socket.socket()         # Create a socket object
host = ip # Get local machine name
port = port              # Reserve a port for your service.

s.connect((host, port))

s.send(str(file_size))
f = open(file,'rb')
print s.recv(100240)
stream=raw_input('Press! Enter to STREAM:')
start_time = time.time()
print 'Streaming...',file
l = f.read(100240)
while (l):
    
    print 'Sending...'
    s.send(l)
    l = f.read(100240)
f.close()
print "Done Sending"
s.shutdown(socket.SHUT_WR)
print s.recv(100240)
#s.send('ok')

s.close                     # Close the socket when done
elapsed_time = time.time() - start_time
#print("--- %s seconds ---" % (time.time() - elapsed_time))
print elapsed_time
