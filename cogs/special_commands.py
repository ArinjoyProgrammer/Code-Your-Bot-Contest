import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
import os


class SpecialCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def serverinfo(ctx):
        name = str(ctx.guild.name)

        server_name = str(ctx.guild.name)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description="",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Server Name", value=server_name, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Channels: ", value=len(
        ctx.message.guild.channels), inline=True)
        embed.add_field(name="Country", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.add_field(name="Requested By: ", value=str(
        ctx.message.author.mention), inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def whois(self, ctx, user: discord.Member = None):

        created_at = user.created_at
        joined_at = user.joined_at

        created = created_at.strftime("Date: %d/%m/%y  |  Time: %H:%M:%S")
        joined = joined_at.strftime("Date: %d/%m/%y  |  Time: %H:%M:%S")

        if user == None:
            user = ctx.author

        rlist = []
        for role in user.roles:
            if role.name != "@everyone":
                rlist.append(role.mention)

        b = ", ".join(rlist)

        embed = discord.Embed(colour=user.color, timestamp=datetime.now())

        embed.set_author(name=f"User Info - {user}"),
        embed.set_thumbnail(url=user.avatar_url),

        embed.add_field(name='ID:', value=user.id, inline=False)
        embed.add_field(name='Name:', value=user.display_name, inline=False)

        embed.add_field(name='Created at:', value=created, inline=False)
        embed.add_field(name='Joined at:', value=joined, inline=False)

        embed.add_field(name='Bot?', value=user.bot, inline=False)

        embed.add_field(name=f'Roles:({len(rlist)})',
                        value=''.join([b]), inline=False)
        embed.add_field(name='Top Role:',
                        value=user.top_role.mention, inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    async def joined(self, ctx, *, member: discord.Member):
        joined_at = member.joined_at
        time_joined = joined_at.strftime("Date: %d/%m/%y  |  Time: %H:%M:%S")

        await ctx.send(f"**{member}** joined on **{time_joined}**")


    @commands.command()
    async def membercount(self, ctx):
        embed = discord.Embed(
            title = "Members",
            description = f"{ctx.guild.member_count}",
            timestamp = datetime.now(),
            color = ctx.author.color
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(SpecialCommands(client))
