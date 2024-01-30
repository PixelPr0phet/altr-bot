import requests
import json

from discord.ext import commands

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = response.json()
    quote = f"{json_data[0]['q']} - {json_data[0]['a']}"
    return quote

@commands.command()
async def inspire(ctx):
    await ctx.send(get_quote())

@commands.command()
async def lol(ctx, name=None):
    message = "some bullshit message"
    if name:
        message = f"lol @ {name}"
    await ctx.send(message)

async def setup(bot):
    bot.add_command(inspire)
    bot.add_command(lol)
