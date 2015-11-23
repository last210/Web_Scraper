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

def get_current_stock():
    url = "http://finance.yahoo.com/q?s=rax&ql=1"
    open_url = urllib.urlopen(url)
    read_url = open_url.read()
    find_price = '<span id="yfs_l84_rax">(.+?)</span>'
    compile_price = re.compile(find_price)
    price = re.findall(compile_price, read_url)
    print "The current stock price of RAX is {0}".format(price)

if __name__ == "__main__":
	main()
    get_current_stock()
