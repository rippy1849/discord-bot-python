import discord
from discord.ext import commands
from discord.ui import Button, View

import discord.ext
from urllib.request import urlretrieve




class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked
        
    # @discord.ui.button(label="Click me2!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    # async def button_callback(self, button, interaction):
    #     await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

class MyButton(Button):
    async def callback(self, interaction: discord.Interaction):
        # await interaction.response.send_message("Hi")
        await interaction.response.edit_message(content='Hi', view=None)
        # await interaction.response.edit_message("Hi")
        await interaction.followup.send("Hi!")



class RippyCog(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command(name="brick", description="Send the brick gif") # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond('https://tenor.com/view/claum-sutherland-lick-brick-gif-11230454')

    @discord.slash_command(name="soap", description="Send the soap gif") # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond('https://tenor.com/view/soap-gay-bath-oops-gif-10322886')



    @discord.slash_command(name="button", description="Send the button") # Create a slash command
    async def button(self, ctx):
        button = MyButton(label="click me", style=discord.ButtonStyle.green)
        
        # async def button_callback(interaction: discord.Interaction):
        #     # await interaction.response.send_message("Hi")
        #     await interaction.response.edit_message(content='Hi', view=None)
        #     # await interaction.response.edit_message("Hi")
        #     await interaction.followup.send("Hi!")
        
        # button.callback = button_callback
        
        view = View()
        view.add_item(button)
        
        
        await ctx.respond("This is a button!", view=view) # Send a message with our View class that contains the button




    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User):
        
        # ctx = await client.get_context(reaction)
        
        # ctx = discord.context.ApplicationContext(discord, user)
        
        # await ctx.send("Hi")
        # discord.commands.context(reaction)
        
        channel = reaction.message.channel
        attachments = reaction.message.attachments
        
        for attachment in attachments:
            # print()
            # print()
            await attachment.save(attachment.filename)          
            # url = attachment.proxy_url
            # urlretrieve(url, './extra.jpg')
        
        # print(attatchments)
        
        
        
        await channel.send("Reacted")
        
        # ctx = await discord.get_context(Message)
        # print(reaction)
        # print(reaction.message)

        
    #Keep track of who says what?
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        print(message.content)



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(RippyCog(bot)) # add the cog to the bot