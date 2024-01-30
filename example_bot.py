import discord
import config
import logging
import requests
import json

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_quote():
    response = requests.get
    ("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = f"{json_data[0]['q']} - {json_data[0]['a']}"
    return(quote)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

client.run(config.altr_token, log_handler=handler, log_level=logging.DEBUG)