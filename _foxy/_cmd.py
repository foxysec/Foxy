from _fetch import *
from _bug import *
from _root import *

import os
import sys 
import time 

class config:
    # Comman Line Type : Not Selected

    ps = f'[{ico.foxy_0}] > '

    # Help Text
    _help = f"""
{ico.b_c2} Help : 
    clear          : clear cmd
    history        : show Foxy command history
    ls             : list files in current directory
    pwd            : print current directory
    cd <dir>       : open folder
    ping <host>    : ping host
    {color.red}foxy_root{color.reset}      : Be foxy_root and get acces to create rat , trojan or brute force payloads and more.
"""

    history = []

    exit_text = f"\n{ico.r_c2} Exitting from {ico.foxy_0}..."

def csystem(fxc):
    if(fxc=='foxy_root'):
        root_run() # Root Section
        time.sleep(1)
        sys.exit(0)
    elif(fxc=='root'):
        root_run() # Root Section
        time.sleep(1)
        sys.exit(0)

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
        

    return False 

def init():
    while True:
        fxc = input(config.ps)
        config.history.append(fxc)
        if(not csystem(fxc)):

            print(f"{ico.r_c0} {report.unknown_cmd(fxc)}")
        