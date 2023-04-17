import discord
from discord.ext import commands

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_prefix = '!'
        self.my_data = {}

        @self.event
        async def on_ready():
            print(f'Logged in as {self.user.name} ({self.user.id})')

        @self.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.command_prefix):
                await self.process_commands(message)

    def add_data(self, key, value):
        self.my_data[key] = value

    def get_data(self, key):
        return self.my_data.get(key)

client = MyClient()

def setup(bot: commands.Bot):
    bot.add_cog(MyCog(bot))

class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def my_command(self, ctx: commands.Context):
        await ctx.send(f'The prefix is {self.bot.command_prefix}')
