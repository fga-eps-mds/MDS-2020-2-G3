import discord
from discord.ext import commands

# Prefixo
client = commands.Bot(command_prefix = ';')

@client.event
async def on_ready():
    print('teste')

client.run('token do bot')
