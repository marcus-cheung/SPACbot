import discord
import os
import SEC425
import RedditMerge as rm
import googlescrape as gs
import ssl
from tableMaker import update


client = discord.Client()


@client.event
async def on_ready():
    # specify notification channel
    SECchannel = client.get_channel(812966548657668127)
    Redditchannel = client.get_channel(812966670808514600)
    Newschannel = client.get_channel(813194561194688523)
    Logschannel = client.get_channel(812966799964110858)
    print("Ready")
    await Logschannel.send("```css\nReady and intialized\n```")

    # driver
    while True:
        # check for update
        if update():
            # updates SEC ticker list
            await Logschannel.send("```Updating SEC```")
            SEC425.update()
            await Logschannel.send("```SEC updated```")
            # updates gs ticker list and reinitalizes latest list of titles
            #await Logschannel.send("```Updating GS```")
            #gs.update()
            #await Logschannel.send("```GS updated```")

        # checking SEC
        await Logschannel.send("```Checking SEC```")
        SECmessage = SEC425.msg425()
        if SECmessage != "":
            await SECchannel.send(SECmessage)
            await SECchannel.send("/tts SEC425 Filed")

        # checking Reddit
        await Logschannel.send("```Checking Reddit```")
        msgDA = rm.RedditDA()
        if msgDA != "":
            await Redditchannel.send(msgDA)

        # checking google scraper
        #await Logschannel.send("```Checking News```")
        #gsmsg = str(gs.scrape())
        #if gsmsg != "@here" and gsmsg.find("function scrape") < 0:
            #await Newschannel.send(gsmsg)


TOKEN = "ODEwNzIzNTk4NTU2NzI1MjQ4.YCnzMA.PfUYNbBdgDybBguBfySjabKTsf0"
client.run(TOKEN)

NewToken = "ODEwNzIzNTk4NTU2NzI1MjQ4.YCnzMA.CmFScdfmfQ1J09Haa8QzTJkxhDU"