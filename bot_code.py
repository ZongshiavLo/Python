from email.mime import message

import discord
import requests
import json


def get_meme(subreddit):
  response = requests.get(f"https://meme-api.com/gimme/{subreddit}")
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  
  async def on_message(self, message):
    # Ignore messages sent by the bot itself
    if message.author == self.user:
        return

    if message.content.startswith("$meme"):
      parts = message.content.split()

      if len(parts) > 1:
          subreddit = parts[1]
      else:
          subreddit = "memes"

      await message.channel.send(get_meme(subreddit))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("token") 