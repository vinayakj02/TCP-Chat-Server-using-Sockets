import socket 
import threading

host = '127.0.0.1'
port = 55_555

clients = {}  ## clientObject : clientName
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server.bind((host,port))
server.listen()


def brodcast(message,expt_client=None):
    if expt_client is not None:
        for client,name in clients.items():
            if client!=expt_client:
                client.send(message.encode('utf-8'))
        return 
    for client,name in clients.items():
        client.send(message.encode('utf-8'))


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            brodcast(message,expt_client=client)
        except:
            client.close()
            brodcast(f'{clients[client]} left the chat'.encode('utf=8'))
            clients.pop(client)
            break


def keepListening():
    while True:
        client, address = server.accept()
        client.send('Send_name'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        perms = input(f"{name} wants to join the server\nAuthorize [y/n] : ").strip()
        y_p = ['y','Yes','yes','YES']
        if perms not in y_p:
            client.send("You were denied access to the chat room by the admin".encode('utf-8'))
            client.close()
            continue

        print(f"{name} joined the server")

        clients[client] = name 
        
        brodcast(f"{name} joined the server !",expt_client=None)
        client.send("Connected to server".encode('utf-8'))

        handling_client = threading.Thread(target=handle,args=(client,))
        handling_client.start()



print("Server is up and listening !!")
keepListening()

