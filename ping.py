import os
import sys


def ping():
    print("\n")
    print("Ping")
    print("\n")
    hostname = input("IP: ")
    response = os.system("ping " + hostname)
    if response == 0:
        print("\n")
        print("Verbindung aufgebaut!")
        print("\n")
        return 0
    else:
        print("\n")
        print("Verbindung konnte nicht hergestellt werden!")
        print("\n")
        return 1
