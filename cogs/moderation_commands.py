import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import os


class ModerationCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send("THE MESSAGES ARE DELETED", delete_after=2)



def setup(client):
    client.add_cog(ModerationCommands(client))
