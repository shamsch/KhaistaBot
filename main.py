import discord
import os
import requests

x = requests.get('https://richup.io/api/room/new?isPrivate=true')
print(x)

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content == '/sendLink':
#         res = "link"
#         await message.channel.send(res)

# client.run(os.getenv('TOKEN'))