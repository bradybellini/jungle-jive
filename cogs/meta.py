import discord
from discord.ext import commands, tasks

class Meta(commands.Cog, name='Meta Related Commands'):

    def __init__(self, client): 
        self.client = client

    @commands.command()
    async def ping(self, ctx, ping=None):
        if ping == None:
            await ctx.send(f'Pong! Latency to Server: `{round(self.client.latency * 1000)}ms`')
        else:
            await ctx.send('no ping for you')

def setup(client):
    client.add_cog(Meta(client))
    print('Meta Cog loaded')