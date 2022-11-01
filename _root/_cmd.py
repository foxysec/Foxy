from _fetch import *
from _bug import *
from _root._con import payloadsystem

import os
import sys 
import time 
import json 
from tabulate import tabulate


class config:
    # Comman Line Type : Not Selected

    ps = f'[{ico.foxy_r}] > '

    # Help Text
    _help = f"""
{ico.b_c2} [Basic]: 

    clear          : clear cmd
    history        : show Foxy command history
    ls             : list files in current directory
    pwd            : print current directory
    cd <dir>       : open folder
    ping <host>    : ping host

{ico.r_c2} [Advanced]:
    list                : list avaliable payloads
    set payload <pn>    : set payload to start 
    
"""

    history = []

    exit_text = f"\n{ico.r_c2} Exitting from {ico.foxy_0}..."

def lpayloads():
    #print(pwd)
    db = ''
    with open(f'./_db/payloads.json','r') as f:
        db= json.loads(f.read())
    
    payloads = db['payloads']
    names    = db['names']
    status   = db['status']
    n = len(payloads)
    data = []
    for i in range(0,n):
        lst = []
        lst.append(f"{color.redbg}{payloads[i]}{color.reset}")
        lst.append(f"{color.white2}{names[i]}{color.reset}")
        if(status[i]=='Avaliable'):
            lst.append(f"{color.green}{status[i]}{color.reset}")
        else:
            lst.append(f"{color.red}{status[i]}{color.reset}")
        data.append(lst)
    print()
    print (tabulate(data, headers=[f"{color.red}Payload{color.reset}", f"{color.white2}Name{color.reset}", f"{color.white2}Status{color.white2}"]))
    print()
    
    

def csystem(fxc):

    fxc_os = {
        'cls'   : 'clear || cls',
        'clear' : 'clear || cls'
    }

    if(fxc in fxc_os):
        os.system(fxc_os[fxc])
        return True

    elif(fxc.startswith('ping ')):
        print()
        os.system(fxc)
        print()
        return True

    elif(fxc.startswith('cd ')):
        os.chdir(fxc.split('cd ')[1])
        return True
    # elif(fxc == '-h' or fxc =='help'):
    #     print(config._help)
    #     return True
    
    match fxc:
        case '-h' :
            print(config._help)
            return True 

        case 'help' :
            print(config._help)
            return True 

        case 'history' :
            print(config.history)
            return True 

        case 'exit' :
            print(config.exit_text)
            time.sleep(1)
            sys.exit(0)

        case 'ls' :
            os.system("ls || dir")
            return True

        case 'pwd' :
            print(os.getcwd())
            return True

        case 'foxy_payloads' :
            lpayloads()
            return True
        case 'payloads' :
            lpayloads()
            return True
        case 'list p' :
            lpayloads()
            return True
        case 'list' :
            lpayloads()
            return True
        case 'show' :
            lpayloads()
            return True
        

    return False 

def init():
    print()
    while True:
        fxc = input(config.ps)
        config.history.append(fxc)
        if(csystem(fxc)):
            pass 
        elif(payloadsystem(fxc)):
            pass
        else:
            print(f"{ico.r_c2} {report.unknown_root(fxc)}")        
