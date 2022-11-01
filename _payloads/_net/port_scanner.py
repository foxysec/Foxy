from _fetch import *
from _bug import *

import os 
import socket 

class config:
    ps = f'[{ico.foxy_r}] > '
    history = []
    _continue = True
    target = ''

    _help = f"""
{ico.b_c2} [Basic]:
    clear , cls     : clear console
    history         : print console history

{ico.r_c2} [Advanced]:
    show config     : show setted informations ==> config informations  (Dont use <.> while setting informations...)
    back            : back to Foxy
    """

def print_config():
    print(f"""
___________________________________________
{ico.b_c2} Config :

    Target : {config.target}

{ico.b_c2} Set Help :

    set target:<target_ip>
___________________________________________""")

def run_exploit():
    target = config.target
    print(f"{ico.b_m} Starting port scanning for {color.blue}{target}{color.reset}.\n")
    print("\tPort\tAction\tService")
    lst = [20,21,22,23,53,25,40,44,69,80,139,137,443,444,445,4444,8080, 8443]
    for port in lst:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            check = s.connect_ex((target,port))
            if(check==0):
                version = None
                try:
                    version = socket.getservbyport(port, "tcp")
                except:
                    pass
                print(f"\t{port}\topen\t{version}")
            s.close()
        except:
            pass
            

def vparse(vname,value):
    if(vname=="target"):
        config.target = value
        print(f'target ==> {color.blue}{value}{color.reset}')

def cmd(fxc):
    fxc_os = {
        'cls'   : 'clear || cls',
        'clear' : 'clear || cls'
    }

    if(fxc in fxc_os):
        os.system(fxc_os[fxc])
        return True

    if(fxc.startswith("set target:")):
        try:
            value = fxc.split('set target:')[1]
            vname = 'target'
        except:
            return False 
        try:
            vparse(vname,value)
        except:
            return False
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
        case 'back' :
            config._continue = False

def start_port_scanner():
    config.ps = f'[{color.red}foxy::net::port-scanner{color.reset}] > '
    while(config._continue):
        fxc = input(config.ps)
        config.history.append(fxc)
        if(cmd(fxc)):
            pass
        else:
            if(fxc!='back'):
                print(f"{ico.r_c2} {report.unknown_root(fxc)}")