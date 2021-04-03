import discord
client = discord.Client()
keywords = [ "sahil", "help", "python", "helo"]

@client.event
async def on_message(message):
    for i in range(len(keywords)):
       if keywords [i] in message.content:
          for j in range(10):
              await message.channel.send("get spammed normie")


client.run('ODI0ODgwMjM2Njg0MTE2MDMw.YF1zlQ.Ns4H9Wt9QyfFL7KH6xePf6W4rlI')              
