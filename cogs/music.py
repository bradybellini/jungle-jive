import discord
import sqlite3
import re
from discord import Message, TextChannel, Member, PartialEmoji
from discord.ext import commands

class Music(commands.Cog, name="Please don't stop the music"):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['history'])
    async def gethistory(self, ctx):
        async for message in self.client.channel.history(limit=1000):
            messages = await channel.history(limit=1000).flatten()
            if 'htt' in message.content:
                await ctx.send(messages)
                # main = sqlite3.connect('music.db')
                # cursor = main.cursor()
                # sql = ("INSERT INTO links(link, date_posted, author, jump_url)")
                # val = (str(message.con))


def setup(client):
    client.add_cog(Music(client))
    print('Music Cog loaded')

