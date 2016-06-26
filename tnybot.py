import configparser

from discord.ext import commands
from discord.ext.commands import Bot
from cogs import Commands, CustomCommands, Notifications


class TnyBot(Bot):
    def __init__(self, command_prefix, formatter=None, description=None, pm_help=False, **options):
        super().__init__(command_prefix, formatter, description, pm_help, **options)

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message):
        name = self.trim_prefix(message, message.content.split()[0])
        if name in self.commands.keys():
            await self.process_commands(message)

    def is_prefixed(self, message, part):
        prefixes = self._get_prefix(message)
        for p in prefixes:
            if part.startswith(p):
                return True

    def trim_prefix(self, message, part):
        prefixes = self._get_prefix(message)
        for p in prefixes:
            part = part.strip(p)
        return part


description = """An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here."""

bot = TnyBot(command_prefix=commands.when_mentioned_or("%"), description=description)

config = configparser.RawConfigParser()
config.read("../tnybot_config")

bot.add_cog(Commands(bot))
bot.add_cog(CustomCommands(bot))
bot.add_cog(Notifications(bot))
bot.run(config["User2"]["user"], config["User2"]["pass"])
