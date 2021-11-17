
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