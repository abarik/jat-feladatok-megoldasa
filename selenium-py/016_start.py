# Feladat: Selenium weboldal menyitás gyakorlása
#
# Készíts egy Python alkalmazást ami selenium-ot használ. Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
# A megoldást egy start.py nevű fileban kell beadnod.

# INFO !!!!!!!!!!
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver
# https://www.selenium.dev/documentation/webdriver/
# https://www.lambdatest.com/blog/complete-guide-for-using-xpath-in-selenium-with-examples/


from selenium import webdriver

PATH = 'e:/Drives/OneDrive_abarik_mailbox_unideb_hu/OneDrive - Debreceni Egyetem/Sajat/struktaravalto_kepzes/PM_junior_automata_tesztelo/IdeaProjects/chromedriver.exe'
URL = 'https://www.python.org/'

browser = webdriver.Chrome(PATH)
browser.get(URL)

browser.maximize_window()  # teljes képernyőre tesszük
print(browser.title)  # a cím kiírása a képernyőre

if 'Python' in browser.title:
    print('Success')
    browser.save_screenshot('screenshot.png' + browser.title + '.png')
else:
    print('Failed')

browser.quit()
