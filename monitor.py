import time
from utils import config
from utils.log import logger
from visa import Visa
from selenium import webdriver
from bot import bot

def init_driver():
    profile = {
        "profile.default_content_setting_values.notifications": 2  # block notifications
    }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', profile)

    chrome_options.headless = True

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    chrome_options.add_argument('--user-agent={'+user_agent+'}')

    # chrome_options.add_argument("--user-data-dir=/Users/vxwong/Library/Application Support/Google/Chrome")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver


def monitor():
    try:
        driver = init_driver()
        visa = Visa(driver)
        visa.go_to_appointment_page()
        visa.login()
        visa.go_to_book_appointment()
        visa.select_centre(*config.BOOKING_CENTER)
        while True:
            dates = visa.check_available_dates()
            if dates:
                logger.info(f"DAY AVAILABLE: {dates}")
                bot.send_message(chat_id=config.CHAT_ID, text=f'DAY AVAILABLE: {dates}')
                # driver.back()
            else:
                logger.info(f"NO DAY AVAILABLE..")
            logger.info(f"Sleep: {config.TIMEOUT}")
            time.sleep(config.TIMEOUT)
            driver.refresh()

    except Exception as e:
        logger.error(f'Monitor runtime error. {e}')
        monitor()


def test_notify():
    try:
        res = bot.send_message(chat_id=config.CHAT_ID, text='bot has started monitoring')
        if type(res) is dict and res['ok'] == False:
            raise Exception(res['error'])
    except Exception as e:
        logger.error(
            f'Test notify error. please make sure that you\'ve sent a message to the bot if you didn\'t change the CHAT_ID in the config.\n\n {e}')
        exit(0)


if __name__ == "__main__":
    test_notify()
    monitor()
