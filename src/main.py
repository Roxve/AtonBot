import discord
# this is where my token is!!!
import secerts

bot = discord.Bot()

@bot.event
async def on_ready(): 
     print(f"logged in as {bot.user}")

# slash commands
@bot.slash_command(name = "ping", description = "Ping!")
async def ping(ctx):
    await ctx.respond("Pong!")

@bot.slash_command(name = "bred", description = "shows you the bred")
async def bred(ctx):
    await ctx.respond("bred")

'''async def on_message(self, message):
    text = message.content.lower()
     if message.author.id == self.user.id:
         return
        
    print(f"got msg = {message.content}, by {message.author}")

     # says hello to you!
    for hello in self.hellos: 
          if text[:len(hello)] == hello:
             await message.reply("Hi!", mention_author=False)
             return'''

#intents = discord.Intents.default()
#intents.message_content = True

#Client = Main(intents=intents)

bot.run(secerts.token)
