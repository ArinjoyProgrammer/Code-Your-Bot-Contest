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
    async def luckynumber(ctx):
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


    @commands.command()
    async def hack(self, ctx, member : discord.Member):

        random_password = ['36b29c', 'kt764a', '45cvv76', 'fh90;ll', 'gda889', 'kla789', 'kkk89q', 'ff89f52', '95632lrt']

        await ctx.send(f"Hacking Satrted on {member}")
        await ctx.send(f"Hacking Username and Password of {member}")
        await asyncio.sleep(4)
        await ctx.send(f"Hacked!\nUsername - ``{member}``\nPassword - ``{random.choice(random_password)}``")
        await asyncio.sleep(4)
        await ctx.send("Hacking Completed 20%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 30%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 50%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Epic Games and Steam Account")
        await asyncio.sleep(2)
        await ctx.send("Hacking Epic Games and Steam Account Completed Successfully")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 80%")
        await asyncio.sleep(3)
        await ctx.send("Hacking Completed 90%")
        await asyncio.sleep(4)
        await ctx.send(f"A **Dangerous Hacking** Completed on **{member}**\nDon't mind this was a really **Fake Hack**")


    @commands.command()
    async def greet(self, ctx, member: discord.Member, *, greet_msg="No **Greet Message** was given"):
        embed = discord.Embed(
            title = "Greet Message",
            description = f"You Greeted **{greet_msg}** to {member.mention}",
            timestamp = datetime.now(),
            color = ctx.author.color
        )
        await ctx.send(embed=embed)

    
    @commands.command()
    async def nowtime(self, ctx):
        nowtime = time.striftime("Date: %d/%m/%y\nTime: %H:%M:%S")

        embed = discord.Embed(
            title = "Now the Time is",
            description = f"{nowtime}",
            color = ctx.author.color
        )


def setup(client):
    client.add_cog(FunCommands(client))
