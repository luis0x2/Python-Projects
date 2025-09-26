import socket
import sys,time 
import subprocess
from datetime import datetime 


#clearing terminal for cleaner look
subprocess.call('cls', shell=True)

#fancy msg
intro="\033[1;35;40m  |-----------------------------|\n\
  |   Sergeant Port Scanner!    |\n\
  |           by 0x2            |\n\
  |-----------------------------|\n\
           ------------          \n\
            ----------           \n\
             --------            "


# Animation for each character, sys.stdout.write print the character then sys.stdout.flush displaying it and then time.sleep is making a timer for the intervals between each character#

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

typewriter(intro)






#creating variables for the input and resolving websites domains

ipinput = input("\n{#} Enter IP Address or Host to Scan :    ")
hostbyname = socket.gethostbyname(ipinput)

#Printing information on the host that we are about to start scanning


