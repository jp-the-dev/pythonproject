import urllib.request
import sys
import os
import time
import adressen


def thenewsofjpthedev():
    print("\n")
    print("TheNewsOfJPTheDev")
    print("\n")
    print("Alle Artikel werden nach einer Woche (16.03.2020 & 17.03.2020)")
    print("ins Archiv versetzt, dort sind sie aber trotzdem")
    print("jederzeit und kostenlos abrufbar.")
    print("Wir freuen uns, wenn Sie unsere Programme gut finden.")
    print('Jede Woche gibt es aktuelle Nachrichten zum Thema "Computer & Internet"')
    print("Falls Sie Programmier- oder Rechtschreibfehler entdeckt haben melden Sie diese hier: " + adressen.email)
    print("\n")
    print('Am 16.03.2020 finden Sie das Thema "Begriffserklärung für viele Begriffe (Computer, Programmieren)"')
    print("als Artikel vor. Wir wünschen Ihnen noch eine schöne Woche.")
    print("\n")
    print("Die aktuellen Nachrichten")
    print("\n")
    print("[1] Petya ist jetzt 4 Jahre alt...                           (Deutsch) - 09.03.2020")
    print("[2] Welche Computerviren sind bisher die gefährlichsten?     (Deutsch) - 09.03.2020")
    print("[3] Sind Hacker böse?                                        (Deutsch) - 10.03.2020")
    print("[4] TheNewsOfJPTheDev - Archiv                               (Deutsch)")
    print("[5] TheNewsOfJPTheDev Aktualisieren")
    print("\n")
    print("Stand: 09.03.2020")
    print("\n")
    eingabe = input("> ")
    if int(eingabe) == 1:
        print("\n")
        print("Petya ist jetzt 4 Jahre alt... (Deutsch) - 09.03.2020")
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
        print("Welche Computerviren waren bisher die gefährlichsten? (Deutsch) - 09.03.2020")
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
        print("NotPetya")
        print("\n")
        print("Der Artikel wurde von JP-The-Dev verfasst")
        print("Angaben ohne Gewähr")
        print("\n")
    elif int(eingabe) == 3:
        print("\n")
        print("Sind Hacker böse? (Deutsch) - 10.03.2020")
        print("\n")
        print("Nein, Hacker sind nicht böse.")
        print("Hacker sind computerinteressierte")
        print("Personen, die darauf spezialisiert sind,")
        print("Schwachstellen zu finden um diese zu teilen oder")
        print("zu beheben (Patch). Ein Cracker allerdings greift")
        print("die Schwachstellen an und nutzt diese aus, um")
        print("Systeme lahmzulegen. Oft wird ein Hacker meist")
        print("mit einem Cracker verwechselt, deshalb ist der")
        print("Begriff Hacker meist der, der für den eigentlichen")
        print("Cracker verwendet wird.")
        print("\n")
        print("Der Artikel wurde von JP-The-Dev verfasst")
        print("Angaben ohne Gewähr")
        print("\n")
    elif int(eingabe) == 4:
        print("\n")
        print("TheNewsOfJPTheDev - Archiv")
        print("\n")
        print("Tut mir leid, aber das Archiv")
        print("ist noch leer, nächste Woche (16.03.2020 & 17.03.2020)")
        print("wird es mit vergangenen Nachrichten")
        print("aufgefüllt, bis später.")
        print("\n")
    elif int(eingabe) == 5:
        print("\n")
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
