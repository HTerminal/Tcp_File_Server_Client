import socket               # Import socket module
import os
import time
file_size=0;
check = 460;
elapsed_time = 0;
p_start_time = time.time()
print("--- %s seconds ---" % (time.time() - p_start_time))
print '########################You are server receiving#################'
ip=raw_input('Enter your ip address:')
port = input('Enter your port no.:')
file_name = raw_input('Enter the file name you are reciveing with .extention:')

s = socket.socket()         # Create a socket object
host = ip                   # Get local machine name
port = port                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open(file_name,'w+b')
s.listen(5)                 # Now wait for client connection.
print 'Listining----'
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    
    size_file=c.recv(8024)
    #hold=raw_input('Enter to send server connected msg');
    c.send('server connected!')
    
    
    print 'Incoming stream size',size_file,'KB'
    
    
    print "Streaming..."
    start_time = time.time()
    l = c.recv(8024)
    while (l):
        print "Receiving..."
        
        f.write(l)
        if file_size == 460:  #if you want to get exit then enable it
            print 'Closing'
            s.close()
            c.close()
            
    
        l = c.recv(8024)
        #if int(elapsed_time) == 5:
        #    os.system("on.bat");
        file_size=os.path.getsize(file_name)
        file_size = file_size/1024
        
        print file_size,'KB','/',size_file,'KB'
        elapsed_time = time.time() - start_time
        print elapsed_time
        
        
    f.close()
    
c.close()
    
        
    


