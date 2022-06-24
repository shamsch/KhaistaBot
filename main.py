import discord
import os
import requests
from keep_alive import keep_alive


token = os.environ['token']

client = discord.Client()

# on ready event
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

# make a get request to richup io api and get a private room id  
def get_room_id():
    res = requests.get('https://richup.io/api/room/new?isPrivate=true')
    res = res.json()
    return res['roomId']


# find a channel by name and get all messages in it when command is called 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #richup io private room command
    if message.content.startswith('!richup'):
        room_id = get_room_id()
        await message.channel.send(f'https://richup.io/room/{room_id}')
    
    #this is just a fun command for a friend and also pings the bot
    if message.content.startswith('!ping'): 
        reply= "kire Skar, ar koto khaistami korbe?"
        await message.channel.send(reply)

    if message.content.startswith('!words'):
        skribble_channel = discord.utils.get(message.guild.channels, name='temp-skribbl-words')
        bot_channel = discord.utils.get(message.guild.channels, name='bot-stuff')
        words = []
        async for message in skribble_channel.history(limit=None):
            words.append(message.content)
        
        #make words all words smaller case
        words = [word.lower() for word in words]
        #make words unique
        words = list(set(words))
        #sort words alphabetically
        words.sort()
        #add words to a text file separated by , and send it to the channel
        with open('words.txt', 'w') as f:
            for word in words:
                #for last word, don't add a comma
                if word == words[-1]:
                    f.write(word)
                else:
                    f.write(word + ',')
            
        await bot_channel.send(file=discord.File('words.txt'))       
        os.remove('words.txt')

keep_alive()
client.run(token)