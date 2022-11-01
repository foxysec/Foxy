from _fetch import *
import json 

from _payloads import discord
from _payloads import network
def getdb():

    db = ''
    with open(f'./_db/payloads.json','r') as f:
        db= json.loads(f.read())
    
    return db

class config:
    payloads = getdb()['payloads']
    names    = getdb()['names']
    status   = getdb()['status']


def getpayload_script(payloadname):
    match payloadname :
        case 'foxy::discord::webhook-spammer':
            return discord.webhook_spammer()
    match payloadname :
        case 'foxy::net::port-scanner':
            return network.port_scanner()
            

def fastcontrol(payloadname):
    if(payloadname in config.payloads):
        return payloadname
    else:
        return False

def payloadsystem(fxc):
    if(fxc.startswith("set payload")):
        payloadname = fxc.split('set payload')[1].split()[0]
        if(not payloadname):
            return False 
        else:
            getpayload_script(payloadname)
            return True