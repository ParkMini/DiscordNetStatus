# http://ip-api.com/json/?fields=query
from discord_webhook import DiscordWebhook, DiscordEmbed

webhookurl = ""

webhook = DiscordWebhook(url=webhookurl)

# create embed object for webhook
embed = DiscordEmbed(title='Your Title', description='Lorem ipsum dolor sit', color='03b2f8')

# set footer
embed.set_footer(text='Embed Footer Text', icon_url='URL of icon')

# set timestamp (default is now)
embed.set_timestamp()

# add fields to embed
embed.add_embed_field(name='Field 1', value='Lorem ipsum')
embed.add_embed_field(name='Field 2', value='dolor sit')

# add embed object to webhook
webhook.add_embed(embed)
response = webhook.execute()