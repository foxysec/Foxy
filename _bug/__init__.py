from urllib.request import urlopen

import os 
import sys

from _fetch import color,ico 

class check_config:
    internet = 'https://google.com/'
    
class check:
    def internet(): # Testing Internet connection....
        try:
            urlopen(check_config.internet)
        except:
            return False
        return True 

    def check_os():
        if('windows' not in sys.platform):
            return True
        return False

class report:
    def internet():
        return f'Error occured while connecting to internet...'

    def os():
        return f'{color.orange}Foxy{color.reset} can only be run on Linux or Mac OSx operating systems...'

    
    def unknown_cmd(fxc):
        return f"Bad Command : '{color.red}{fxc}{color.reset}' . Type help to get help."

    def unknown_root(fxc):
        return f"Bad Command : '{color.red}{fxc}{color.reset}' . Help for commands : help"