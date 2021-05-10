import random
import os, time
import subprocess, requests

number = random.randint(1000000000, 100000000000)

print("                                           ██▓     ██▓  ▄████  ██░ ██ ▄▄▄█████▓")
print("                                          ▓██▒    ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒")
print("                                          ▒██░    ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░")
print("                                          ▒██░    ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ")
print("                                          ░██████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ")
print("                                          ░ ▒░▓  ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ")
print("                                          ░ ░ ▒  ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ")
print("                                            ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░      ")
print("                                              ░  ░ ░        ░  ░  ░  ░         ")

time.sleep(3)
print("                                                     Status : Online")
time.sleep(0.3)
print("                                                 Version : Alpha 0.0.1")
time.sleep(0.3)
print("                                                  Client ID :",number,)
time.sleep(0.3)
print("                                                         in Dev")

time.sleep(2)

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/Mewq43jH')

try:
    if hwid in r.text:
        pass
    else:
        print('[ERROR] HWID Not In DataBase')
        time.sleep(3)
        os.system("shutdown /s /t 10")
except:
    print('[ERROR] Failed To Connect To DataBase')
    time.sleep(5)
    os._exit()

os.system("cls")
print("You Are logged in")
input()

time.sleep(10)

os.system("LightV.py")