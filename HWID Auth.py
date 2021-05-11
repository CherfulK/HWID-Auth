import os, time
import subprocess, requests

print("                                           ██▓     ██▓  ▄████  ██░ ██ ▄▄▄█████▓")
print("                                          ▓██▒    ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒")
print("                                          ▒██░    ▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░")
print("                                          ▒██░    ░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ")
print("                                          ░██████▒░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ")
print("                                          ░ ▒░▓  ░░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ")
print("                                          ░ ░ ▒  ░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ")
print("                                            ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░      ")
print("                                              ░  ░ ░        ░  ░  ░  ░         ")



hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/Mewq43jH')

try:
    if hwid in r.text:
        pass
    else:
        print('[ERROR] HWID Not In DataBase')
        print("Copy You're HWID")
        print(f'HWID: {hwid}')
        time.sleep(3)
        os._exit()
except:
    print('[ERROR] Failed To Connect To DataBase')
    time.sleep(5)
    os._exit()

print("You Are logged in")
input()

time.sleep(5)
os.system("LightV.py")
