import os
import smtplib 

from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

client = Bot("-")

@client.event
async def on_ready():
    print('Music Bot Ready')

@client.command(aliases=['p', 'pl'])
async def play(ctx, url: str = 'https://nr3.newradio.it/proxy/omnianet?mp=/stream'):
    channel = ctx.message.author.voice.channel
    player = ctx.message.author
    
    try:
        voice = await channel.connect()
    except:
        pass
    
    source = FFmpegPCMAudio(executable="C:/Users/Luca/Documents/nn/trp/bin/ffmpeg.exe", source=url)
    player = voice.play(source)

@client.command()
async def richiesta(ctx, *oper):
    channel = client.get_channel(826030047554043934)
    await channel.send('Grazie per aver richiesto: ' + " ".join(oper[:]))

@client.command(aliases=['s', 'st'])
async def stop(ctx):
    player.stop()

client.run(os.environ.get('TOKEN'))