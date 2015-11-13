import urllib
import re 
import sys
sys.tracebacklimit=0
import logging

logger = logging.getLogger(__name__)
logger.info('info log')
logger.debug('debug log')

if __name__ == "main": main()
user_input = raw_input("Enter URL to be scraped: ")

def main():	
	try:
		urllib.urlopen(user_input)
	except:
		print "You did not enter a valid URL"
	
def print_html(user_input):
	web_input = urllib.urlopen(user_input)
	web_output = web_input.read()
	print web_output

print_html(user_input)
