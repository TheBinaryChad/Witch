import datetime
from core.formatting import *

def check_updates():
    with open('version.txt','r') as f:version = f.readline();f.close()
    info(f'Checking for updates...[Current version : {version}]')
    import requests
    try:
        ver = requests.get('https://raw.githubusercontent.com/Cryptonian007/Witch/version.txt').text
        if int(ver) > int(version):
            info(f'Update available {ver}')
        else:info('Witch is up-to-date')
    except Exception as e:
        error('Couldn\'t check for updates. Are you connected to the internet?',e)
