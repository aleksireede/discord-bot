#!/usr/bin/env python3
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Replace 'YOUR_BOT_TOKEN' with the token you obtained from the Discord Developer Portal
TOKEN = os.getenv("token")
guild = os.getenv("GUILDS")
allowed_content_types = [
    "image/jpeg",
    "image/png",
]

# Create an instance of the bot with the required intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

bot = commands.Bot()
@bot.slash_command(name="mc_server",description="Show the Minecraft server ip address", guild_ids=[guild]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def mc_server(ctx): 
    await ctx.respond("Minecraft Server: mc.mehukattiserver.cc")
# Start the bot

@bot.slash_command(name="add_private_emoji",description="Create Custom emoji",guild_ids=[guild])
async def add_private_emoji(
    ctx,
    name: discord.Option(str),
    image: discord.Option(discord.Attachment),
    role: discord.Option(discord.Role),
):
    if image.content_type not in allowed_content_types:
        return await ctx.respond("Invalid attachment type!", ephemeral=True)

    image_file = await image.read()  # Reading attachment's content to get bytes

    await ctx.guild.create_custom_emoji(
        name=name, image=image_file, roles=[role]
    )  # Image argument only takes bytes!
    await ctx.respond(content="Private emoji is successfully created!")

bot.run(TOKEN)

