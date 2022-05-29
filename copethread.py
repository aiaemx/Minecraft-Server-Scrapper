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
url = "https://discord.com/api/webhooks/977980292767830036/9g1r4t-YXMTphz07RnBnqOwfpjslk74mio6Dq9eozMGp_eZL6hNnlE6Z5SGoXnC1eQvP"
if len(url) < 5:
    print("You haven't put in a webhook, so it's going to run locally.")
    time.sleep(2)

logo = """

  /$$$$$$                      /$$
 /$$__  $$                    |__/
| $$  \__/  /$$$$$$   /$$$$$$  /$$ /$$   /$$ /$$$$$$/$$$$
| $$       /$$__  $$ /$$__  $$| $$| $$  | $$| $$_  $$_  $$
| $$      | $$  \ $$| $$  \ $$| $$| $$  | $$| $$ \ $$ \ $$
| $$    $$| $$  | $$| $$  | $$| $$| $$  | $$| $$ | $$ | $$
|  $$$$$$/|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/| $$ | $$ | $$
 \______/  \______/ | $$____/ |__/ \______/ |__/ |__/ |__/
                    | $$
                    | $$
                    |__/
"""
print(logo)
time.sleep(1)
number_of_threads = "20000"

def task():
    name = "worker" + str(random.randint(0,99))
    while True:
        ip = (str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + ":25565")
        #print("Checking for minecraft server on IP address: " + str(ip))
        try:
            server = JavaServer.lookup(str(ip))
            status = server.status()
            print("Server Found!\nIP Address & Port: "+str(ip)+"\nPlayers Online: "+str(status.players.online))
            data = {"content" : "**Server Found!**\n**IP Address & Port:** "+str(ip)+"\n**Players Online:** "+str(status.players.online)}
            result = requests.post(url, json = data)
            with open("servers.txt","a") as file:
                file.write(str(ip) + "\n")
        except:
            pass
            #print("server timed out")

for i in range(int(number_of_threads)):
    t1 = Thread(target=task)
    t1.start()
