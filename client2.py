import socket

host = '127.0.0.1'  # Standard loopback interface address 

port = 65432        # Port to listen on (non-privileged ports are > 1023)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))



from_server = client.recv(4096)
print (from_server)
client.send(b"I am client 2 :  ")
client.send(b"what is going on here")