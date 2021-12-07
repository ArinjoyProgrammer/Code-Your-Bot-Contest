import discord
from discord.ext import commands
from datetime import datetime
import time
import random
import asyncio


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Economy Command has been moved to MAIN.PY. Because the commands are somehow not working in the Cogs


def setup(client):
    client.add_cog(Economy(client))
