'''
SCRAPER.PY: Scrapes data from HTML text using regex (HREF values)
This file is a part of The Witch Project
By - github.com/Cryptonian007
22 Oct 2021 | 21:06
'''
import re,os
from urllib.parse import urlparse

def cln(lst):return[y[3:-1]for y in lst if urlparse(y).query!=''] # cleans up retrieved results

def manipulatePath(url,val):
    '''
    Manipulates the path of URL with the path supplied
    Return: manipulated URL (string)
    Args: [URL] , [PATH]
    '''
    parsed = urlparse(url)
    l = parsed.path.split('/')
    l[-1] = val
    return parsed.scheme + '://' + parsed.netloc \
    + '/'.join(l)

async def scrape(url,client):
    '''
    It scrapes HREF values from the HTML text using regex and returns
    a list of valid results (those with queries)
    if connection to the site fails it returns an empty list
    Args: [URL] , [Aiohttp CLIENT Object]
    '''
    try:
        seeds = set()
        resp = await client.get(url)
        html_data = await resp.text() # get HTML text
        #print(html_data)
        results = re.findall('''[HREF|href]=["|']\S+["|']''',html_data)
        #print(results)
        results = cln(results)
        for i in results:
            if i.startswith('http'):
                seeds.add(i)
            else:
                '''
                if site is http(s)://example.com/path convert to http(s)://example.com/path/
                if site is http(s)://example.com/path/path.php then leave it as it is
                == 
                if site is http(s)://example.com convert to http(s)://example.com/
                '''
                basename = os.path.basename(url)
                if '.' in basename or basename == '':
                    j = manipulatePath(url,i)
                else:
                    url = url + '/';j=manipulatePath(url,i)
                seeds.add(j)
        return list(seeds) # remove duplicates
    except:return []
'''
basename = os.path.basename(url)
if '.' in basename
'''
