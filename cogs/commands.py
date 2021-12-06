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

    @commands.command()
    async def pong(self, ctx):
        await ctx.reply("Ping!")

    @commands.command()
    async def hi(self, ctx):
        await ctx.reply(f"Hello! {ctx.author.mention} How are you?")

    @commands.command()
    async def hello(self, ctx):
        await ctx.reply(f"Hi {ctx.author.mention} How are you doing?")

    @commands.command()
    async def fine(self, ctx):
        await ctx.reply("Wow! Excellent Work!!")

    @commands.command()
    async def bad(self, ctx):
        await ctx.reply("Oh! That's not good!")

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Invite Link",
            description = "Invite Link of the Bot - <link>",
            timestamp = datetime.now(),
            color = discord.Color.blue()
        )
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Commands(client))
