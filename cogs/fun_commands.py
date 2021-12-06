import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import random
import os


class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def slap(self, ctx, member: discord.Member, *, reason="No **Reason** was given for **Slapping**"):
        await ctx.send(f"You **Slapped** {member.mention}  |  Reason: **{reason}**")


    @commands.command()
    async def wish(self, ctx, member: discord.Member, *, wish=f"No **Wish** was given for the **User**"):
        await ctx.send(f"You wished **{wish}** for {member.mention}")


    @commands.command()
    async def luckynumber(self, ctx):
        lucky_number = random.randint(0, 100)

        embed = discord.Embed(
            title = "Your Lucky Number",
            description = f"Your **Lucky Number** is **{lucky_number}**\nNote - don't forget to check your Lucky Number again!",
            timestamp = datetime.now(),
            color = ctx.author.color
        )
        await ctx.send(embed=embed)

        if (lucky_number == 100):
            await ctx.send("Wow! I think your day is going on well !!!")


        @commands.command()
        async def coolrate(self, ctx):
            coolrate = random.randint(0, 100)

            embed = discord.Embed(
                title = "What is your Cool Rate?",
                description = f"Your **Cool Rate** is **{coolrate}**%",
                timestamp = datetime.now(),
                color = ctx.author.color
            )
            await ctx.send(embed=embed)

            if (coolrate == 100):
                await ctx.send("Yeah! You are very very much **Cool**")


def setup(client):
    client.add_cog(FunCommands(client))
