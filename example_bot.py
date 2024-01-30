import discord
import config
import logging
import requests
import json
from discord.ext import commands
import random

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents, command_prefix='$')
bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    await bot.load_extension('inspire')
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if random.randint(1,10) == 5:
        await message.channel.send(f"{message.author} got that dawg in me")
    await bot.process_commands(message)    


@bot.command()
async def reload(ctx):
    await bot.reload_extension('inspire')

bot.run(config.altr_token, log_handler=handler, log_level=logging.DEBUG)

