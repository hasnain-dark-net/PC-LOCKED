import socket

WINDOWS_IP = "192.168.1.102"
PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((WINDOWS_IP, PORT))
sock.send(b"LOCK")
sock.close()

print("Windows Locked!")
