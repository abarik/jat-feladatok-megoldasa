# 001 Feladat: Python filekezelés feladatok
#
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999 oldalt.
# Lokátorral keresd ki az összes linket az oldalról.
# Tárold a memóriában egy listában az összes linket.
# A list tartalmát írd ki egy fájlba. Minden link egy új sorba kerüljön.
# A kimenetre írd ki hány linket találtál
# A megoldást egy linkek.py nevű file-ban kell beadnod.

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

import csv

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'http://selenium.oktwebs.training360.com/'

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    links = browser.find_elements_by_xpath('//a[boolean(@href)]')
    my_links = list()
    for link in links:
        my_links.append([link.text, link.get_attribute('href')])
    print(my_links)
    with open('linkek.txt', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for item in my_links:
            spamwriter.writerow(item)
except:
    print('Hiba')
finally:
    print(len(my_links))
    browser.quit()
