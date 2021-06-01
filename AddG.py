'''Author ***RAJAREDDY*****'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 1)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", r'C:\Users\koushik\Desktop\downloads')
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/.Appx")
time.sleep(5)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv, text/csv, text/plain,application/octet-stream doc xls pdf txt")
profile.set_preference('browser.helperApps.alwaysAsk.force', False)
profile.set_preference('browser.download.manager.alertOnEXEOpen', False)
profile.set_preference('browser.download.manager.focusWhenStarting', False)
profile.set_preference('browser.download.manager.useWindow', False)
profile.set_preference('browser.download.manager.showAlertOnComplete', False)
profile.set_preference('browser.download.manager.closeWhenDone', False)
time.sleep(5)
driver = webdriver.Firefox(firefox_profile=profile, executable_path=r'c:\geckodriver-v0.26.0-win64\geckodriver.exe')
time.sleep(5)

main_url = "https://store.rg-adguard.net/"
def send_url_location(app_url):
    try:
        driver.find_element_by_id("url").send_keys(app_url)
    except NoSuchElementException as exception:
        return "No Results"

def select_retail():
    try:
        drop_down = driver.find_element_by_xpath('//*[@id="ring"]')
        select = Select(drop_down)
        select.select_by_visible_text("Retail")
        time.sleep(5)
    except NoSuchElementException as exception:
        return "No Results"

def click_submit_button():
    try:
        driver.find_element_by_xpath('/html/body/div/input[3]').click()
        time.sleep(10)
    except NoSuchElementException as exception:
        print("No Results")

def click_download_link_apex(i):
    try:
        driver.find_element_by_partial_link_text('appx').click()
        time.sleep(15)
    except NoSuchElementException as exception:
        print("download link No Results",i)


def driver_fun():
    driver.get(main_url)
    #with open (r'C:\AppReputations\GovernmentAndPolitics.txt','r') as f:
    with open(r'C:\AppReputations\healthAndFitness.txt', 'r') as f:
    # with open(r'C:\\Users\\koushik\\Downloads\\Education.txt', 'r') as f:
        #games_family_kids
        urls_list = f.readlines()
        for i in urls_list:
            send_url_location(i)
            select_retail()
            click_submit_button()
            click_download_link_apex(i)

    driver.quit()

#driver function
driver_fun()