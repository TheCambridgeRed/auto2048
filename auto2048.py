#! python3
# auto2048.py - Automates playing 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions as selenium_exceptions
import time
import re

browser = webdriver.Firefox()
browser.get('https://play2048.co')

cookies_button = browser.find_element_by_class_name(
    'cookie-notice-dismiss-button')
mobiles_button = browser.find_element_by_class_name('notice-close-button')
time.sleep(1)
cookies_button.click()
time.sleep(1)
mobiles_button.click()

page = browser.find_element_by_tag_name('html')
score = browser.find_element_by_class_name('score-container')
running_score = score.text

keys_list = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]
i = 0

while True:
    try:
        time.sleep(0.1)
        page.send_keys(keys_list[i])
        browser.find_element_by_class_name('game-over')
        break
    except selenium_exceptions.NoSuchElementException:
        if i == 3:
            i = 0
        else:
            i += 1

score_text_re = re.compile(r'^(\d*)(\s\+\d*)?$')
score_text_mo = score_text_re.search(score.text)

print(f'Game over! Got a score of {score_text_mo.group(1)}!')
time.sleep(5)
browser.quit()
