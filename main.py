import discord
import os
import requests
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #main command 
    if message.content == '/sendLink':
      res = requests.get('https://richup.io/api/room/new?isPrivate=true')

      res= res.json()
      roomId = res['roomId']
        
      link = f"https://richup.io/room/{roomId}"
      await message.channel.send(link)
    
    #this is just a fun command for a friend xD  
    if message.content == '/whoIsKhaista': 
        reply= "Skar ওরফে Shiblu!"
        await message.channel.send(reply)

keep_alive()
client.run(os.getenv('TOKEN'))