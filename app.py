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

def send_webhook():
    webhook = DiscordWebhook(url=webhookurl)
    embed = DiscordEmbed(title='DiscordNetStatus', description='Sucessexful Get IP!', color=0x4287f5)
    embed.set_footer(text='Made by. ParkMini')
    embed.add_embed_field(name='IP Address', value=ip, inline=False)
    embed.add_embed_field(name='Run Time', value=runTime, inline=False)
    embed.add_embed_field(name='Last Check Time', value=lastGetTime, inline=False)
    webhook.add_embed(embed)
    response = webhook.execute()

def main():
    try:
        getip()
        print(f"{dt.datetime.now()} : 아이피를 얻자")
        print(f"{dt.datetime.now()} : 아이피를 얻었다")
        print(f"{dt.datetime.now()} : 전송을 하자")
        send_webhook()
        print(f"{dt.datetime.now()} : 전송을 했다")
        print(f"{dt.datetime.now()} : 300초를 기다린다")
        time.sleep(300)
        print(f"{dt.datetime.now()} : 300초를 기다렸다")
        main()
    except:
        print("에러 발생")
        main()
main()