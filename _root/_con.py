from _fetch import *
import json 

from _payloads import discord
from _payloads import network
from _payloads import getpayload_script

def getdb():

    db = ''
    with open(f'./_db/payloads.json','r') as f:
        db= json.loads(f.read())
    
    return db

class config:
    payloads = getdb()['payloads']
    names    = getdb()['names']
    platform = getdb()['platform']


            

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