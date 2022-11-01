from _fetch import *
from _bug import *

from discord_webhook import DiscordWebhook

import os 

class config:
    ps = f'[{ico.foxy_r}] > '
    history = []

    webhook = ''
    amount  = 0
    message = ''

    _help = f"""
{ico.b_c2} [Basic]:
    clear , cls     : clear console
    history         : print console history

{ico.r_c2} [Advanced]:
    show config     : show setted informations ==> config informations  (Dont use <.> while setting informations...)
    """

def print_config():
    print(f"""
___________________________________________
{ico.b_c2} Config :

    Webhook URL : {config.webhook}
    Amount      : {config.amount}
    Message     : {config.message}

{ico.b_c2} Set Help :

    set webhook:<webhookurl>
    set amount:<amount>
    set message:<spam message>

___________________________________________""")

def run_exploit():
    n = config.amount
    webhook = DiscordWebhook(url=config.webhook, content=config.message)
    while(n>0):
        response = webhook.execute()
        n-=1

def vparse(vname,value):
    if(vname=="webhook"):
        config.webhook = value
        print(f'webhook ==> {color.blue}{value}{color.reset}')
    elif(vname=="amount"):
        config.amount = int(value)
        print(f'amount ==> {color.blue}{int(value)}{color.reset}')
    elif(vname=="message"):
        config.message = value
        print(f'message ==> {color.blue}{value}{color.reset}')

def cmd(fxc):
    fxc_os = {
        'cls'   : 'clear || cls',
        'clear' : 'clear || cls'
    }

    if(fxc in fxc_os):
        os.system(fxc_os[fxc])
        return True

    if(fxc.startswith("set webhook:") or fxc.startswith('set amount:') or fxc.startswith('set message:')):
        if(fxc.startswith("set webhook:")):
            try:
                value = fxc.split('set webhook:')[1]
                vname = 'webhook'
            except: return False 
            try:vparse(vname,value)
            except: return False
            return True
        elif(fxc.startswith("set amount:")):
            try:
                value = fxc.split('set amount:')[1]
                vname = 'amount'
            except: return False 
            try:vparse(vname,value)
            except: return False
            return True
        elif(fxc.startswith("set message:")):
            try:
                value = fxc.split('set message:')[1]
                vname = 'message'
            except: return False 
            try:vparse(vname,value)
            except: return False
            return True



    match fxc:
        case 'history' :
            print(config.history)
            return True 
        case 'show config' :
            print_config()
            return True 
        case 'help' :
            print(config._help)
            return True 
        case 'run':
            run_exploit()
            return True
        case 'exploit':
            run_exploit()
            return True

def start_webhook_spammer():
    config.ps = f'[{color.red}foxy::discord::webhook-spammer{color.reset}] > '
    while True:
        fxc = input(config.ps)
        config.history.append(fxc)
        if(cmd(fxc)):
            pass
        else:
            print(f"{ico.r_c2} {report.unknown_root(fxc)}")