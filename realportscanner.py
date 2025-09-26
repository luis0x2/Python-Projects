# import Queue so whatever elements are retreived from the list its no longer available in the list so that we dont go over the same ports #
# python threading is basically simulated multi-threading and can mess up and go over the same ports thats why were using Queue module to make sure it doesnt happen #
# Importing sockets to be able to connect to the hosts and other functions #
# Importing sys and time for animation #
import queue
import socket
import threading
from queue import Queue
import sys,time
message="  |-----------------------------|\n\
  |     Welcome to  Red24       |\n\
  |   Sergeant Port Scanner!    |\n\
  |          by 0x2             |\n\
  |-----------------------------|\n\
           ------------          \n\
            ----------           \n\
             --------            "

# Animation for each character, sys.stdout.write print the character then sys.stdout.flush displaying it and then time.sleep is making a timer for the intervals between each character#

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

typewriter(message)
target = input("\n[#] Please Enter IP Address! :  ")
# empty queue ready to be filled from port_list #
# open ports variale waiting to be filled #
queue = Queue()
open_ports = []

# defineing portscan and making socket with AF_INET to tell it is a internet socket and not UNIX and SOCK_STREAM to tell it to scan TCP #
# sock.connect to connect to target and connect on these particular ports #
# return true if port open and any exceptions return false #
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
# getting the port_list and filling it into the queue #
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)
# worker is the function/method that the threads will be using #
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("[#] Port {} is Open bruvaaa!".format(port))
            open_ports.append(port)
        
# telling it the range for the port list and to fill the queue with the port list #
port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

for t in range(200):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
# start thread_list #
for thread in thread_list:
    thread.start()

# the thread.join is important as it waits untill al the threads are done to display the message of open ports #
for thread in thread_list:
    thread.join()

print("[#] Open Ports are : ", open_ports)