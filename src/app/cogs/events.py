import nextcord
from nextcord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("INFO: Logged in as {0.user}".format(self.bot))
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("That command does not exist.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Events(bot))