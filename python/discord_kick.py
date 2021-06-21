
# def called_by(id_list):
#     def predicate(ctx):
#         return ctx.author.id in id_list
#     return commands.check(predicate)

# target = message.guild.get_member(mention_to_uid(subcommand[0]))

from discord.ext import commands
from discord import Member
import discord
import sys


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, pass_context=True)


@bot.event
async def on_ready():
    members = bot.get_guild(831976182962323476).fetch_members()
    if commands.bot_has_permissions(kick_members=True):
        print('Bot has kick permissions')
    else:
        print("Bot doesn't have kick permissions, terminating")
        sys.exit(1)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick_all(ctx):
    members = bot.get_guild(831976182962323476).fetch_members()
    async for m in members:
        print(m)
        if m.bot or m == bot.get_guild(831976182962323476).owner:
            print('bot/owner')
            continue
        else:
            await m.kick()


@kick_all.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to do that!")

bot.run('NzA4ODAzMzM0NjU5NjM3Mjgz.Xrcqiw.rJVgFQCUlV7uIcKHcG9ZYcUt1HE')

# async for m in members:
#     print(m)
#     if m.bot or m == bot.get_guild(831976182962323476).owner:
#         print('bot/owner')
#         continue
#     else:
#         await bot.kick(m)


# @bot.event
# async def on_ready():
#     print('Logged on as {0}!'.format(bot.user))

#     perm = bot.get_guild(831976182962323476).me.guild_permissions
#     for i in [[p[0], p[1]] for p in perm if p[1]]:
#         print(i[0], i[1])

# for _id in bot.guilds:
#     if _id.name == 'Jdog Testing':
#         print('Found Jdog')
#         server_id = _id.id
#         all_users = bot.get_guild(server_id)
#         for user in all_users.members:
#             print('{} / {}'.format(user.name, user.id))
#         print(all_users.owner)


# @bot.event
# async def on_message(message):
#     await bot.process_commands(message)
# print(message.channel.guild.me.guild_permissions)

# print('Message from {0.author}: {0.content}'.format(message))


# @bot.command(name='myid', pass_context=True)
# async def _myid(ctx):
#     channel = bot.get_channel(831976182962323479)
#     if channel:
#         await channel.send("{} is your id".format(ctx.message.author.id))

# @bot.command(name="kick")
# @called_by(admins)
# async def kick_command(ctx, target: Member, *, reason=None):
#     await target.kick(reason=reason)
# bot.run("token")
