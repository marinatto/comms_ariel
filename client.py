import socket 

UDP_IP = "127.0.0.0"
UDP_PORT = 7000 #port number

s = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

s.bind((UDP_IP, UDP_PORT))

while True:
    msg, addr = s.recvfrom(16) # buffer size = 16 bytes
    if len(msg) <=0:
        break
    print("received message: {} from adress: {}".format(msg, addr[1]))
