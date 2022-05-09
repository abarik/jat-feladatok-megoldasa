# 013 Feladat: Több elem lekérdezése
#
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Kérd le a button-okat és ellenőrizd le a lenyomásuk eredményét


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'http://selenium.oktwebs.training360.com/trickyelements.html'

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    buttons = browser.find_elements_by_xpath('//button')
    for button in buttons:
        button.click()
        result = browser.find_element_by_xpath('//label[@id="result"]')
        print(result.text)
        assert result.text == f'{button.text} was clicked'
finally:
    browser.quit()
