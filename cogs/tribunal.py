"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.2.0
"""

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

# Here we name the cog and create a new class for the cog.
class Tribunal(commands.Cog, name="tribunal"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="threshold",
        description="Sets the amount of dislikes needed to administer punishment.",
    )
    async def threshold(self, context: Context, user: discord.User) -> None:
        """
        Sets the amount of dislikes needed to administer punishment.

        :param context: The application command context.
        """
        self.bot.config['threshold']
        

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Tribunal(bot))
