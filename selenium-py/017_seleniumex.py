# 008 Feladat: Hibakezelés megvalósítása selenium programban
#
# Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről. Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt. A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás. Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet. Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál lekezeli a nemlétező elem tipusú hibát. A megoldáshoz használj python try except struktúrát.
# A megoldást egy seleniumex.py nevű fileban kell beadnod.


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'https://www.python.org/'

browser = webdriver.Chrome(PATH)
browser.get(URL)

try:
    control = browser.find_element_by_xpath('//div[@id="nemletezik"]')
except NoSuchElementException:
    print('Az elem nem létezik!')
else:
    print('Minden oké!')

controls = browser.find_elements_by_xpath('//div[@id="nemletezik"]')
if len(controls) == 0:
    print('Az elem nem létezik!')
else:
    print('Minden oké!')

browser.quit()
