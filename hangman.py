# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:57:13 2020

@author: louise
"""
import random
import socket
def main():
    word = random_word()
    #print("The word is: ", word)
    
    guess = ["_" for char in word]
    used_char = ""
    
    number_of_guesses = 11    
    
    """establish connection"""
    
    server_port = 4000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.1.46.234', server_port))
    server_socket.listen(1)
    print("Server ready to recieve")
    
    """connecting with client"""
    
    connection, client_address = server_socket.accept()
    print(connection.recv(1024).decode()) #prints hello i want to play
    
    while (number_of_guesses >0):
        to_message = "Display: "+list_to_str(guess)+"\nPlease enter your guess, you currently have " +str(number_of_guesses)+" left. \nYou already used the characters: "+used_char +"\nEnter here: "
        connection.send(to_message.encode()) #encodes message
        client_char = connection.recv(1024).decode().strip()
        used_char +=client_char
        guess, right_guess = guess_char(word, guess, client_char)
        #print(guess)
        if won(word, guess):
            print("Client guessed the word")
            connection.send(("You guessed the word! It's : "+word).encode())
            connection.close()
            server_socket.close()
            break
        if right_guess ==0:  
            print("incorrect guess")
            number_of_guesses -=1
    
    print("Ending game")
    #check if client ran out of guesses
    if (number_of_guesses == 0):
        to_message = "You lost, you don't have any guesses left. The word was: "+word
        connection.send(to_message.encode())
        connection.close()
        server_socket.close()   
      
def list_to_str(guess):
    string = ""
    for char in guess:
        string = string+ char +" "
    return string        
    
def guess_char(word, guess, char):
    right_guess = 0
    for x in range(0, len(word)):        
        if word[x] == char:
            guess[x] = char
            right_guess =1
            
    return guess, right_guess

def won(word, guess):
    if list(word) == guess:
        return True
    else:
        return False
       

def random_word():
    #open file
    file = open("hangman words.txt", "r")
    try:
        lines = file.readlines()
    except: (FileNotFoundError)
    file.close()
    #generate random number
    rand_int = random.randint(0,854)
    #generate random word
    word = lines[rand_int].strip()
    return word
      
main()

