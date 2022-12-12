'''
This python file is a part of The Witch Project
Version - 1.01
[Cryptonian007 | 10/16/2021, 20:07]
'''
from colorama import Fore, Style
import datetime

'''
[  VULN   ]
[   OK    ]
[  ERROR  ]
[  INFO   ]
[  WARN   ]
[    -    ]
'''
def vuln(text):
    attr = Fore.MAGNETA + Style.BRIGHT +"VULN" + Style.RESET_ALL + Fore.RESET
    print(f'[  {attr}   ] {text}')
def ok(text):
    attr = Fore.GREEN + Style.BRIGHT +"OK" + Style.RESET_ALL +Fore.RESET
    print(f'[   {attr}    ] {text}')
def error(text,exp=None):
    if exp != None:log_error(exp)
    attr = Fore.RED + Style.BRIGHT +"ERROR" + Style.RESET_ALL +Fore.RESET
    print(f'[  {attr}  ] {text}')
def info(text):
    attr = Fore.CYAN + Style.BRIGHT +"INFO" + Style.RESET_ALL +Fore.RESET
    print(f'[  {attr}   ] {text}')
def warn(text):
    attr = Fore.YELLOW + Style.BRIGHT + "WARN" + Style.RESET_ALL + Fore.RESET
    print(f'[  {attr}   ] {text}')
def minus(text):
    attr = Fore.YELLOW + Style.BRIGHT + "-" + Style.RESET_ALL + Fore.RESET
    print(f'[    {attr}    ] {text}')
def plus(text):
    attr = Fore.CYAN + Style.BRIGHT + "+" + Style.RESET_ALL + Fore.RESET
    print(f'[    {attr}    ] {text}')

def logo():
    print(Style.BRIGHT + Fore.RED +
    f'''
___ __ _____________________________
7  V  V  77  77      77     77  7  7
|  |  |  ||  |!__  __!|  ___!|  !  |
|  !  !  ||  |  7  7  |  7___|     |
|        ||  |  |  |  |     7|  7  |
!________!!__!  !__!  !_____!!__!__! {Fore.YELLOW}

           Version : 1.01  
'''
    + Fore.RESET + Style.RESET_ALL)

def log_error(err):
    val = cur_time()
    with open(f'CrashLogs.txt', 'a') as f:
        f.write(f'[{val}] ERROR\n')
        f.write(str(err) + '\n')
        f.write('======\n')

def cur_time():
    return datetime.datetime.now().strftime("%H:%M:%S")