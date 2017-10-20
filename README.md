# senjouBot - a python discord self-bot

### DISCLAIMER
If you decide to use this bot on your own Discord account(s), I will not be liable if your accounts are getting banned! Written in the Discord API TOS, self bot's are not allowed and, if they get detected, you will get banned!  

*"[...] Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is 
forbidden, and can result in an account termination if found."* *- quote [Discord Bots TOS](https://discordapp.com/developers/docs/topics/oauth2#bot-vs-user-accounts)*

---
### DESCRIPTION

This is a little Discord self-bot I'm currenty working on. It will not have so much functions, just little things like sending gifs, creating embed messages, changing game and status and such stuff.

---
### CURRENT FEATURES  
*{this is an argument} - ({this is an optional argument}) - {these|are|valid|argument|options}*

- **game**  
`>game ({string})`  
With this command you can change the displayed game *(`Playing...`)*.  
Enter no argument to disbale game display.

- **embed**  
`>embed {message} ({-c red|green|blue|gold|orange})`  
Sending colored embed messages, maby later with title and fields.  
![img](http://zekro.de/ss/Discord_2017-10-19_21-57-40.jpg)

- **status**  
`>status ({on|online|off|offline|dnd|idle|afk})`  
Set status wich is displayed to others. A little side effect of a selfbot is, that other users could see a other status then you set, because only the status of the bot will be displayd to other users. So you can set your status to 'dnd' or 'idlde', but everyone else could see you as 'online', because only the bots status is displayed to others.  
Set no argument to set your status to 'online'.
