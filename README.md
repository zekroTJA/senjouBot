# senjouBot - a python discord self-bot

### DISCLAIMER
If you decide to use this bot on your own Discord account(s), I will not be liable if your accounts are getting banned! Written in the Discord API TOS, self bot's are not allowed and, if they get detected, you will get banned!  

*"[...] Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is 
forbidden, and can result in an account termination if found."* *- quote [Discord Bots TOS](https://discordapp.com/developers/docs/topics/oauth2#bot-vs-user-accounts)*

---

### PLEASE READ BEFORE USAGE

If you want to use this bot or the code of it in any way in your own projects, please read this before:
**[zekro Open Source Code Policy](https://gist.github.com/zekroTJA/adbce830d6c876661cb7d7244ecb19b8)**

---

### DESCRIPTION

This is a little Discord self-bot I'm currenty working on. It will not have so much functions, just little things like sending gifs, creating embed messages, changing game and status and such stuff.

---
### CURRENT FEATURES  
*{this is an argument} - ({this is an optional argument}) - {these|are|valid|argument|options}*

- **game**  
`>game ({string})`  
With this command you can change the displayed game *(`Playing...`)*.  
*Enter no argument to disbale game display.*

- **embed**  
`>embed {message} ({-c red|green|blue|gold|orange})`  
Sending colored embed messages, maby later with title and fields.  
![img](http://zekro.de/ss/Discord_2017-10-19_21-57-40.jpg)

- **status**  
`>status ({on|online|off|offline|dnd|idle|afk})`  
Set status which is displayed to others. A little side effect of a selfbot is, that other users could see a other status then you set, because only the status of the bot will be displayd to other users. So you can set your status to 'dnd' or 'idlde', but everyone else could see you as 'online', because only the bots status is displayed to others.  
*Set no argument to set your status to 'online'.*

- **faq**  
`>faq ({question link})`  
That's just a little command for myself, because I'm getting a lot of questions which are often the same, so I can easily answer with links or something like that with a bot command instead of searching for it again and again.  
Maybe later, I will implement a function, that you can set your links with the message into a config file to set links outside of the bot's code.  
*Enter no argument to list all links.*

- **gif**  
`>gif {search query} ({-0|1|2|...})`  
Just a simple gif command to send gifs from keywords *(and index of search result with attaching `-1` or some other index)* with giphy API.  
If you have your own giphy API token, please open `main.py` and enter at `GIPHY_TOKEN` your giphy API token.

- **guild**  
`>guild`  
Getting various stats and information about current guild. 
**ATTENTION:** Please only use this command on your own guilds or woth explicit permission of the guilds administrators or owners!  
Exactly information:
  - ID
  - Owner (Name, ID)
  - Region
  - Members (Users, Online Users, Bots, Online Bots)
  - Channels (Textchannels, Voicechannels)
  - Created at - date
  - Rolenames

- **lmgtfy**  
`>lmgtfy {your search query}`  
A command to create easy embeded [let me google that for you](http://lmgtfy.com/) links.

---
### SETUP

Just clone or download that repository somewhere on your PC or server.

For this bot, you need to install following python packages:
- [discord.py](https://github.com/Rapptz/discord.py) (`pip3 install discord.py`)
- [giphypop](https://github.com/shaunduncan/giphypop) (`pip3 install giphypop`)

**For Windows:**  
1. Check if you have installed python **3.5+**, when not, install it from [python.org](http://python.org)
2. Open the containing folder.
3. Double-click the batch file `start.bat`
4. Enter your discord **account** token (**not** a bot account token!)  
*If you don't know how to get your private account token, take a look below.*

**For Linux / Debian / ...**  
1. Navigate via terminal or SSH to the containing directory
2. Check if you have installed python **3.5+**, if not, enter  
`$ sudo apt-get install python3`  *or use that packet manager which is installed on your system*
2. If you have not installed screen app, please do this with  
`$ sudo apt-get install screen`  *or use that packet manager which is installed on your system*
3. Start the start script with `$ sh start.sh`
4. Enter your discord **account** token (**not** a bot account token!)  
*If you don't know how to get your private account token, take a look below.*

---
### GETTING PRIVATE ACCOUNT TOKEN

1. Open your desktop discord client
2. Press `[STRG]` + `[SHIFT]` + `[I]` to open developer tools
3. Navigate to tab `Application`
4. Click on the left side on `Local Storage` -> `https://discordapp.com`
5. In the table, search for the key `token` and copy your token
