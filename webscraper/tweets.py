import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_tweets(hash_tag):
    chrome_options = Options()
    chrome_options.headless = True
    browser = webdriver.Chrome(chrome_options=chrome_options)
    url = f'https://twitter.com/search?q=%23{hash_tag}&src=typed_query&f=top'

    browser.get(url)
    time.sleep(1)

    body = browser.find_element(By.TAG_NAME, 'body')

    for _ in range(5):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

    tweets = browser.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')

    for i in tweets:
        print(i.get_attribute('innerText'))
