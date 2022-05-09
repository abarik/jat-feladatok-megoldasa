# 015 Feladat: Selenium adat kinyeréses feladatok
#
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/todo.html oldalt.
# A feladatod, hogy kigyűjtsd az összes jelenleg aktív Todo bejegyzést.
#  Ha lehet akkor ezt minnél kevesebb selenium lokátorral old meg.
#  (Tökéletes megoldáshoz csak egy darab find_by hívásra van szükség).
# A megoldást egy todos.py nevű fileban kell beadnod.

# 013 Feladat: Több elem lekérdezése
#
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Kérd le a button-okat és ellenőrizd le a lenyomásuk eredményét


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'http://selenium.oktwebs.training360.com/todo.html'

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    items = browser.find_elements_by_xpath('//span[@class="done-false"]')
    my_list = list()
    for item in items:
        my_list.append(item.text)
    print(my_list)
    assert len(my_list) > 0
finally:
    browser.quit()
