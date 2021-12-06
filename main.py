import discord
from discord.ext import commands
from datetime import datetime
import random
import os
from dotenv import load_dotenv

load_dotenv()

prefixes = '.', '!', '>'

client = commands.Bot(command_prefix = prefixes)
client.remove_command("help")


@client.event
async def on_ready():
    print("The Bot is Ready")


# Commands which haven't worked in Cogs!
# None are here


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")



client.run(os.getenv('token'))
