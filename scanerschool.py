# Importing sockets to be able to connect to the hosts and other functions #
# Importing sys and time for animation #
# date time for date and time (used for seeing how long the scan lasted) #
# itertools also used for animation # 
# the animation in the script might look weird or messed up in a normal python shell on windows but if u run it in Visual Studio Code or Pycharm it looks much more presentable #


import sys,time
from datetime import datetime
import socket
from time import sleep
import itertools


#loading animation
print("\033[1;35;40mLoading Script...")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]""\n ==========\n Loaded! <3"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

#printing name of port scanner along with my name

msg = "\033[1;35;40m\n\n      -*-------*-  \n  -*---------------*-\n|---------------------| \n|Seargent Port Scanner| \n*-                   -*\n|   By 0x2   |\n|---------------------|\n  -*---------------*-\n      -*-------*-"

#simple typewriter like animation to spice it up a bit
# Animation for each character, sys.stdout.write print the character then sys.stdout.flush displaying it and then time.sleep is making a timer for the intervals between each character#
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

#making input for ip address or host and then macking a variable for the socket.getbyhostname to resolve any domain to its ip

ipinput=input("\n\n{#} Please Enter Targeted IP Address or Hostname :  ")
hostbyname=socket.gethostbyname(ipinput)
portrange=input("\n{#} Please Enter Port range (must use in this syntax  eg:   1,100 or 1,2000")
done = 'false'
#Printing the target we are scanning to show user and adding ---- for visual aspect


print ("_" * 60)
print ("Please Wait scanning Remote Host", hostbyname)
print ("_" *60)

#checking date and time the script was started
t1 = datetime.now()

#using range function to specify the ports being scanned
#sock.connect to connect to target and connect on these particular ports
#making socket with AF_INET to tell it is a internet socket and not UNIX and SOCK_STREAM to tell it to scan TCP
#Animation for each character, sys.stdout.write print the character then sys.stdout.flush displaying it and then time.sleep is making a timer for the intervals between each character
#==0 is used to check whether the resault is equal to zero or not and will return answer is true or false by displaying the open ports
try:
    for port in range (portrange):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resault=sock.connect_ex((hostbyname, port))
        if resault==0:
            print (f"[#]Port {port} is : Open!!")
    sock.close()
#if control c or any keyboard interrupt is used on the script
except KeyboardInterrupt:
    print ("Ctrl + C Pressed")
    sys.exit()
#exiting if the hostname cannot be resolved
except socket.gaierror:
    print("Hostname cannot be resolved, Exiting")
    sys.exit()
#exiting if no connection towards host or ip 
except socket.error:
    print ("Could not connect to server!")
    sys.exit()


#checking tim again

t2=datetime.now()

#calculate distamce in time to see how long the scan took

total = t2 - t1

#printing time on screen
print(f"Time Scan took  --> :  {total}")





