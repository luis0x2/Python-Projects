#Import subprocess so we can use system commands.
import subprocess
#Import the re module so we can make use of regular expressions. 
import re
#Import art to make it pretty <3
interface=input(" Enter Network Interface :  ")
#Python allows us to run system commands using the functions provided by the subprocess module
#specify that we want to capture the output, ro do this we specify the second argument as capture_output = True.
#this information gets stored in the stdout attribute as bytes and needs to be decoded before being used as a string in Python.
command_output = subprocess.run(["netsh", interface, "show", "profiles"], capture_output = True).stdout.decode()
#find all the wifi names which are listed after 
#"ALL User Profile     :". Using regular expressions we can create 
#a group of all characters until the (\r) appears  (return escape sequence)
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
#create a list were all the wifii usernames and passwords will be saved
wifi_list = []

#If any profile names are not found this means that wifi connections have also not been found
#So we run this part to check the details of the wifi and see whether we can get their passwords.

if len(profile_names) != 0:
    for name in profile_names:

        #Every wifi connection will need its own dictionary which will be appended to the variable wifi_list. 
        
        wifi_profile = {}
        #We can now run the command to see the information 
        
        profile_info = subprocess.run(["netsh", interface, "show", "profile", name], capture_output = True).stdout.decode()
        #We use the regular expression to only look for the absent ones so we can ignore them.
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            #Assign the ssid of the wifi profile to the dictionary.
            wifi_profile["ssid"] = name
            #"key=clear" command part to get the password.
            profile_info_pass = subprocess.run(["netsh", interface, "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            #Again run the regular expression to capture the group after the :  (AKA Passwords)
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            #Check if we found a password using the regular expression. 
            #if the wifi connections dont have passwords state none.
            if password == None:
                wifi_profile["password"] = None
            else:
                #We assign the grouping (where the password is contained) that 
                #we are interested in to the password key in the dictionary.
                wifi_profile["password"] = password[1]
            #We append the wifi information to the variable wifi_list.
            wifi_list.append(wifi_profile) 

for x in range(len(wifi_list)):
    print(wifi_list[x]) 

print("Cheers for the passwords! <3")