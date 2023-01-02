from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)
client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{PREFIX}백준'):
        url = str(message.content).split('/백준 ')[1]
        await message.channel.send('문제 링크 :'+url)
        print(url)
        await message.content.delete()


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
