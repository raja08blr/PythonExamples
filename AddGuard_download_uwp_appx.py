from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.firefox.options import Options

path=r"C:\Users\QuickboostTest\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe"
options = Options()
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")
driver = webdriver.Firefox(firefox_options=options,executable_path=path)
# url='https://www.microsoft.com/en-in/p/itunes/9pb2mz1zmb1s?cid=msft_web_appsforwindows_chart&activetab=pivot:overviewtab'
# url1= "https://www.microsoft.com/en-in/p/whatsapp-desktop/9nksqgp7f2nh?cid=msft_web_appsforwindows_chart&activetab=pivot:overviewtab"
with open(r"C:\Automation\pps\Urls\music_download_urls.txt",'r') as f:
    data = f.readlines()
    for url in data:
        # print(url)
        driver.get("https://store.rg-adguard.net/")
        driver.find_element_by_xpath('//*[@id="url"]').send_keys(url)
        time.sleep(5)
        drop_down = driver.find_element_by_xpath('//*[@id="ring"]')
        select = Select(drop_down)
        select.select_by_visible_text("Retail")
        time.sleep(10)
        driver.find_element_by_xpath('/html/body/div/input[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/input[3]').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div/input[3]').click()
        driver.find_element_by_xpath('/html/body/div/input[3]').click()
        time.sleep(20)
        dr = driver.find_element_by_xpath('//*[@id="selectBoxInfo"]/table/tbody/tr[2]/td[1]/a')
        t = dr.text
        if "appx" or "appxbundle" in t:
            # print("Present")
            dr.click()
            time.sleep(15)
        else:
            dr1 = driver.find_element_by_xpath('//*[@id="selectBoxInfo"]/table/tbody/tr[4]/td[1]/a')
            t1 = dr1.click()
            # print("No appx",url)


    driver.quit()
# def read_file(path):

