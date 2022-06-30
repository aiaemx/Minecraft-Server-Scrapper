from threading import Thread
import random
import time
import requests
from mcstatus import JavaServer

print("This script works best while connected to a vpn because ISPs block residential ips from spamming people or something. :/")
time.sleep(1)
print("Starting in 5 seconds")
time.sleep(4)
# Post webhook here
url = ""
if len(url) < 5:
    print("You haven't put in a webhook, so it's going to run locally.")
    time.sleep(2)

logo = """
Minecraft Server Scrapper
"""
print(logo)
time.sleep(1)
number_of_threads = "50000"

def task():
    name = "worker" + str(random.randint(0,99))
    while True:
        ip = (str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + ":25565")
        #print("Checking for minecraft server on IP address: " + str(ip))
        try:
            server = JavaServer.lookup(str(ip))
            status = server.status()
            print("- Server Found!\n- IP: "+str(ip)+"\n- MOTD: "+str(status.description)+"\n- Version: "+str(status.version.name)+"\n- Player Count: "+ str(status.players.online)+"/"+str(status.players.max)+"\n- Players Online: NOT WORKING ATM")
            data = {"content" : "```diff\n- Server Found!\n- IP: "+str(ip)+"\n- MOTD: "+str(status.description)+"\n- Version: "+str(status.version.name)+"\n- Player Count: "+ str(status.players.online)+"/"+str(status.players.max)+"\n- Players Online: NOT WORKING ATM```"}
            result = requests.post(url, json = data)
            with open("servers.txt","a") as file:
                file.write(str(ip) + "\n")
        except:
            pass
            #print("server timed out")

for i in range(int(number_of_threads)):
    t1 = Thread(target=task)
    t1.start()
