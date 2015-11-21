import urllib
import re
import sys
import logging

logger = logging.getLogger(__name__)
logger.info('info log')
logger.debug('debug log')

def configure_logging():
    root_logger = logging.getLogger()
    log_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        "%Y-%m-%d %H:%M:%S")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)
    root_logger.setLevel(logging.DEBUG)

def print_html(user_input):
	web_input = urllib.urlopen(user_input)
	web_output = web_input.read()
	print web_output

def main():
	configure_logging()
	user_input = raw_input("Enter URL to be scraped: ")
	logger.info("user input is %s", user_input)

	try:
		urllib.urlopen(user_input)
	except:
		logger.exception("URL exception")
		print "You did not enter a valid URL"
	print_html(user_input)

if __name__ == "main":
	main()
