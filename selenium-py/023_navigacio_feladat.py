# 017 Feladat: Navigációs feladatok
#
# A program töltse be a példatárból az http://localhost:9999/general.html oldalt.
# A feladatod, hogy végiglátogassd az összes linket ezen az oldalon.
# Egy link meglátogatása akkor érvényes, ha a hozzá tartozó a html elemre rákattintottál,
# a megjelent új oldalnak ellenrőizted, hogy eggyezik az urlje az előzőleg használt
# a tag href-jével és sikeresen vissza navigáltál a főoldalra.
# (A tökéletes megoldás nem tartalmaz sor ismétléseket.
# Ezt mondjuk függvények írásával is elő tudod idézni.)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'http://selenium.oktwebs.training360.com/general.html'

browser = webdriver.Chrome(PATH)


def go_to_page(link):
    try:
        a_href = link.get_attribute('href')
        link.click()
        time.sleep(0.1)
        try:
            assert a_href == browser.current_url
        except AssertionError:
            print(' ---> Assertion failed')
        browser.back()
        time.sleep(0.1)
    except:
        print(' ---> Failed')
    else:
        print(' ---> Success')


try:
    browser.get(URL)
    links = browser.find_elements_by_xpath('//a[boolean(@href) and not(boolean(@target)) and not(contains(@href, "http"))]')
    for link in links:
        print('Cheking: ', link.text, '-----', link.get_attribute('href'), end='')
        go_to_page(link)
finally:
    browser.quit()
