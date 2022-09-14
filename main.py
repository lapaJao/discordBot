import discord
from discord.ext import commands

TOKEN = "yourTokenHere"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!commands"):
        await message.channel.send("!hello - Hello!\n"
                                   "!Front-end - Ganha o cargo de Front-end\n"
                                   "!Back-end - Ganha o cargo de Back-end\n"
                                   "!Full-stack - Ganha o cargo de Full-stack\n"
                                   "!Data-science - Ganha o cargo de Data-science\n")

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("!Front-end"):

        member = message.author

        var = discord.utils.get(message.guild.roles, name = "Front-end")
        await member.add_roles(var)
        await message.channel.send(f"{member} agora tem o cargo de programador {var}")

    if message.content.startswith("!Back-end"):

        member = message.author

        var = discord.utils.get(message.guild.roles, name = "Back-end")
        await member.add_roles(var)
        await message.channel.send(f"{member} agora tem o cargo de programador {var}")

    if message.content.startswith("!Full-stack"):

        member = message.author

        var = discord.utils.get(message.guild.roles, name = "Full-stack")
        await member.add_roles(var)
        await message.channel.send(f"{member} agora tem o cargo de programador {var}")

    if message.content.startswith("!Data-science"):

        member = message.author

        var = discord.utils.get(message.guild.roles, name = "Data-science")
        await member.add_roles(var)
        await message.channel.send(f"{member} agora tem o cargo de programador {var}")


client.run(TOKEN)

input()