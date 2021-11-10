import discord

class MyClient(discord.Client):
    async def on_ready(self):
         print('Logged on as {0}!'.format(self.user))

    async def on_message(self,message):
        print('Message from {0.author}: {0.content}'.format(message))
        
client = MyClient()
client.run('OTA0OTgzMjA3MTUyMzM2OTM3.YYDdSg.8xjSspawVuuzR5pmbfDIFsGYo6w')