import os
import sys


def notizen():
    print("\n")
    print("Notizen")
    print("\n")
    print("[1] Notiz anzeigen")
    print("[2] Notiz erstellen")
    print("[3] Notiz löschen")
    print("\n")
    eingabe = input("> ")
    if int(eingabe) == 1:
        print("\n")
        print("Notiz anzeigen")
        print("\n")
        eingabe = input("Notizname: ")
        notiz_name = eingabe
        datei = open(notiz_name + ".notiz", "r")
        print(datei.read())
    elif int(eingabe) == 2:
        print("\n")
        print("Notiz erstellen")
        print("\n")
        eingabe = input("Notizname: ")
        notiz_name = eingabe
        eingaeb = input("Notizinhalt: ")
        notiz_inhalt = eingabe
        datei = open(notiz_name + ".notiz", "w")
        datei.write(notiz_inhalt)
        datei.close()
    elif int(eingabe) == 3:
        print("\n")
        print("Notiz löschen")
        print("\n")
        datei = open("system.txt", "r")
        rohezeile = datei.readlines(1)
        zeile = ""
        buchstabe = ""
        for buchstabe in rohezeile:
            zeile = zeile + buchstabe
        if zeile == "Linux":
            eingabe = input("Notizname: ")
            notiz_name = eingabe
            os.system("rm " + notiz_name + ".txt")
            print()
        elif zeile == "Windows":
            eingabe = input("Notizname: ")
            notiz_name = eingabe
            os.system("del " + notiz_name + ".txt")
