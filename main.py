import os
from Shell.shell import Shell
from rich.console import Console

print("""  __ \   __ ) __ __|     ___|  |     _ _| 
  |   |  __ \    |      |      |       |  
  |   |  |   |   |      |      |       |  
 ____/  ____/   _|     \____| _____| ___| 
 """)
print("-"*50)
console=Console()
console.print("Welcome to the CLI for Discord Bots, Made by Wraith#3886\nPlease Input your Bot Token to Continue",style='bold',height=5)
tok=input("> ")

if 'ultron' in os.environ:
    tok=os.environ['ultron']

sh=Shell(tok)

sh.load_shell()

sh.run_shell()
