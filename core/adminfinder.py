'''
ADMINFINDER.PY : Used to find possible admin panels of a site by concentating suffixes to the
base URL one by one. Uses asyncio.
This file is a part of the Witch Project
By Cryptonian007 [24|11|21::08:43]
'''

from core.formatting import *
from urllib.parse import urlparse
import asyncio,aiohttp,sys
#import progressbar

ok_sites = []
failed = 0
total = 0

def check_suffixes(lst):
    # yeah ik it's stupid
    lol = []
    for i in lst:
        if i[0] == '/':lol.append(i)
        else:lol.append('/'+i)
    return lol

async def check(url,suffix,client,boolean):
    global failed
    # checks the HTTP response (if site is good or bad)
    if boolean:
        if url.endswith('/'):
            url = url[0:-1]
            nurl = url + suffix
        else:
            nurl = url + suffix
    else:nurl = urlparse(url).scheme + '://' + urlparse(url).netloc + suffix
    try:
        resp = await client.get(nurl)
        code = resp.status
        if code == 200:
            ok(nurl)
            ok_sites.append(nurl)
        else:failed += 1;minus(f'{nurl}')
    except:failed += 1;minus(f'{nurl}')

async def check_urllist(url,suffixes,boolean):
    # intuitive
    global total
    async with aiohttp.ClientSession() as session:
        tasks = []
        for suffix in suffixes:
            total += 1
            task = asyncio.create_task(check(url,suffix,session,boolean))
            tasks.append(task)
        await asyncio.gather(*tasks)

def adminFinder(url,suffixfile,boolean):
    # main function
    try:
        f = open(suffixfile)
        lst = f.read().splitlines()
        new_lst = check_suffixes(lst)
        asyncio.new_event_loop().run_until_complete(check_urllist(url,new_lst,boolean))
    except Exception as e:
        error(f'Exception! [{e}]')
    return ok_sites,total,failed
