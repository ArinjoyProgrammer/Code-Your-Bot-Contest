import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import os


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client



def setup(client):
    client.add_cog(HelpCommand(client))