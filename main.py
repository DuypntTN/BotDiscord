import asyncio
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

TOKEN = os.environ['DISCORD_TOKEN']
PREFIX = '+'

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.remove_command('help')

# Ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# Load Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# On Ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}')
    print(f'ID: {bot.user.id}')
    print(f'Prefix: {PREFIX}')
    print(f'Guilds: {len(bot.guilds)}')
    print(f'Users: {len(bot.users)}')
    print(f'Commands: {len(bot.commands)}')
    print('------')

# Shutdown
@bot.command()
async def shutdown(ctx, time: int):
    await ctx.send(f'Shutting down in {time} minutes.')
    await asyncio.sleep(time * 60)
    await ctx.send('Shutting down now.')
    # Execute the shutdown command
    # os.system('shutdown /s /t 0')

# Check time left before shutdown
@bot.command()
async def timeleft(ctx):
    await ctx.send('Checking time left...')
    # Execute the time left command
    os.system('shutdown /a')

# Run Bot
bot.run(TOKEN)