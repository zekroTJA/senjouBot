import discord
import asyncio
from discord import Game, Embed, Color
from discord.ext import commands
from os import path

bot = commands.Bot(command_prefix=">", description='''Selfbot by zekro''', self_bot=True)


@bot.event
async def on_ready():
    print("Logged in as %s#%s" % (bot.user.name, bot.user.discriminator))
    print("ID: " + bot.user.id)
    

@bot.command(pass_context=True, aliases=[''])
async def test(ctx, *args):
    print(args)


@bot.command(pass_context=True, aliases=['g'])
async def game(ctx, *args):
    if args:
        txt = " ".join(args)
        await bot.change_presence(game=Game(name=txt))
        msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.green(), description="Changed game to `%s`!" % txt))
    else:
        await bot.change_presence(game=None)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.gold(), description="Disabled game display."))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)


@bot.command(pass_context=True, aliases=['em', 'e'])
async def embed(ctx, *args):
    colors = {
        "red": Color.red(),
        "green": Color.green(),
        "gold": Color.gold(),
        "orange": Color.orange(),
        "blue": Color.blue()
    }
    if args:
        argstr = " ".join(args)
        if "-c " in argstr:
            text = argstr.split("-c ")[0]
            color_str = argstr.split("-c ")[1]
            color = colors[color_str] if color_str in colors else Color.default()
        else:
            text = argstr
            color = Color.default()
        await bot.send_message(ctx.message.channel, embed=Embed(color=color, description=text))
    await bot.delete_message(ctx.message)



if path.isfile("token.txt"):
    with open("token.txt") as f:
        token = f.readline()
    bot.run(token, bot=False)
else:
    print("[ERROR] Please enter a valid account token into a file named 'token.txt'!")
    input()
    exit()

