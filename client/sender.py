import socket
import time

# Replace with the IP address of the receiver
receiver_ip = '192.168.56.1'
receiver_port = 5000

# Create a socket object
s = socket.socket()

# Connect to the receiver
s.connect((receiver_ip, receiver_port))

while True:
    x=input("Enter your order")
    s.send(x.encode())
# Close the socket
s.close()
