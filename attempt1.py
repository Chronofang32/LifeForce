import asyncio
import discord
from health import health

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('TRANSMIT MESSAGE CAROL ACE RODGER ENZO'):
        await message.channel.send('*4 high pitch tones emit from the sticker to be received by the ships microphone*')

    if message.content.startswith('set'):
        await message.channel.send('set who?', mention_author=True)

        try:
            def check(m):
                return m.channel == message.channel

            await client.wait_for('message', check=check, timeout=45.0)
            print(message.content)
        except asyncio.TimeoutError:
            await message.channel.send('!!TIMEOUT IN LINE 28, REVERTING LOOP!!')

    if message.content.startswith('channel'):
        await message.channel.send('channel printed, check console...')
        print(message.channel)

    if message.content.startswith("."):
        await message.delete()
        whattosay = input()
        await message.channel.send(whattosay)

    if message.content.startswith("radio"): #syntax [radio|channelid|message]
        channum = message.content.split("|")
        msg = channum[2]
        channel = client.get_channel(int(channum[1]))
        await channel.send(msg)

    if message.content.startswith("health"): #syntax [health|set/damage/state|1/2|amount]
        healthcmd = message.content.split("|")
        if healthcmd[1] == "set":
            await message.channel.send(str(health.healthSet(message, int(healthcmd[2]), int(healthcmd[3]))))
        elif healthcmd[1] == "damage":
            await message.channel.send(str(health.healthSub(message, int(healthcmd[2]), int(healthcmd[3]))))
        elif healthcmd[1] == "state":
            if healthcmd[2] == "1":
                await message.channel.send(str(health.HL1))
            elif healthcmd[2] == "2":
                await message.channel.send(str(health.HL2))
            else:
                await message.channel.send("invalid syntax in line 62")
        else:
            await message.channel.send("invalid syntax in line 64")

client.run('')
