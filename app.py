# 
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import json
import time
import datetime as dt

webhookurl = ""

# Source Code
# do not Edit This
runTime = str(dt.datetime.now())
ip = ""
lastGetTime = ""

def getip():
    global ip
    global lastGetTime
    res = requests.get("http://ip-api.com/json/?fields=query")
    res = json.loads(str(res.text))
    ip = res["query"]
    lastGetTime = str(dt.datetime.now())

# [ Status Code ]
# 1 : Program is started
# 2 : IP is Not Changed
# 3 : IP is Changed
# 4 : Failed get IP

def send_webhook(statusCode):
    webhook = DiscordWebhook(url=webhookurl)
    if (statusCode == 1 or statusCode == 2):
        embed = DiscordEmbed(title='DiscordNetStatus', description='Check your Network Status!', color=0x03b2f8)
    elif (statusCode == 3):
        embed = DiscordEmbed(title='DiscordNetStatus', description='IP Address is changed!', color=0xdddd00)
    elif (statusCode == 4):
        embed = DiscordEmbed(title='DiscordNetStatus', description='Failed to Get IP!', color=0xdd3322)

    embed.set_footer(text='Made by. ParkMini')
    embed.add_embed_field(name='IP Address', value=ip)
    embed.add_embed_field(name='Run Time', value=runTime)
    embed.add_embed_field(name='Last Check Time', value=lastGetTime)
    webhook.add_embed(embed)
    response = webhook.execute()
    print(response)