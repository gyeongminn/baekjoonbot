from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()


def get_data(problem):
    url = 'https://solved.ac/api/v3/problem/show?problemId='+str(problem)
    requestData = requests.get(url)
    return json.loads(requestData.content)


def get_icon(level):
    return 'https://d2gd6pc034wcta.cloudfront.net/tier/'+str(level)+'.svg'


def get_level(level):
    levels = ['Unrated', 'Bronze V', 'Bronze IV', 'Bronze III', 'Bronze II', 'Bronze I',
              'Silver V', 'Silver IV', 'Silver III', 'Silver II', 'Silver I',
              'Gold V', 'Gold IV', 'Gold III', 'Gold II', 'Gold I', 'Platinum V',
              'Platinum IV', 'Platinum III', 'Platinum II', 'Platinum I',
              'Diamond V', 'Diamond IV', 'Diamond III', 'Diamond II', 'Diamond I',
              'Ruby V', 'Ruby IV', 'Ruby III', 'Ruby II', 'Ruby I']
    return levels[int(level)]


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
        problem = url.split('https://www.acmicpc.net/problem/')[1]
        await message.delete()

        data = get_data(problem)

        tags = []
        for t in data['tags']:
            tags.append(t['displayNames'][0]['name'])
        tags = ", ".join(tags)

        embed = discord.Embed(
            title="문제 링크", url="https://www.acmicpc.net/problem/"+problem)
        embed.set_author(name=data['titleKo'], url="https://www.acmicpc.net/problem/" +
                         problem, icon_url="https://im2.ezgif.com/tmp/ezgif-2-21a8b14550.png")
        embed.add_field(name="문제 번호", value=data['problemId'], inline=True)
        embed.add_field(name="난이도", value=get_level(
            data['level']), inline=True)
        embed.add_field(name="유형", value=tags, inline=False)
        await message.channel.send(embed=embed)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
