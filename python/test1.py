# # Open the files as read-only
# jokes = open("jokes.txt", "r")
# answers = open("answers.txt", "r")

# # Get the first line and do something with it
# # joke_line = jokes.readline()
# # answer_line = answers.readline()

# # get all jokes
# all_jokes = jokes.readlines()
# all_answers = answers.readlines()

# print(all_jokes)

# joke_num = 0

# # get number of jokes
# number_jokes = len(all_jokes)
# print("There are", number_jokes, "jokes")

# x = int(input("Which joke do you want to see? "))

# print("Joke #" + str(x))
# print(all_jokes[x - 1])
# print(all_answers[x - 1])

# import random as rn


# def gen_list():
#     nums = []
#     single_digit = rn.randrange(0, 10)
#     print(single_digit)
#     for i in range(10):
#         if i != single_digit:
#             nums.append(i)
#             nums.append(i)
#         else:
#             nums.append(i)
#     print(*nums)
#     return nums

def scale(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

from bs4 import BeautifulSoup
import requests as rq
import os
import discord
from dotenv import load_dotenv
from time import sleep
import datetime

base_url = "https://twitter.com/"
handle = "@Starboardstudi1"


scrape_url = base_url + handle

response = rq.get(scrape_url)
soup = BeautifulSoup(response.content, 'html.parser')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

print(TOKEN)


# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

messageWaitTime = 2


@client.event
async def on_message(message):
    author = message.author
    if message.content:
        await message.channel.send('Welcome again {}!'.format(author))


client.run(TOKEN)
