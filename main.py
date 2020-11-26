import discord, os
os.system('clear')

intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)



@client.event
async def on_message(message):
    if client.user.mention in message.content.split():
        await message.channel.send('meow')