import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

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

@bot.command(name="insult", help="Responds with an insult to a passed name")
async def insulter(ctx, name):
    response = name + " is sad person"
    print(ctx)
    await ctx.send(response)

@bot.command(name="pounce", help="Sends message to the desired channel")
async def pounce(ctx, *args, **kwargs):
    channel = bot.get_channel(692658879972245514)
    message = ' '.join([word for word in args])
    author = ctx.message.author
    print(args, kwargs)
    await channel.send(str(message)+": pounce by "+str([y.name.lower() for y in author.roles][1:]))

@bot.event
async def on_command_error(ctx, error):
    with open('err.log', 'a') as f:
        f.write(f'Unhandled message: {error}\n')
        await ctx.send("The command was invalid. Please type `!help` for the list of available commands")

bot.run(TOKEN)
