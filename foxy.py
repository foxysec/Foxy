# *
# *
# * Starting....
# *
# *

from _fetch import * # Colors & FETCH
from _bug import * 
import _bug._check as bug_check


import _foxy as foxy # Foxy Module [Main]

def start_foxy():
    print(f'{ico.b_c2} Starting {color.orange}Foxy{color.reset}...')
    #print(f'{ico.b_c1} Checking for possible bugs...',end='\n')
    bug_check.run()

    foxy.run()

if __name__ == "__main__":
    os.system('clear || cls')
    start_foxy()