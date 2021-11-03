from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [233958654263558146]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = None
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            intents=Intents.all(),
        )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("robot running...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("robot online")
    
    async def on_disconnect(self):
        print("robot offline")
    
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(796429389897269286)
            print("robot siap")

        else:
            print("robot reconnected")
    
    async def on_message(self, message):
        pass

bot = Bot()