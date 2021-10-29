# Networking Tic-Tac-Toe

This is my **Networking Tic-Tac-Toe** software. I decided to make this game to learn about and show what I can do from learning about networking and sockets in Python. 

This game has a server and client file. The server is started first and only on one machine, and is what gives the clients their starting information, and connects and allows them to send messages to each other. The first person who starts the client will be given a waiting message, and then the second person that joins will be shown the board and prompted for a spot to go. This spot is sent over the server to the other client, and both client's boards are updated. This continues until someone wins, or until there is a tie, in which case the clients are disconnected from the server.

To play, one person has to start the server by typing: **py server.py**, and then both people enter the IP provided when the server starts in the client file next to the word ***SERVER***. To start the client, both people type: **py client.py** (or client_colors.py if you are in a terminal that supports colored characters).

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This program uses a client/server connection, where multiple clients can connect to one server. At the moment, only 2 clients may connect to the server at a time, but this can be increased as the server uses threading and can therefore handle many clients and their requests.

This program uses a TCP based server to communicate between server and clients. The default port being used is 5050, but this can be changed.

Messages are encoded using UTF-8, which is a Unicode character encoding method. When they are received by the opposite client, they are decoded and used by that client to update the board.

# Development Environment

Some tools that I used to make this program are:

* Python
* Visual Studio Code
* Python sockets library
* Python threading library

# Useful Websites

* [Sockets Tutorial Video](http://www.youtube.com/watch?v=3QiPPX-KeSc)
* [ZetCode Python Sockets](http://zetcode.com/python/socket/)
* [Stack Overflow](http://stackoverflow.com/questions/21217313/sending-strings-to-and-fro-server-client-python)
* [HowtoGeek "What's the Difference Between TCP and UDP?"](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)

# Future Work

* Modify the server to accept more than 2 clients, pair up 2 clients out of the many, and start a game for each pair
* Use the client/server model on a different and more complex game
* Learn about and use UDP as opposed to TCP