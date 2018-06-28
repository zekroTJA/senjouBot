import discord      # pip3 install discord.py
import asyncio
import giphypop     # pip3 install giphypop
from discord import Game, Embed, Color, Status, ChannelType
from discord.ext import commands
from os import path


# If you have an own giphy token, please use it for this bot,
# because the API creator warned that the public giphy token,
# which is used, when no token is entered, should be only used for
# testing purposes and will be determinated maybe later.
# You can get a api key here: https://github.com/Giphy/GiphyAPI
GIPHY_TOKEN = ""

# Default command prefix is set to '>', change it here if you want
PREFIX = ">"

# Add here entries for the FAQ command like following
# "key for command": [Embed(), "Description"]
FAQS = {
    "addbot": [Embed(description="[zekroBot - Get It](https://github.com/zekroTJA/DiscordBot#get-it)", color=Color.gold()), "zekroBot Get It"],
    "support": [Embed(description="[Support Guideline](https://gist.github.com/zekroTJA/ced58eb57642acc1e0c39f010e33975d)", color=Color.green()), "Support Guideline"],
    "userbots": [Embed(description="Invite with: `!invite <botID>`\n[User Bot Rules](https://gist.github.com/zekroTJA/485972bbe3b607dee7c91278577be26c)"), "User Bots"],
    "faq": [Embed(description="[zekro FAQ](https://gist.github.com/zekroTJA/75d2da53b01a4c76db27ef6befbfabf6)", color=Color.blue()), "zekro FAQ"]
}

# Here you can define which message invokes should be automatically replced
REPLACES = {
    "-lenny-": "( ͡° ͜ʖ ͡°)",
    "-meh-": "¯\_(ツ)_/¯",
    "-wut-": "ಠ_ಠ",
    "-yeah-": "(⌐■_■)",
    "-tt-": "(╯°□°）╯︵ ┻━┻",
    "-give-": "༼ つ ◕_◕ ༽つ",
}


# Creating selfbot instance
bot = commands.Bot(command_prefix=PREFIX, description='''Selfbot by zekro''', self_bot=True)


#####################
# L I S T E N E R S #
#####################

@bot.event
async def on_ready():
    """
    Printing username + discriminator and user ID
    when bot is finished logging in and ready
    """
    print(
            "\n +--------------------------------------------+"
            "\n |        senjouBot - discord self-bot        |"
            "\n | (c) 2017 Ringo Hoffman (zekro Development) |"
            "\n +--------------------------------------------+\n"
         )
    print("Logged in as %s#%s" % (bot.user.name, bot.user.discriminator))
    print("ID: " + bot.user.id)
    

@bot.event
async def on_message(msg):
    """
    Replace invokes in your message automatically with other text like emotes.
    Invokes and replacements can be defined in 'REPLACES' dict above.
    """
    if msg.author == bot.user:
        for k, v in REPLACES.items():
            if k in msg.content:
                await bot.edit_message(msg, msg.content.replace(k, v))



###################
# C O M M A N D S #
###################

@bot.command(pass_context=True)
async def test(ctx, *args):
    """
    Just a command for testing purposes and debugging
    """
    print(ctx.message.server.get_member(bot.user.id).game)


@bot.command(pass_context=True, aliases=['g'])
async def game(ctx, *args):
    """
    Command for changing 'game' status
    """
    if args:
        cstatus = ctx.message.server.get_member(bot.user.id).status
        txt = " ".join(args)
        await bot.change_presence(game=Game(name=txt), status=cstatus)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.green(), description="Changed game to `%s`!" % txt))
    else:
        await bot.change_presence(game=None, status=cstatus)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.gold(), description="Disabled game display."))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)


@bot.command(pass_context=True, aliases=['em', 'e'])
async def embed(ctx, *args):
    """
    Sending embeded messages with color (and maby later title, footer and fields)
    """
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


@bot.command(pass_context=True, aliases=['s'])
async def status(ctx, *args):
    """
    Change account status visible for others*
    *an effect of using a userbot is, that the bot displays your status as 'online'
    for other users while you can change your status to 'idle' or 'dnd', but
    noone will see it until the bot changes the status.
    """
    stati = {
        "on":       Status.online,
        "online":   Status.online,
        "off":      Status.invisible,
        "offline":  Status.invisible,
        "dnd":      Status.dnd,
        "idle":     Status.idle,
        "afk":      Status.idle
    }
    if args:
        cgame = ctx.message.server.get_member(bot.user.id).game
        if (args[0] in stati):
            if (args[0] == "afk"):
                await bot.change_presence(game=cgame, status=Status.idle, afk=True)
            else:
                await bot.change_presence(game=cgame, status=stati[args[0]], afk=False)
                print(stati[args[0]])
            msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `%s`." % args[0], color=Color.gold()))
    else:
        await bot.change_presence(game=cgame, status=Status.online, afk=False)
        msg = await bot.send_message(ctx.message.channel, embed=Embed(description="Changed current status to `online`.", color=Color.gold()))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)


@bot.command(pass_context=True)
async def faq(ctx, *args):
    """
    Thats just a verry helpful command for myself because a lot of people
    asking me always the same questions in PM, so I can answer with
    this short command easily.
    """
    if args:
        if args[0] in FAQS:
            await bot.send_message(ctx.message.channel, embed=FAQS[args[0]][0])
    else:
        cont = ""
        for k, v in FAQS.items():
            cont += "*%s*  -  `%s`\n" % (v[1], k)
        await bot.send_message(ctx.message.channel, embed=Embed(description=cont))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def gif(ctx, *args):
    """
    A simple command to send gifs by keyword from giphy api
    """
    if args:
        query = " ".join(args)
        index = 0
        if " -" in query:
            try:
                index = int(query.split(" -")[1])
            except:
                pass
            query = query.split(" -")[0]
        giphy = giphypop.Giphy() if GIPHY_TOKEN == "" else giphypop.Giphy(api_key=GIPHY_TOKEN)
        gif = [x for x in giphy.search(query)][index]
        if gif:
            await bot.send_message(ctx.message.channel, gif)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True, aliases=['server'])
async def guild(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    owner = [g.owner.name + "#" + g.owner.discriminator, g.owner.id]
    region = str(g.region)
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    tchans = str(len([c for c in g.channels if c.type == ChannelType.text]))
    vchans = str(len([c for c in g.channels if c.type == ChannelType.voice]))
    created = str(g.created_at)
    roles = ", ".join([r.name for r in g.roles])

    em = Embed(title="Guild Information")
    em.description =    "```\n" \
                        "ID:        %s\n" \
                        "Owner:     %s (%s)\n" \
                        "Region:    %s\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Channels:\n" \
                        "  Text:    %s\n" \
                        "  Voice:   %s\n" \
                        "Created:   %s\n" \
                        "Roles:\n" \
                        "%s" \
                        "```" % (gid, owner[0], owner[1], region, membs, membs_on, users, users_on, bots, bots_on, tchans, vchans, created, roles)

    await bot.send_message(ctx.message.channel, embed=em)
    await bot.delete_message(ctx.message)
        

@bot.command(pass_context=True, aliases=['google'])
async def lmgtfy(ctx, *args):
    """
    Just a simple lmgtfy command embeding the link into the message.*
    *Links are still visible because discord asks you if this link is safe :/
    """
    if args:
        url = "http://lmgtfy.com/?q=" + "+".join(args)
        await bot.send_message(ctx.message.channel, embed=Embed(description="**[Look here!](%s)**" % url, color=Color.gold()))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True, aliases=['gnick', 'gn'])
async def globalnick(ctx, *args):
    """
    With this command, you can change your nickname on all discord servers
    you are on and you have the permission to chnage your nickname.
    ATTENTION: Please don't overuse this command because I dont know,
    if it could lead to a discord account ban!
    """
    if args:
        newname = args[0]
        errors = []
        for s in bot.servers:
            await bot.edit_message(ctx.message, embed=Embed(description="Changing nickname on `%s`..." % s.name))
            try:
                await bot.change_nickname(s.get_member(bot.user.id), newname)
            except:
                errors.append(s.name)
                pass
        if errors:
            msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.red(), description="**Failed changing nickanme on following servers:**\n\n" + "\n".join(errors)))
        else:
            msg = await bot.send_message(ctx.message.channel, embed=Embed(color=Color.green(), description="Successfully changed nick on all servers!"))
    await bot.delete_message(ctx.message)
    await asyncio.sleep(3)
    await bot.delete_message(msg)


# Testing if file 'token.txt' exists. If it is so, then the token
# will be read out of this file. If not, the user will be asked
# for the token in the console to enter, wich will be saved in this
# file after and the bot will log in
if path.isfile("token.txt"):
    with open("token.txt") as f:
        token = f.readline()
    print("[INFO] Starting up and logging in...")
    bot.run(token, bot=False)
else:
    print("Please enter your discord account token (bot a bot account token!):")
    token = input()
    print("[INFO] Saving token...")
    with open("token.txt", "w") as f:
        f.write(token)
    print("[INFO] Starting up and logging in...")
    bot.run(token, bot=False)

