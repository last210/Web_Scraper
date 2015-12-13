import urllib
import re
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


def valid_stock():
    configure_logging()
    open_stockfile = open("stocks.txt")
    stockfile = open_stockfile.read()
    user_stock = raw_input("Which stock would you like the current price of? ")
    logger.info("USER INPUT: %s", user_stock)

    if user_stock.upper() in stockfile:
        try:
            get_current_stock(user_stock)
        except :
            raise Exception("INVALID INPUT FROM USER")
    else:
        logger.exception("INVALID INPUT FROM USER")
        print "You did not enter a valid stock"
        try_again()

def try_again():
    try_again = raw_input("Would you like to try again? [Y or N] ")
    if try_again.upper() == "Y":
        valid_stock()
    elif try_again.upper() == "N":
        print "Have a good day!"
    else:
        print "You did not enter a valid response. Please enter Y or N. "
        # still need prompt for new response
        # enable exit after 3 attempts

def get_current_stock(user_stock):
    url = "http://finance.yahoo.com/q?s=" + user_stock + "&ql=1"
    open_url = urllib.urlopen(url)
    read_url = open_url.read()
    find_price = ('<span id="yfs_l84_' +
                 user_stock.lower() + '">(.+?)</span>')
    compile_price = re.compile(find_price)
    price = re.findall(compile_price, read_url)
    print ("The current stock price of {0} is {1}".format(
               user_stock.upper(), price))

if __name__ == "__main__":
    # main()
    # get_current_stock()
    valid_stock()
