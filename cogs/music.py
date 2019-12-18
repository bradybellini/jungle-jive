import discord
import sqlite3
import re
from discord import Message, TextChannel, Member, PartialEmoji
from discord.ext import commands

class Music(commands.Cog, name="Please don't stop the music"):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['history'])
    @commands.is_owner()
    async def gethistory(self, ctx):
        count = 0

        async for message in ctx.channel.history(limit = None, oldest_first = True):
            if message.author == self.client.user.id:
                pass
            elif 'htt' in message.content:
                main = sqlite3.connect('music.db')
                cursor = main.cursor()
                sql = ("INSERT or IGNORE INTO links(link, date_posted, author, jump_link, count) VALUES(?,?,?,?,?)")
                val = (str(message.content), str(message.created_at), str(message.author), str(message.jump_url), count)
                cursor.execute(sql, val)
                main.commit()
                cursor.close()
                main.close()

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author == self.client.user.id:
            return
        else:
            main = sqlite3.connect('music.db')
            cursor = main.cursor()
            if message.channel.id == 399477609559490560 and 'http' in message.content:
                cursor.execute('SELECT link, author, jump_url FROM links WHERE link = ?', (message.content,))
                result = cursor.fetchone()
                if not result:
                    sql = ("INSERT INTO links(link, date_posted, author, jump_url) VALUES(?,?,?,?)")
                    val = (str(message.content), str(message.created_at), str(message.author), str(message.jump_url))
                    cursor.execute(sql, val)
                    
                else:
                    await message.channel.send(str(result[2]))
            main.commit()
            cursor.close()
            main.close()


def setup(client):
    client.add_cog(Music(client))
    print('Music Cog loaded')