import discord
import sqlite3
import re
from datetime import datetime
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
            # if message.author == self.client.user or message.channel.id != 399477609559490560:
            #     print('returned')
            #     return
            if 'htt' in message.content and message.author != self.client.user :
                main = sqlite3.connect('music.db')
                cursor = main.cursor()
                sql = ("INSERT or IGNORE INTO links(link, date_posted, author, jump_link, count) VALUES(?,?,?,?,?)")
                val = (str(message.content), str(message.created_at.date()), str(message.author), str(message.jump_url), count)
                cursor.execute(sql, val)
                main.commit()
                cursor.close()
                main.close()
            else:
                pass

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author == self.client.user:
            print('returned')
            return
        else:
            main = sqlite3.connect('music.db')
            cursor = main.cursor()
            if message.channel.id == 399477609559490560 and 'http' in message.content:
                cursor.execute('SELECT link, date_posted, author, jump_link FROM links WHERE link LIKE ?', (message.content,))
                result = cursor.fetchone()
                if not result:
                    sql = ("INSERT INTO links(link, date_posted, author, jump_link) VALUES(?,?,?,?)")
                    val = (str(message.content), str(message.created_at.date()), str(message.author), str(message.jump_url))
                    cursor.execute(sql, val)
                    
                else:
                    embed = discord.Embed(colour = 0x7ed321, description = "This song/link was already posted!")
                    embed.timestamp = datetime.utcnow()
                    embed.set_author(name="Jungle Jive")
                    embed.set_footer(text=f'{self.client.user.name}', icon_url=f'{self.client.user.avatar_url}')
                    embed.add_field(name="Original Poster", value=f"{result[2]}")
                    embed.add_field(name="Link to original post", value=f"[Click here]({result[3]})")
                    embed.add_field(name="Date of original post", value=f"{result[1]}")
                    await message.channel.send(embed=embed)
            main.commit()
            cursor.close()
            main.close()
            
    @commands.command(aliases=['musicchat', 'chat'])
    async def music_chat(self, ctx):
        await ctx.send(file=discord.File('music_channel.png'))

def setup(client):
    client.add_cog(Music(client))
    print('Music Cog loaded')