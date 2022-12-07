import json
import re
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from selenium import webdriver


def main():
    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'

    links_product = ['https://www.wildberries.by/catalog/84888191/detail.aspx?targetUrl=MI']



    for url in links_product:
        # response = session.get(url, timeout=20)
        # time.sleep(5)
        # if response.status_code != 200:
        #     continue
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.find('div', class_="slide__content"))

        # celenium
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(3)
        browser.find_element(by=By.CLASS_NAME, value="zoom-image-container").click()
        time.sleep(3)
        html_page = browser.page_source
        soup = BeautifulSoup(html_page, 'html.parser')
        blocks = soup.findAll('div', class_="zoom-image-container")
        for block in blocks:
            images = block.findAll('img')
            for i in images:
                print('src', "" + i['src'].replace('//', 'https://'))
# https://basket-05.wb.ru/vol848/part84888/84888191/images/big/3.jpg
if __name__ == '__main__':
    main()
