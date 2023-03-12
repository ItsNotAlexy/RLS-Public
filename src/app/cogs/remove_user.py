import nextcord
import sqlite3
from nextcord.ext import commands

class RemoveUser(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def remove(self, ctx, id:int):
        conn = sqlite3.connect('./src/api/database/auth.db')
        c = conn.cursor()
        c.execute("DELETE FROM whitelist WHERE id = ?", (id,))
        conn.commit()
        conn.close()

        SucessEmbed = nextcord.Embed(
            title="Sucessfully Removed User",
            description=f"User with ID: `{id}` has been removed to the whitelist ✅",
            color=nextcord.Color.green()
        )
        await ctx.send(embed=SucessEmbed)

def setup(bot):
    bot.add_cog(RemoveUser(bot))