import discord
from discord.ext import commands
import tokens


bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

# bot.run(os.getenv('TOKEN')) # run the bot with the token


bot.run(tokens.TOKEN)