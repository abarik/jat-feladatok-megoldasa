# 010 Feladat: Selenium findby elágazásokkal
#
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az
# http://localhost:9999/trickyelements.html oldalt.
# Használj id lokátort és keressd ki az elemenekt egyesével.
# A legelső olyan elemre ami button típusú kattints rá és ellenőrizd,
# hogy a helyes szöveg jelenik-e meg az elemek listája alatt.
# A megoldást egy elementtype.py nevű fileban kell beadnod.

# 008 Feladat: Hibakezelés megvalósítása selenium programban
#
# Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről. Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt. A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás. Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet. Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál lekezeli a nemlétező elem tipusú hibát. A megoldáshoz használj python try except struktúrát.
# A megoldást egy seleniumex.py nevű fileban kell beadnod.


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'http://selenium.oktwebs.training360.com/trickyelements.html'

browser = webdriver.Chrome(PATH)
browser.get(URL)

buttons = browser.find_elements_by_xpath('//button')
label = browser.find_element_by_xpath('//label[@id="result"]')
if len(buttons) > 0:
    buttons[0].click()
    # print(buttons[0].text)
    # print(label.text)
    if buttons[0].text in label.text:
        print('Test success!')
    else:
        print('Test failed!')
else:
    print('Test blocked! (No button elements.)')

browser.quit()

# INFO !!!
# http://xpather.com/
