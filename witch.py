''''
This file is a part of the Witch Project
'''

from core.formatting import *
from core.utilities import *
import argparse, time,os
from colorama import init
from urllib.parse import urlparse

init()

'''TODO:
During targeted scanning, the user will receive CLI prompts for
subdomain, robots and form scanning
subdomain
then robots
then forms

then reverse-domain (if supplied)
then admin-panel (if supplied)
'''

def targetedScan(url):
	if urlparse(url).query != '':
		info('Checking for SQLi vulnerability in this site...')
		#scan
		choice = input('Crawl site and get more URLs?[y/n]: ')
		if 'y' in choice:pass
			#crawl
		choice = input('Would you like Witch to scan for subdomains?[y/n]: ')
		if 'y' in choice:pass
			#scan
		info('Scanning for robots.txt and sitemap.xml')
		#scan
		choice = input('Crawl these sites for URLs?[y/n]: ')
		if 'y' in choice: pass
		info('Checking for availability of forms...')
		#scan

def Quit():
	print('');info(f'Exiting at {cur_time()}');quit()

def main():
	logo()

	info(f'Starting Witch at {cur_time()}\n')

	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', type=str,help="Supply a URL for targeted scanning")
	parser.add_argument('-c','--depth',help="Set crawler depth [Default: 1][Works with -u flag]", default=1)
	parser.add_argument('-r', '--reverse-domain',action='store_true', help="Reverse domain a site[Works with -u flag]")
	parser.add_argument('-a', '--admin-panel', help="Find admin panel of a site")
	parser.add_argument('-s','--suffix-file',help='The file containing paths for URL [For -a tag][Default: core/suffixes.txt]',default='core/suffixes.txt')
	parser.add_argument('-f','--fix-url',help='Use the URL given by you instead of the root URL [For -a tag]',action='store_true')
	parser.add_argument('-d', '--dork', help="Supply a dork to fetch results from Google[Multipage search]")
	parser.add_argument('-o', '--output', help="Name of the output file [JSON,TXT,CSV]", default='output.txt')
	parser.add_argument('-up','--check-updates',action='store_true',help='Checks for updates')
	args = parser.parse_args()

	if args.check_updates:
		check_updates()

	if args.url:
		targetedScan(args.url)

	if args.admin_panel:
		findAdminPanel(args.admin_panel,args.suffix_file,args.fix_url)

def findAdminPanel(url,file,boolean):
	from time import time
	from core.adminfinder import adminFinder
	info(f'Witch is going to use the suffix file: {file}')
	info('Finding possible admin panels. This may take a while...\n')
	then = time()
	results = adminFinder(url,file,boolean)
	now = time()
	tm = now-then
	print('')
	info(f'Finished in {tm} secs')
	info(f'Total suffixes: {results[1]}')
	info(f'Failed Connections: {results[2]}')
	info(f'Sites with Response 200: {len(results[0])}')
	if len(results[0]) != 0:
		info('Possible admin panels:')
		for x in results[0]:
			plus(x)

if __name__ == '__main__':
	try:
		main()
		Quit()
	except KeyboardInterrupt:
		error('KeyboardInterrupt [Ctrl + C]')
		Quit()
