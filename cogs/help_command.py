import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import os


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

        

    @commands.command()
    async def help(self, ctx):
        member = ctx.author

        embed = discord.Embed(
            title = "Help Command for  **__Perfectz__**",
            description = "This is a Help Command for **__Perfectz Bot __**",
            timestamp = datetime.now(),
            color = ctx.author.color
        )
        embed.set_author(
            name=self.client.user.name,
            icon_url=self.client.user.avatar_url
        )
        embed.add_field(name = "_ _", value = "_ _", inline = False)
        embed.add_field(
            name = "Chat Commands (With Prefix)",
            value = "``ping``, ``pong``, ``hi``, ``hello``, ``fine``, ``bad``, ``invite``",
            inline = False
        )
        embed.add_field(name = "_ _", value = "_ _", inline = False)
        embed.add_field(
            name = "Fun Commands (With Prefix)",
            value = "``slap``, ``wish``, ``luckynumber``, ``coolrate``, ``hack``, ``greet``, ``nowtime``, ``rip``",
            inline = False
        )
        embed.add_field(name = "_ _", value = "_ _", inline = False)
        embed.add_field(
            name = "Special Commands (With Prefix)",
            value = "``serverinfo``, ``whois``, ``joined``, ``membercount``, ``announcement``",
            inline = False
        )
        embed.add_field(name = "_ _", value = "_ _", inline = False)
        embed.add_field(
            name = "Moderation Commands (With Prefix)",
            value = "``mute``, ``unmute``, ``kick``, ``ban``, ``unban``, ``report``, ``warn``, ``clear``",
            inline = False
        )
        embed.add_field(name = "_ _", value = "_ _", inline = False)
        embed.add_field(
            name = "Support Us",
            value = "[Invite](https://discord.com/api/oauth2/authorize?client_id=916706978749894666&permissions=545460846583&scope=bot)",
            inline = False
        )
        embed.add_field(name = "_ _", value = "_ _", inline = False)
        embed.set_footer(
            text = "Developed By < Arinjoy.py />#8981"
        )

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(HelpCommand(client))
