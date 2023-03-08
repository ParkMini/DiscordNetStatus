# 
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import socket
import json

webhookurl = ""
ip = ""

res = requests.get("http://ip-api.com/json/?fields=query")
res = json.loads(str(res.text))
ip = res["query"]


# webhook = DiscordWebhook(url=webhookurl)
# embed = DiscordEmbed(title='DiscordNetStatus', description='Lorem ipsum dolor sit', color=0x03b2f8)
# embed.set_footer(text='Embed Footer Text', icon_url='URL of icon')
# embed.add_embed_field(name='Field 1', value='Lorem ipsum')
# embed.add_embed_field(name='Field 2', value='dolor sit')
# webhook.add_embed(embed)
# response = webhook.execute()