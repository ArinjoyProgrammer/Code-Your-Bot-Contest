import discord
import discord
from discord.ext import commands
from datetime import datetime
import os


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")

def setup(client):
    client.add_cog(Commands(client))
