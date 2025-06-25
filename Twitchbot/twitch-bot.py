from twitchio.ext import commands

bot = commands.Bot(token="und79exrgtj9bhk06th2vaqt8wk1lm", prefix='!', initial_channels=['bonecollector07'])

@bot.event
async def event_ready():
    print(f'Logged in as:{bot.nick}')  # Twitch bot account

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

bot.run()