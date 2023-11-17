import time
import socket
import sys
import os

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and port to bind the server
host = socket.gethostname()
port = 8080

# Bind the socket
s.bind((host, port))

# Listen for incoming connections
s.listen(1)
print("Waiting for incoming connection...")

# Accept a connection from a client
conn, addr = s.accept()
print(addr, "is connected to the server")

# Receive a command from the client
command = conn.recv(1024).decode()
print("Received command:", command)

# Execute the command (for demonstration, we'll just run a simple command)
if command == "whoami":
    result = os.popen("whoami").read()
else:
    result = "Invalid command"

# Send the result back to the client
conn.send(result.encode())
print("Result sent successfully")

# Close the connection
conn.close()
