import nextcord
from nextcord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        HelpEmbed = nextcord.Embed(
            title="Help",
            description="This bot is used to manage the RLS Discord server. It is currently in development, and will be updated frequently.",
            color=nextcord.Color.blue()
        )
        HelpEmbed.add_field(
            name="Commands",
            value="`add` - Adds a user to the whitelist\n`remove` - Removes a user from the whitelist\n`help` - Displays this message", 
            inline=False
        )
        HelpEmbed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.send(embed=HelpEmbed)

def setup(bot):
    bot.add_cog(Help(bot))
