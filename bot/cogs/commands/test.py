import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def test(self, ctx):
        await ctx.respond("test")

def setup(bot):
    bot.add_cog(Test(bot))