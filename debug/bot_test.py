import discord

PREFIX = '/'
TOKEN = 'MTA1NTc5MTg2MTU3MjMyNTQxNw.Gke9cZ.HV0xh3n-TdIhDuqs9R9kw3wqjhBoboIQ2AB5Ok'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# client = discord.Client()


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{PREFIX}백준'):
        url = str(message.content).split('/백준 ')[1]
        await message.delete()
        await message.channel.send('문제 링크 :'+url)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
