import sys
import os
import random
import time
try:
    import discord
except:
    os.system("pip3 install discord")
    import discord


def discordreader():
    print("1. Gehe auf die Seite https://discordapp.com/developers/applications")
    print("\n")
    print("2. Melde dich mit deinem Discordaccount an, oder registriere dich.")
    print("\n")
    print('3. Erstelle eine neue Anwendung (Klicke auf "New Application")')
    print("\n")
    print("4. Gebe deinem Bot einen Namen (z. B. Mein Bot)")
    print("\n")
    eingabe = input("5. Kopiere die Client ID hier rein: ")
    client_id = eingabe
    print("\n")
    print("6. Klicke oben links auf die drei übereinanderliegenden Striche")
    print('   und klicke danach auf "Bot"')
    print("\n")
    print('7. Erstelle einen Bot (Klicke auf "Add Bot")')
    print("\n")
    print('8. Kopiere nun den Token (Klicke auf "Copy" bei der Überschrift "TOKEN")')
    eingabe = input("und füge den Token hier ein: ")
    token = eingabe
    TOKEN = token
    print("\n")
    print("Lade nun den Bot ein in dem du auf die Seite")
    print("https://discordapp.com/api/oauth2/authorize?client_id=" + client_id + "&scope=bot&permissions=8 gehst.")
    print("\n")
    time.sleep(16)
    class MyClient(discord.Client):
        #Einloggen
        async def on_ready(self):
            print("Ich habe mich eingeloggt. Jetzt kannst du alle Nachrichten sehen.")
        #Wenn Nachricht gepostet wird
        async def on_message(self, message):
            print("Nachricht von " + str(message.author) + " enthält " + str(message.content))
    client = MyClient()
    client.run(TOKEN)
