import urllib
import re 

user_input = raw_input("Enter webaddress to be scraped: ")
web_input = urllib.urlopen(user_input)
web_output = web_input.read()

print web_output
