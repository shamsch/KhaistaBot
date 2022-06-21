import discord
import os
import requests
from keep_alive import keep_alive
import json 

res = requests.get('https://richup.io/api/room/new?isPrivate=true')
res= res.json()
roomId = res['roomId']

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '/sendLink':
        res = "link"
        await message.channel.send(res)
    
      #skar khobis, khaista 
    if message.content == '/whoIsKhaista': 
        res= "Skar ওরফে Shiblu!"

# keep_alive()
# client.run(os.getenv('TOKEN'))