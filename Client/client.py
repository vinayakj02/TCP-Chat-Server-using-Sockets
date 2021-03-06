import socket
import threading
import style 
name = input("Enter your name : ").strip()
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55_555))

def keepListening():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'Send_name':
                client.send(f'{name}'.encode('utf-8'))
            elif '/private' in message:
                x = message.split()
                recv_person = x[3]
                text = x[4:]
                text = style.color(text)
                text = style.bold(text)
                text = style.italics(text)
                if recv_person==name:
                    print(f'{recv_person} : {" ".join(text)} (private)')
            else : 
                print(message)
        except:
            print("Error in client.py")
            client.close()
            break  
def sendMessage():
    while True:
        inp = input().strip()
        if "/leave" in inp:
            client.send(f"{name} left the chat room".encode('utf-8'))
            client.close()
            break
        
        inp = style.color(inp)
        inp = style.bold(inp)
        inp = style.italics(inp)
        client.send(f"{style.BOLD}{name}{style.END} : {inp}".encode('utf-8'))
        # client.send(f'{name} : {inp}'.encode('utf-8'))

toKeepListening = threading.Thread(target=keepListening)
toSendMessage = threading.Thread(target=sendMessage)

toKeepListening.start()
toSendMessage.start()


        
