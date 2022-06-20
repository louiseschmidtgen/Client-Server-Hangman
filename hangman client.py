# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 03:08:38 2020

@author: louis
"""
import socket

serverPort = 4000
#creates the socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""establish connection"""
clientSocket.connect(('10.1.46.234', serverPort))
print("I want to play")
clientSocket.send("Hello, I want to play\n".encode())

while True:
    """now playing the game"""
    message_server = (clientSocket.recv(1024)).decode() #asks for move
    print(message_server)
    #if message play
    if "D" == message_server[0]:    
        play = input() + "\n" #enter guess char
        clientSocket.send(play.encode()) 
        print("Playing: ", play)
    #if message is you lost
    elif "Y" == message_server[0]:
        print("Ending game")
        boolean = False
        break 
    #message ran out of guesses
    else:    
        print("Ending game because you ran out of guesses.")
        boolean = False
        break 
    
clientSocket.close()