#importing scapy to use arp scans and such and you can get scapy by using the command in terminal  "pip3 install scapy"
#importing sys and time for animations and also importing sleep
#importing date time to wllow me to show how long the scan has taken and to display it to the user

from scapy.all import ARP, Ether, srp
import sys,time
from datetime import datetime
from time import sleep

#making a variable for the msg that the animation is going to use to dislay the name of the tool and who created it

msg = "\033[1;35;40m\n\n      -*-------*-  \n  -*---------------*-\n|---------------------| \n|Seargent Port Scanner| \n*-                   -*\n|   By 0x2   |\n|---------------------|\n  -*---------------*-\n      -*-------*-"

#simple typewriter like animation to spice it up a bit
#Animation for each character, sys.stdout.write print the character then sys.stdout.flush displaying it and then time.sleep is making a timer for the intervals between each character#
for char in msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

#ip address for the destination aswell as creating the ARP packet
#pdst is where the arp packet should go so that why we tell it it is the target_ip
target_ip=input("\n\n[#] Input Targeted IP Address along with Subnet eg: --192.168.0.1/24--  ---> :  ")
arp= ARP(pdst=target_ip)
# printing the target we are scanning aswell as some -- for visual appeal

print("_" * 60)
print("Please wait while we scan the Host", target_ip)
print("_" * 60)

# chekcing the time the the script was started
t1 = datetime.now()
#creating the Ether broadcast packet
#FF:FF:FF:FF:FF:FF MAC addres indicates that it is broadcasting
#dst means the destination mac address
ether= Ether(dst="ff:ff:ff:ff:ff:ff")
#stacking them together
packet=ether/arp
#mkaing variable for created packet and now sending them using srp() function, which sends and recieves packets at layer 2 of the OSI model and setting the timeout to 3 so the script will not get stuck
resault = srp(packet, timeout=3, verbose=0)[0]

#now we will need a list for all the clients, we will fll this into the loop
clients=[]

for sent, recieved in resault:
    # for each response, append ip and mac address to 'clients; list
    # psrc is the IP to update in the targets arp table, hwsrc is the MAC corresponding to psrc, to update in the targets arp table.
    clients.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})
#printing the client to the screen
print("[#] These are the Available Devices on the Network :  ")
print("ip" + " "*18+"mac")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))

# check time again and make variable as t2 for second time or (end time)
t2=datetime.now()
#calculate distance in time so we can see how long the scann took
total=t2-t1
#printing resault to screen
print(f"[#] Scan took ^,{total}")



















