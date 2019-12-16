import discord
import os
from key import discord_api
from discord.ext import commands, tasks
from itertools import cycle

#Meta stuff#
client = commands.Bot(command_prefix = 'jj.')
# client.remove_command('help')
status = '!jj help'

#########################################
#                                       #
#               Events                  #
#     Figure out how to move to cog     #
#########################################

#Says when bot is ready and invokes listed loops#
@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

#########################################
#                                       #
#               Loops                   #
#                                       #
#########################################

@tasks.loop(minutes=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#########################################
#                                       #
#         Cog Related Commands          #
#                                       #
#########################################

@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} cog has loaded')
    except Exception as e:
        print(f'{extension} cog could not be loaded')
        raise e

@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} cog unloaded')
    except Exception as e:
        print(f'{extension} cog could not be unloaded')
        raise e

@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} cog reloaded')
    except Exception as e:
        print(f'{extension} cog could not be reloaded')
        raise e

#########################################
#                                       #
#          Other Meta Stuff             #
#                                       #
#########################################

#Initial load of cog files#
for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        try:
            client.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            print(f'{filename} cog can not be loaded')
            raise e



#Bot API Token#
client.run(discord_api)