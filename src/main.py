import discord
# this is where my token is!!!
import secerts


class Main(discord.Client):
    async def on_ready(self): 
        print(f"logged in as {self.user}")
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.lower().startswith("hello"):
            message.reply("Hello!", mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

Client = Main(intents=intents)


Client.run(secerts.token)
