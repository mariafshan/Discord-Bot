# mario.py
import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        text = 'Hello {0.mention}!'.format(message.author)
        await message.channel.send(text)

    if message.content.startswith('$say '):
        text = message.content[5:]
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith('$announce'):
        await message.delete()
        allowed_mentions = discord.AllowedMentions(everyone = True)
        announcement = []
        with open('announcement.txt') as text:
            for line in text:
                line = line.strip()
                announcement.append(line)
        text = ""
        for i in range(len(announcement)):
            text = str(text) + "\n" + str(announcement[i])
        announcement.clear()
        await message.channel.send(content = text,
                                   allowed_mentions = allowed_mentions, delete_after=5.0)
        # await message.channel.send(content = text, allowed_mentions = allowed_mentions)

    if message.content.startswith('$help'):
        text = open('help.txt')
        text_list = []
        for line in text:
            line = line.strip()
            text_list.append(line)
        text.close()
        text = ""
        for i in range(len(text_list)):
            text = str(text) + "\n" + str(text_list[i])
        await message.channel.send("```" + text + "```")
        text_list.clear()

client.run(os.getenv('TOKEN'))
