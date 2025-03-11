Chat Application - Multi-Device Communication  

This is a chat application that allows multiple devices to communicate in real-time through a common server.  

How to Run 

Update the Client Configuration
- In chat_client.py, change the HOST IP to match your server machine’s IP.  
- Find your server’s IP
  -Windows: Open cmd and run: ipconfig
  -Linux:   Open terminal and run: ip addr show 

Start the Server 
- On the server machine,
     run: python chat_server.py
- On client machines
     run: python chat_client.py
  
-enjoy chatting

(You can run client and server on same machine and chat).
