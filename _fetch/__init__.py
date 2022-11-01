"""
Colors & FETCH Module
"""


class color:
    orange      =  "\033[38;5;214m" 
    black       = '\033[30m'
    red         = '\033[31m'
    redbg       = '\33[41m'
    green       = '\033[32m'
    yellow      = '\033[33m'
    blue        = '\033[34m'
    magenta     = '\033[35m'
    cyan        = '\033[36m'
    white       = '\033[37m'
    white2      = '\33[97m'
    underline   = '\033[4m'
    reset       = '\033[0m'

class ico:

    foxy_0 = color.orange+'Foxy'+color.reset # Normal Foxy 
    foxy_r = color.red+'Foxy'+color.reset # Root Foxy 

    
    # Blue (No Error) 
    b_c0  = color.green+'◉'+color.reset # Blue Un Empty Circle
    b_c1  = color.green+'○'+color.reset # Blue Empty Circle
    b_c2  = color.green+'●'+color.reset # Blue Full Circle


    # Red (Error)
    r_c0  = color.red+'◉'+color.reset # Red Un Empty Circle
    r_c1  = color.red+'○'+color.reset # Red Empty Circle
    r_c2  = color.red+'●'+color.reset # Red Full Circle
