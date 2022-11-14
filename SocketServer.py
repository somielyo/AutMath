#Imports Modules
import socket
import RPi.GPIO as GPIO
import time
from pydub import AudioSegment
from pydub.playback import play

#Defines Server Values
listensocket = socket.socket()
Port = 8000
maxConnections = 999
IP = socket.gethostname() #Gets Hostname Of Current Macheine

listensocket.bind(('',Port))

#Opens Server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts Incomming Connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")

running = True

#Sets Up Indicator LED

#Main
while running:
    message = clientsocket.recv(1024).decode() #Receives Message
    print(message) #Prints Message
    #Turns On LED
    if not message == "":
        song = AudioSegment.from_wav("exercice.wav")
        play(song)
        exec(open("./micro.py").read())

    #Closes Server If Message Is Nothing (Client Terminated)
    else:
        clientsocket.close()
        running = False