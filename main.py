from _bot import New
import asyncio

bot=New()
tok=input("Input Bot Token - ")

async def runbot():
    await bot.start(tok)
loop=asyncio.get_event_loop()

class Navigator:
    def __init__(self,bot):
        self.bot=bot
        self.guild=''
        self.guild_ins=None
        self.chan=''
        self.chan_ins=None
    
    def show_available_guilds(self):
        guilds=['Guild Name - Guild ID\n']
        guilds.extend([f"{guild.name} - {guild.id}" for guild in self.bot.guilds])
        return guilds

    def show_available_channels(self):
        if self.guild=='':
            return ''
        
        channels=['Channel Name - Channel ID']
        channels.extend([f"{channel.name} - {channel.id}" for channel in self.guild_ins.channels])
        return channels
    
    def move_guild(self,guildname):
        if " ".join(guildname) in [guild.name for guild in self.bot.guilds]:
            self.guild=guildname
            for g in self.bot.guilds:
                if g.name==" ".join(guildname):
                    self.guild_ins=g
                    break
            return True
        return False

    def move_guild_id(self,guildid):
        if guildid in [guild.id for guild in self.bot.guilds]:
            for g in self.bot.guilds:
                if g.id==guildid:
                    self.guild_ins=g
                    self.guild=g.name
                    break
            return True
        return False

    def move_chan(self,channame):
        if " ".join(channame) in [chan.name for chan in self.guild_ins.channels]:
            self.guild=channame
            for g in self.guild.channels:
                if g.name==" ".join(channame):
                    self.chan_ins=g
                    break
            return True
        return False

    def move_chan_id(self,chanid):
        if chanid in [chan.id for chan in self.guild_ins.channels]:
            for g in self.guild_ins.channels:
                if g.id==chanid:
                    self.chan_ins=g
                    self.chan=g.name
                    break
            return True
        return False

class Shell:
    def __init__(self,bot):
        self.bot=bot
        self.nav=Navigator(bot)
        print("\nShell Initialized")

    async def start(self):
        while True:
            inp=input("> ")
            inp=inp.split()

            if inp[0]=='nav':
                if self.nav.guild=='':
                    if len(inp) == 1 and self.nav.guild != '':
                        if self.channels != '':
                            self.nav.chan=''
                        else:
                            self.nav.guild=''
                        print("Navigated Back to Guilds")
                    
                    else:
                        x=self.nav.move_guild(inp[1:])
                        if x:
                            print("Moved to"," ".join(inp[1:]))
                        else:
                            print("Couldn't find Guild with Name")
                else:
                    x=self.nav.move_chan(inp[1:])
                    if x:
                        print("Moved to"," ".join(inp[1:]))
                    else:
                        print("Couldn't find Channel with Name") 

            elif inp[0]=='navid':
                if self.nav.guild=='':
                    if len(inp) == 1 and self.nav.guild != '':
                        if self.channels != '':
                            self.nav.chan=''
                        else:
                            self.nav.guild=''
                        print("Navigated Back to Guilds")
                    
                    else:
                        x=self.nav.move_guild_id(int(inp[1]))
                        if x:
                            print("Moved to"," ".join(inp[1:]))
                        else:
                            print("Couldn't find Guild with ID")  

                else:
                    x=self.nav.move_chan_id(int(inp[1]))
                    if x:
                        print("Moved to",self.nav.chan_ins.name)
                    else:
                        print("Couldn't find Channel with ID")          

            elif inp[0] == 'show':
                if inp[1].startswith('guild'):
                    print("\n".join(self.nav.show_available_guilds()))
                    print("\n -- ")
                elif inp[1] == 'channels':
                    if self.nav.guild != '':
                        print("\n".join(self.nav.show_available_channels()))
                        print("\n -- ")
                    else:
                        print("No Guild Chosen")

            elif inp[0].startswith('cur'):
                if inp[1] == 'guild':
                    print("Current Guild is"," ".join(self.nav.guild) if self.nav.guild != '' else 'None')
                elif inp[1] == 'channel':
                    print("Current Channel is"," ".join(self.nav.chan) if self.nav.chan != '' else 'None')

            elif inp[0].startswith('send'):
                if self.nav.chan != '':
                    await self.nav.chan_ins.send(" ".join(inp[1:]))
                    print("Sent Message")
                else:
                    print("No Channel Selected")

                

async def runshell():
    print("Starting Shell")
    while bot._inited==False:
        await asyncio.sleep(1)
    sh=Shell(bot)
    await sh.start()

loop.create_task(runshell())
loop.create_task(runbot())
loop.run_forever()