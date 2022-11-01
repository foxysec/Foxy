from _fetch import *
import _bug._check as bug_check
from _root._cmd import init 
import time 
import json


def root_run():
    print(f'{ico.r_c2} Starting {color.red}Foxy Root{color.reset}...')
    bug_check.run()
    init()