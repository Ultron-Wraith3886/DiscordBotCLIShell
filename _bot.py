from nextcord.ext.commands import Bot

class New(Bot):
    def __init__(self):
        super().__init__(command_prefix='somethingnotmemorableloremipsum')
        self._inited=False

    async def on_ready(self):
        self._inited=True


    