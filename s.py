#!/usr/bin/env python3

import os
import time

# In the first stage, the user will be asked to input a string, if the string is 'hello' or 'hi'(case insensitive), 
# the program will respond with 'hi brochancho', otherwise it will respond with 'invalid input, skill issue'. 
# In the second stage, the program will ask the user for inputs, which will then be logged into a file called "log.txt" in a folder called "logs". 
# The program will continue to ask for inputs until the user types 'exit', at which point it will exit the logging function. 
# Each log entry will include a timestamp and the message that was logged. 


# This is a simple program that takes user input and responds accordingly.
userinput = input("Enter a string: ").lower()

if userinput == "hello":
    print("hi brochancho")
elif userinput == "hi":
    print("hi brochancho")
else:
    print("invalid input, skill issue")

# This is a program the logs data into a file called "log.txt". 

def log(msg): 
    folder = "logs"

    if not os.path.exists(folder):
        os.makedirs(folder)
    print("folder created, you didnt have one, noob, but now you do")

    filepath = os.path.join(folder, "log.txt")

    with open(filepath, "a") as f:
       f.write(time.strftime("%Y-%m-%d %H:%M:%S") + ", s.py: " + msg + "\n")

# the great logging begins

print("logging has begun")

while True:
    userinput = input("Enter a string to log, type 'exit' to exit this function").lower()
    if userinput == "exit":
        print("exiting")
        break

    log(userinput)
    print("logged: " + userinput)