import urllib.request
import sys
import os
import time


def thenewsofjpthedev():
    print("\n")
    print("TheNewsOfJPTheDev")
    print("\n")
    print("Alle Artikel werden nach einer Woche ins")
    print("Archiv versetzt, dort sind sie aber trotzdem")
    print("jederzeit und kostenlos abrufbar.")
    print("Bei Fragen oder Problemen jp-the-dev@gmail.com")
    print("kontaktieren. Danke für deine Hilfe")
    print("\n")
    print("Die aktuellen Nachrichten")
    print("\n")
    print("[1] Petya ist jetzt 4 Jahre alt...                      (Deutsch) - 09.03.2020")
    print("[2] Welche Computerviren sind die gefährlichsten?       (Deutsch) - 09.03.2020")
    print("[3] TheNewsOfJPTheDev - Archiv                          (Deutsch)")
    print("\n")
    print("Stand: 09.03.2020")
    print("\n")
    eingabe = input("> ")
    if int(eingabe) == 1:
        print("\n")
        print("Petya ist jetzt 4 Jahre alt...")
        print("\n")
        print("Was ist Petya?")
        print("Petya ist ein Verschlüsselungstrojaner,")
        print("der 2016 zuerst entdeckt wurde.")
        print("Er schrieb sich ins Bootmenü und wurde")
        print("somit immer wieder gestartet.")
        print("\n")
        print("Wie lief es ab, wenn Petya ausgeführt wurde?")
        print("\n")
        print("1. Petya schreibt sich ins Bootmenü und startet nun")
        print("   den PC neu.")
        print("2. Petya wird als Betriebssystem ausgeführt und verschlüsselt")
        print("   alle Datenträger, es sieht so aus, als wenn gerade ein")
        print("   Laufwerk repariert wird, aber in Wirklichkeit wird es von")
        print("   Petya nur verschlüsselt.")
        print("3. Wenn nun der Prozess abgeschlossen ist, wird Petya gestartet,")
        print("   der Bildschirm blinkt / flackert und ein weißer Totenkopf auf")
        print("   einem roten Hintergrund erscheint, Petya!")
        print("4. Petya möchte nun, dass man Bitcoin im Wert von 300$ an eine")
        print("   spezielle Bitcoinadresse sendet, damit der PC wieder entschlüsselt")
        print("   werden kann, dies kann man aber mit einer speziellen Software umgehen,")
        print("   die aktuell und kostenlos vertrieben wird, feststeht, dass man Petya")
        print("   überlisten und seinen PC retten kann.")
        print("\n")
        print("Der Artikel wurde von JP-The-Dev verfasst.")
        print("Angaben ohne Gewähr")
        print("\n")
    elif int(eingabe) == 2:
        print("\n")
        print("Welche Computerviren sind die gefährlichsten?")
        print("\n")
        print("Jerusalem")
        print("Morris")
        print("Melissa")
        print("ILOVEYOU")
        print("Klez")
        print("Code Red")
        print("Sobig F.")
        print("MyDoom")
        print("Nuwar")
        print("Conf*cker")
        print("\n")
    elif int(eingabe) == 3:
        print("\n")
        print("TheNewsOfJPTheDev - Archiv")
        print("\n")
        print("Tut mir leid, aber das Archiv")
        print("ist noch leer.")
        print("\n")
    time.sleep(3)
    print("\n")
    print("[1] TheNewsOfJPTheDev aktualisieren")
    print("[ENTER] News beenden")
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
                url = "https://raw.githubusercontent.com/jp-the-dev/pythonproject/master/" + self + ".py"
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
        extra_apps("thenewsofjpthedev")
    else:
        print()
