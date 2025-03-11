import socket
import threading

HOST = ""  # Your server's IP address

PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(message)
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    msg = input()
    client.send(msg.encode())
