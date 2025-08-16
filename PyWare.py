import time
import os
import requests

Webhook_url = "https://example.com"
print("--PyWare--")
Run = input("This is SPYWARE are you sure you want to run? Y/N | ")
if Run.upper() == "Y":
    Confirm = input("Are you POSITIVE you want to run this? Y/N | ")
    if Confirm.upper() == "Y":
        print("Test")
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
