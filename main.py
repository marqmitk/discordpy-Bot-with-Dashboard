from discord.ext import commands
import discord
import os
import threading
from dashboard.app import start_app

debug = False

DEFAULT_PREFIX = '!'
token = ''

intents = discord.Intents.all()
bot = commands.Bot(
  command_prefix='!', 
  intents=intents, 
  status=discord.Status.online,
  activity=discord.Game(f'{DEFAULT_PREFIX}help')
  )

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}#{bot.user.discriminator}')
  print('------')
  print('Loaded commands:')

  for f in os.listdir('./cogs'):
    if f.endswith('.py'):
      name = f[:-3]
      await bot.load_extension(f'cogs.{name}')

  for cog in bot.cogs:
    print(cog)
    for command in bot.get_cog(cog).get_commands():
      print('- ' + command.name)
  print('\n')

  if debug:
    start_app([bot], debug=True)
  else:
    thread = threading.Thread(target=start_app, args=([bot], ))
    thread.start()

  await bot.tree.sync()
  print('------')
bot.run(token)
