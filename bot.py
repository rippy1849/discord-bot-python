import discord
from discord.ext import commands
import tokens




intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.guild_reactions = True


bot = commands.Bot(intents=intents)

bot.load_extension('cogs.greetings')
bot.load_extension('cogs.rippy-cog')

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

# @bot.event
# async def on_message(message: discord.Message):
#     print(message.content)


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

# bot.run(os.getenv('TOKEN')) # run the bot with the token


bot.run(tokens.TOKEN)