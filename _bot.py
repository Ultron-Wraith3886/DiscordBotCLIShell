from nextcord.ext.commands import Bot

class New(Bot):
    def __init__(self,shell):
        super().__init__(command_prefix='somethingnotmemorableloremipsum')
        self._inited=False
        self.shell=shell

    async def on_ready(self):
        self._inited=True

    async def on_message(self,msg):
        if self.shell.nav.chan_ins is None:
            return 
        if msg.channel.id == self.shell.nav.chan_ins.id and self.shell.mcount>0:
            print('yes')
            self.shell.nav.history.append(msg)
            self.shell.out(f"{msg.author.display_name} : {msg.content}")