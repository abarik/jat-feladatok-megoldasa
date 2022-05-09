# 013 Feladat: Lokátorok gyakorlása
#
# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az
# http://localhost:9999/kitchensink.html oldalt.
# Gyakorlás képpen keress ki elemekt a képernyőről az
# alábbi kritériumoknak megfelelően:
# ID alapján
# NAME alapján
# XPath kifejezéssel.
# Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.
# A megoldást egy locators.py nevű fileban kell beadnod.


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'http://selenium.oktwebs.training360.com/kitchensink.html'

browser = webdriver.Chrome(PATH)
browser.get(URL)

button = browser.find_element_by_id('mousehover')
print(button.tag_name)  # elem neve
print(button.rect)  # a téglalap méretei
print(button.value_of_css_property('color'))  # valamely CSS property
print(button.get_attribute('id'))  # az id attribútum értéke
print(button.get_attribute('class'))  # a class attribútum értéke
print(button.text)  # az elem tartalma

table = browser.find_element_by_name('courses')
print(table.tag_name)  # elem neve
print(table.rect)  # a téglalap méretei
print(table.value_of_css_property('color'))  # valamely CSS property
print(table.get_attribute('id'))  # az id attribútum értéke
print(table.get_attribute('class'))  # a class attribútum értéke
print(table.text)  # az elem tartalma


check = browser.find_element_by_xpath('//input[@name="cars" and @type="checkbox"]')
print(check.tag_name)  # elem neve
print(check.rect)  # a téglalap méretei
print(check.value_of_css_property('color'))  # valamely CSS property
print(check.get_attribute('id'))  # az id attribútum értéke
print(check.get_attribute('class'))  # a class attribútum értéke
print(check.get_attribute('value'))  # a value attribútum értéke
print(check.text)  # az elem tartalma


browser.quit()

# INFO !!!
# http://xpather.com/
