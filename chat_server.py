import socket
import threading

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5000

clients = []

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    clients.append(client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"[{address}] {message}")
            for client in clients:
                if client != client_socket:
                    client.send(f"[{address}] {message}".encode())
        except:
            break
    
    print(f"[-] Connection closed: {address}")
    clients.remove(client_socket)
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[*] Chat server started on {HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    threading.Thread(target=handle_client, args=(client_socket, addr)).start()
