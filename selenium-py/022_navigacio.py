# Navigáció
#
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Navigáció gyakorlása

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'http://selenium.oktwebs.training360.com/'

browser = webdriver.Chrome(PATH)


def go_to_general_page():
    # general_link = browser.find_element_by_xpath('//a[text()="General text and other elements"]')
    general_link = browser.find_element_by_xpath('//a[contains(text(), "General text and other elements")]')
    general_link.click()


try:
    browser.get(URL)
    print(browser.title)
    go_to_general_page()
    time.sleep(0.5)
    browser.back()
    time.sleep(0.5)
    go_to_general_page()
    print(browser.current_url)
    anchors = browser.find_elements_by_xpath('//header//small//a')
    for a in anchors:
        a.click()
        time.sleep(0.5)
        print(browser.current_url)
    print('*' * 50)
    while browser.current_url != URL:
        browser.back()
        print(browser.current_url)



finally:
    browser.quit()
