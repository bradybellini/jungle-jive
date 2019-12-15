import discord
import sqlite3
import re
from discord import Message, TextChannel, Member, PartialEmoji
from discord.ext import commands

class Music(commands.cog, name="Please don't stop the music"):

    def __init__(self, client):
        self.client = client

