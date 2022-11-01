from _fetch import *
from _bug import *

def run():
    if(not check.internet()):
        print(f'{ico.r_c2} {report.internet()}')
    
    elif(not check.check_os()):
        print(f'{ico.r_c2} {report.os()}')