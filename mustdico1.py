import discord
import os
client = discord.Client()
@client event
async def on_ready():
    print("login")
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
