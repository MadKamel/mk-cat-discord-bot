import discord, os, random
os.system('clear')

token = os.getenv('token')
client = discord.Client()

meows = ["miaow", "*purrr*", "mrrow"]

meows2 = ["*purrrr* *purrrr*", "miaow!", "mrrrow!"]

shut = ["shut", "quiet", "stop"]

happy = False

friends_list = [433433822248304641]

@client.event
async def on_message(msg):
  global happy
  if not client.user.id == msg.author.id:
    print('\nINCOMING:===============\n@ ' + msg.author.name + '\n# ' + msg.channel.name + '\n= ' + msg.content + '\n========================\n')
    if msg.content == '<@!' + str(client.user.id) + '>':
      happy = True
      await msg.channel.send(random.choice(meows))
  
    else:
      for i in range(len(shut)):
        if shut[i] in msg.content.split(' '):
          happy = False
    
      if happy:
        if msg.author.id in friends_list:
          await msg.channel.send(random.choice(meows + meows2))
        else:
          await msg.channel.send(random.choice(meows))


print("MK's Cat Online.")
client.run(token)