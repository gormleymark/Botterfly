import os
import random
import discord  
import requests
import json
from discord.ext import commands
from db_connector import DatabaseConnector

db = DatabaseConnector()

TOKEN = db.GetDiscordToken()

intents = discord.Intents.all()
intents.messages = True  # Enable the messages intent

bot = commands.Bot(command_prefix='!', intents=intents)

##
api_url = "http://192.168.1.101:7184/api/bot/data"  # Update the URL with your actual endpoint
access_token = "test"  # Include any necessary data in the payload

# Define the data to send
bot_data = {
    "AccessToken": access_token,
    # Add other data fields as needed
}

# Send a POST request to the C# API endpoint
response = requests.post(api_url, json=bot_data)

# Check the response
if response.status_code == 200:
    print("Data sent successfully")
else:
    print(f"Error: {response.status_code}, {response.text}")
##

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
    
    # this is to get access token (expires every 6 hrs) and refresh token (to get new access token)
    # need to authenticate first to get STRAVA_CODE
    token_url = 'https://www.strava.com/oauth/token'
    payload = {
        'client_id': os.getenv('STRAVA_CLIENT_ID'),
        'client_secret': os.getenv('STRAVA_CLIENT_SECRET'),
        'code': os.getenv('STRAVA_CODE'),
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, data=payload)

    # Extract the access token from the response
    # access token required for all requests
    #access_token = response.json()['access_token']
    
    #url = "https://www.strava.com/api/v3/athlete/activities?before=1705144298&after=1673608298&per_page=30"
    #response = requests.get(url)
    await ctx.send(response.json())
    


bot.run(TOKEN)
