import discord
import sqlite3
import re
from discord import Message, TextChannel, Member, PartialEmoji
from discord.ext import commands

class Music(commands.Cog, name="Please don't stop the music"):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['history'])
    async def gethistory(self, ctx, ping=None):
        async for message in client.channel.history(limit=1000):
            if message