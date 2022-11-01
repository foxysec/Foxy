from discord_webhook import DiscordWebhook

def run_exploit(webhook,n,message):
    webhook = DiscordWebhook(url=webhook, content=message)
    while(n>0):
        response = webhook.execute()
        n-=1