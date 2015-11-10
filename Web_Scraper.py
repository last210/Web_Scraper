import urllib
import re 

#web_input = urllib.urlopen("http://www.google.com")
user_input = raw_input("Enter webaddress to be scraped: ")
web_input = urllib.urlopen(user_input)
web_output = web_input.read()

""" #PULLS TITLE
title = "<title>(.+?)</title>" #(.+?) pulls anything between title tags
title_compile = re.compile(title)
title_output = re.findall(title_compile, web_output) #atleast two arguments
"""

print web_output
#print title_output