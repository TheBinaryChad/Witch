'''
CRAWLER.PY : crawls a site with a specified depth and grabs URLs with parameters
This file is a part of The Witch Project
By- github.com/Cryptonian007
'''
from scraper import *
from urllib.parse import urlparse
import asyncio,aiohttp

grabbed = set() # URLs grabbed
visited = set() # URLs visited

async def crawl_single(site,client):
	'''
	Crawls a single URL
	Generates root URL and crawls
	Crawls given URL if its not the same as root URL
	Adds to set to avoid duplicates
	Args: [URL] [aiohttp CLIENT object]
	'''
	parsed = urlparse(site)
	root_url = parsed.scheme + '://' + parsed.netloc + '/' # get root URL
	if root_url not in visited:
		res = await scrape(root_url,client)
		for x in res:grabbed.add(x)
		visited.add(root_url)
	if site not in visited:
		if site != root_url: #TODO: improve conditional statement
			#print('NOT THE SAME')
			res = await scrape(site,client)
			for x in res:grabbed.add(x)
			visited.add(site)

async def crawl_multi(urllist):
	# intuitive
	async with aiohttp.ClientSession() as session:
		tasks = []
		for u in urllist:
			task = asyncio.create_task(crawl_single(u,session))
			tasks.append(task)
		await asyncio.gather(*tasks)

def crawlSite(urllist,depth=1): # max depth: 4
	'''
	Crawls with specified depth
	Args: [URL(s)] [DEPTH (default=1)]
	Return: list(grabbed URLs)
	'''
	asyncio.run(crawl_multi(urllist))
	if grabbed != set():
		for _ in range(depth):
			asyncio.run(crawl_multi(grabbed))
	return list(grabbed)

