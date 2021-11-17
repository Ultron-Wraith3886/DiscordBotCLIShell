from Shell.navigator import Navigator
from rich.console import Console
from asyncio import sleep,get_event_loop,all_tasks
from os import system

from _bot import New


class Shell:
    def __init__(self,token,_loader_chars=['-','\\','|','/'],_loader_tasks:list=[]):
        self.token=token
        self.loop=get_event_loop()
        self.bot=New(self)
        self.nav=Navigator(self.bot)
        self.ld_t=_loader_tasks
        self.ld_c=_loader_chars

        self.loaded=False

        self.console=Console()
        self.mcount=0
        self.takeinp = True

    def load_shell(self):
        self.loop.run_until_complete(self.load())

    def run_shell(self):
        self.loop.create_task(self.start())
        self.loop.run_forever()

    def out(self,item):

        print(item)
        self.counter-=1
        if self.counter <= 0:
            self.takeinp=True

    async def add_task(self,task:str='None'):
        self.ld_t.append(task)

    async def remove_task(self):
        task=self.ld_t.pop(0)
        print(task)
        self.console.log(f"{task}Completed")
        if len(self.ld_t)==0:
            self.loaded=True

    async def connect_loop(self):
        await self.bot.start(self.token)

    async def load(self):
        with self.console.status("[bold blue]Creating Shell ",spinner='aesthetic') as status:
            self.console.log("[bold blue]Getting Ready")
            await sleep(1.69)
            status.update("[bold blue]Creating Bot Instance ",spinner='aesthetic',speed=2)
            self.console.log("[bold blue]Connecting to Discord API...")
            await sleep(1)
            self.loop.create_task(self.connect_loop())
            self.console.log("[bold green]Connected to the Discord API")
            await sleep(1)
            self.console.log("[bold blue]Generating Resources...")
            while not self.bot._inited:
                await sleep(1)
            self.console.log('[bold green]Resources Ready')
            status.update("[bold blue overline]Discord-Bot-CLI-Shell Initiated",spinner='arc',speed=0.1)
            self.loaded=True
            await sleep(2)

    async def start(self):
        while True:
            if not self.takeinp:
                continue
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

            elif inp[0].startswith('msghis'):
                if self.nav.chan == '':
                    print("You haven't navigated to a Channel yet")
                else:
                    print("\n")
                    print("\n".join([f"{msg.author.display_name} : {msg.content}" for msg in await self.nav.show_history(int(inp[1]) if len(inp)>1 else 7)]))
                    print("\n")

            elif inp[0].startswith('livechat'):
                if self.nav.chan == '':
                    print("You haven't navigated to a channel yet")
                else:
                    print("\n")
                    limit=inp[1] if len(inp)>1 else 10
                    print("Showing Live Chat till",limit,"Messages")
                    self.mcount=limit
                    self.takeinp=False

            elif inp[0].startswith('clear'):
                system('cls')
                system('clear')

            elif inp[0].startswith('close'):
                break
