import nextcord
import sqlite3
from nextcord.ext import commands

class AddUser(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, id:int):
        conn = sqlite3.connect('./src/api/database/auth.db')
        c = conn.cursor()
        c.execute("INSERT INTO whitelist VALUES (?)", (id,))
        conn.commit()
        conn.close()

        SucessEmbed = nextcord.Embed(
            title="Sucessfully Added User",
            description=f"User with ID: `{id}` has been added to the whitelist ✅",
            color=nextcord.Color.green()
        )
        await ctx.send(embed=SucessEmbed)

def setup(bot):
    bot.add_cog(AddUser(bot))
        