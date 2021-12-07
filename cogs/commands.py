import discord
from discord.ext import commands
from datetime import datetime

from discord.ext.commands.core import check
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import os


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

        DiscordComponents(self.client)


    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong!")

    @commands.command()
    async def pong(self, ctx):
        await ctx.reply("Ping!")

    @commands.command()
    async def hi(self, ctx):
        await ctx.reply(f"Hello {ctx.author.mention} How are you?")

    @commands.command()
    async def hello(self, ctx):
        await ctx.reply(f"Hello {ctx.author.mention} How are you doing?")

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
            description = "Invite Link of the Bot - https://discord.com/api/oauth2/authorize?client_id=916706978749894666&permissions=545460846583&scope=bot",
            timestamp = datetime.now(),
            color = discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def select(self, ctx):
        await ctx.send("Select", components = [
            Select(
                placeholder = "Select something!",
                options = [
                SelectOption(label="A", value="A"),
                SelectOption(label="B", value="B")
            ]
        )
    ])

    @commands.command()
    async def hi(self, ctx):
        await ctx.send(
            "Hello!",
            components = [
                Button(label = "Hello", style=3)
            ]
        )
        interaction = await self.client.wait_for("button_click", check=lambda i: i.component.label.startswith("Click"))
        await interaction.respond(content="Hello, Nice to meet you! ", ephemeral=False)




def setup(client):
    client.add_cog(Commands(client))
