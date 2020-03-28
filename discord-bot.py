import discord
import random


def discord_bot():
    TOKEN = "DEIN_TOKEN"
    class MyClient(discord.Client):
        #Einloggen
        async def on_ready(self):
            print("Ich habe mich eingeloggt.")
        #Wenn Nachricht gepostet wird
        async def on_message(self, message):
            print("Nachricht von " + str(message.author) + " enthält " + str(message.content))
            if str(message.content) == "Test":
                await message.channel.send("Fest")
    client = MyClient()
    client.run(TOKEN)
