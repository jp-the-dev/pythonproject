import time
import sys
import urllib.request
import os


def update():
    print("\n")
    print("Update")
    print("\n")
    print("Die aktuelle Version ist 1.2,")
    print("alsbald erscheint die Version 1.3.")
    print("\n")
    print("Stand: 08.03.2020")
    time.sleep(3)
    print("\n")
    print("[1] Update aktualisieren")
    print("[ENTER] Update beenden")
    eingabe = input("> ")
    if eingabe == "1":
        def extra_apps(self):
            def check_ping():
                hostname = "www.github.com"
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
        def extra_apps_download(self):
            url = "https://raw.githubusercontent.com/jp-the-dev/pythonproject/master" + self + ".py"
            name = self + ".py"
            urllib.request.urlretrieve(url, name)
            url = "https://raw.githubusercontent.com/jp-the-dev/pythonproject/master/" + self + "-starter.py"
            name = self + "-starter.py"
            urllib.request.urlretrieve(url, name)
            print("\n")
            print("Bitte starte JannOS neu!")
            print("\n")
            sys.exit()
        if int(check_ping()) == 0:
            extra_apps_download(self)
        elif int(check_ping()) == 1:
            print("\n")
        extra_apps("update")
    else:
        print()
