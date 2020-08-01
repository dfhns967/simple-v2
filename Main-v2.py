#importing the packages
import discord
import random
 
#the nedded vars
Token = "NzM4OTA2NzI1MjU1NjEwMzY5.XySugw.hzp4o8lILpRPiw1QdPpVoetklCw"
client = discord.Client()
 
#for random picking
welcoming = [
    'yo welcome buddy',
    'welcome its me deadpool'
]
 
#the commands 
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
 
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Anime Bird server!'
    )
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content == 'iam back':
        response = random.choice(welcoming)
        await message.channel.send(response)
        
#firing up the bot
client.run(Token)
