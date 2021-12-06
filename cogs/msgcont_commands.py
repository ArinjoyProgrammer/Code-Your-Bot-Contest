import discord
from discord.ext import commands
from discord.ext.commands.converter import GuildConverter
from discord.ext.commands.core import command


class MessageContentCommand(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("Perfectz"):
            await message.channel.send("My Prefixes are in this server are ``>``")



def setup(client):
    client.add_cog(MessageContentCommand(client))
