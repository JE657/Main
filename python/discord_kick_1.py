from discord.ext import commands
from discord import Member
import discord
import sys

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, pass_context=True)

SERVER_ID = 831976182962323476


@bot.event
async def on_ready():
    members = bot.get_guild(SERVER_ID).fetch_members()
    if commands.bot_has_permissions(kick_members=True):
        print('Bot has kick permissions')
    else:
        print("Bot doesn't have kick permissions, terminating")
        sys.exit(1)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick_all(ctx):
    members = bot.get_guild(SERVER_ID).fetch_members()
    async for m in members:
        print(m)
        if m.bot or m == bot.get_guild(SERVER_ID).owner:
            print('bot/owner')
            continue
        else:
            await m.kick()


@kick_all.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to do that!")

# Bot ID, Dont Modify
bot.run('NzA4ODAzMzM0NjU5NjM3Mjgz.Xrcqiw.rJVgFQCUlV7uIcKHcG9ZYcUt1HE')
