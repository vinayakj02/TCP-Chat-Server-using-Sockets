# TCP Chat server using Sockets
A chatroom implemented using TCP Sockets in Python.

## Feautures 
* Clients (users) can join and leave the server (chat room)
* Clients can only join the server if the server authorizes it 
* **Commands**
  * ``/leave`` will let the client exit from the server
  * ``/color <color> <text>`` makes the text appear in that color
  * ``**text**`` will make <b>text</b> bold
  * ``__text__`` will make the <i>text</i> italicised


## To run
* Run ``server.py`` to start the chat room.
* Run ``client.py`` to start each client.
