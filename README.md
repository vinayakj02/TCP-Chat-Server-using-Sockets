# TCP Chat server using Sockets
A chatroom implemented using TCP Sockets in Python.

## Feautures 
* Clients (users) can join and leave the server (chat room).
* Clients can only join the server if the server authorizes it.
* Clients can send private messages to other clients (users) in the server (chat room).
* **Commands**
  * ``/private <person_name> <text>`` only the client with person_name will be able to view the message. 
  * ``/leave`` will let the client (user) exit from the server.
  * ``/color <color> <text>`` makes the text appear in that color.
  * ``**text**`` will make <b>text</b> bold.
  * ``__text__`` will make the <i>text</i> italicised.


## To run
* Run ``server.py`` to start the chat room.
* Run ``client.py`` to start each client.
