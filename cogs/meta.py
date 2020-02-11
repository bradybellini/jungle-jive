import discord
from discord.ext import commands, tasks

class Meta(commands.Cog, name='Meta Related Commands'):

    def __init__(self, client): 
        self.client = client

    @commands.command(hidden=True, aliases=['kill', 'stop'])
    @commands.is_owner()
    async def kill_bot(self, ctx):
        ": Shuts down the bot on the server"
        await ctx.send('Shutting down...')
        await ctx.send('Goodbye')
        await self.client.logout()

    @commands.command()
    async def ping(self, ctx, ping=None):
        if ping == None:
            await ctx.send(f'Pong! Latency to Server: `{round(self.client.latency * 1000)}ms`')
        else:
            await ctx.send('no ping for you')

def setup(client):
    client.add_cog(Meta(client))
    print('Meta Cog loaded')
