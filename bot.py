import os
import random
import discord  
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.messages = True  # Enable the messages intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
    
@bot.command(name='strava', help='')
async def strava(ctx):
    token_url = 'https://www.strava.com/oauth/token'
    payload = {
        'client_id': os.getenv('STRAVA_CLIENT_ID'),
        'client_secret': os.getenv('STRAVA_CLIENT_SECRET'),
        'code': os.getenv('STRAVA_AUTH'),
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, data=payload)

    # Extract the access token from the response
    #access_token = response.json()['access_token']
    
    #url = "https://www.strava.com/api/v3/athlete/activities?before=1705144298&after=1673608298&per_page=30"
    #response = requests.get(url)
    await ctx.send(response.json())
    


bot.run(TOKEN)
