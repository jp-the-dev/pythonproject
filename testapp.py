import restartapi
import installapi
import sys
import os
import time


def testapp():
    print("Testapp")
    print("\n")
    print("Hier gibt es keine Infos...")
    print("\n")
    time.sleep(2)
    print("[1] Testapp aktualisieren")
    print("[ENTER] Testapp beenden")
    eingabe = input("")
    if eingabe == "1":
        installapi.installapi3("testapp")
        restartapi.restartapi()
    else:
        print()
