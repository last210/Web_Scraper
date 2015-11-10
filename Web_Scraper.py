import urllib
import re 
import sys
sys.tracebacklimit=0

user_input = raw_input("Enter webaddress to be scraped: ")
try:
	urllib.urlopen(user_input)
except:
	print "You did not enter a valid URL"
	
def print_html(html):
	web_input = urllib.urlopen(user_input)
	web_output = web_input.read()
	print web_output

print_html(user_input)
