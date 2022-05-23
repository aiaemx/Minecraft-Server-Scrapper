from threading import Thread
import random
import requests
from mcstatus import JavaServer

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
number_of_threads = input("How many threads do you want? [200000 is recommended] ")
name = input("What is your name? [used when the server is posted] ")

def task():
    while True:
        ip = (str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + ":25565")
        print("Checking for minecraft server on IP address: " + str(ip))
        try:
            server = JavaServer.lookup(str(ip))
            status = server.status()
            url = "https://discord.com/api/webhooks/977980292767830036/9g1r4t-YXMTphz07RnBnqOwfpjslk74mio6Dq9eozMGp_eZL6hNnlE6Z5SGoXnC1eQvP"
            data = {"content" : "Server found at " + str(ip) + " nns online: " + str(status.players.online) + ". server found by " + str(name)}
            result = requests.post(url, json = data)
            with open("servers.txt","a") as file:
                file.write(str(ip) + "\n")
        except:
            print("server timed out")

for i in range(int(number_of_threads)):
    t1 = Thread(target=task)
    t1.start()
