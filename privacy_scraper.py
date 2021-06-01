#extract privacty policies 
'''Author ***RAJAREDDY*****'''
'''
TODO:
> read links from the excel sheet
> get privacy link 
> open link and get html content
> remove script, navigation menu, header, footer, comment
> add the content to next column in excel
'''

# imports
import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup, Comment
import re
import time
from os import walk


# instantiate browser here
option = Options()
option.add_argument('--incognito')
option.add_argument('--ignore-certificate-errors')
option.add_argument('--allow-running-insecure-content')
option.add_argument('--disable-web-security')
#option.add_argument("--lang=es")
# set locale as EN, prefer english version of site
option.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})


option.add_argument("--headless")
# try to get english version by translating
prefs = {"translate_whitelists": {"your native language":"en"},"translate":{"enabled":"True"}}
option.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(executable_path="C:\\Users\\rmishra1\\Downloads\\chromedriver_win32\\new\\chromedriver", chrome_options=option)



# add css remove to clean function
def is_comment(element): 
    return isinstance(element, Comment)

def clr(html):

    
    try:
        soup = BeautifulSoup(html,'lxml').body
        

        #remove all script
        [s.extract() for s in soup(['script','style','header','footer','nav','img'])]
        #remove comment
        '''
        comments = soup.findAll(html=lambda html:isinstance(html, Comment))
        [comment.extract() for comment in comments]
        '''
        #body  = soup.find('body')

        #remove comment
        to_remove = soup.find_all(text=is_comment) 
        for element in to_remove: 
            element.extract()
        #remove empty tags
        for x in soup.find_all():
            if len(x.get_text(strip=True)) == 0:
                x.extract()
    except:
        return 'NULL'
    return soup






def clean(html):
    soup = BeautifulSoup(html,'lxml')
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    # 
    #print(text)
    return text



# get page content from link
def getContent(privacy_url):
    #body
    print(privacy_url)
    # chromedriver path:  C:\Users\rmishra1\Downloads\chromedriver_win32\new
    if privacy_url == 'NULL':
        return "NULL"

    # not useful for now    
    '''
    type = privacy_url[-4:]
    # if static html page then use beautifulsoup, better performance
    if type == '.htm' or type == 'html':
        i = 0
        html = None
        while i<4:
            try:
                html = requests.get(privacy_url)
                break
            except:
                time.sleep(10)
                i+=1
               
            
                
        if html == None or (html.status_code!=200):
            return 'NULL'
        print("\n\n\tSUCCESS\n\n")
        html = html.content

    # otherwise use selenium
    '''
    try:          
        browser.get(privacy_url)
    except:
        return 'NULL'
    print("\n\n\tSUCCESS\n\n")
        
    #content = browser.find_element_by_tag_name('body').text
    html = browser.page_source
    # handle 404 error
    if '404' in browser.title:
        return 'NULL'

    return clr(html)
        





# write dataframe to excel file
def write_excel(file_path, data):
    print(">>>>>>>>>>>writing excel<<<<<<<<<<<<<<<<<<")
    # save as .xlsx
    writer = pd.ExcelWriter(file_path+'x', engine='xlsxwriter') # pylint: disable=abstract-class-instantiated
    data.to_excel(writer, sheet_name ='Sheet1', index = False)
    writer.save()
    print(">>>>>>>>>>>>>>>>done<<<<<<<<<<<<<<<<<<<<<<")



def main():

    dirPath = "C:\\Users\\rmishra1\\Desktop\\work\\top_free\\"
    outPath = "C:\\Users\\rmishra1\\Desktop\\temp\\new\\"
    files = []

    for info in walk(dirPath):
        #print(info)
        files.extend(info[2])

    files = files[20:]
        
    #open files one by one
    for f in files:
        if f.endswith((".xls", ".xlsm", ".xlsx")):
            file_path = dirPath + f
            print("\nOPEN: "+ f + "\n" + "PATH: " + file_path )


            

            print("*"*10+"\n\treading excel\n"+"*"*10)

            xl = pd.read_excel(file_path,keep_default_na=False) # do not treat NULL as default NA

            # rename because column contains links to privacy policies
            xl.rename(columns = {'privacy policy':'privacy_policy_href'}, inplace = True)

            #header = list(xl.columns.values)

            

            privacy = []

            for index, row in xl.iterrows():

                print(index," privacy policy of: ", row['name'])
                time.sleep(1)
                content  = getContent(row['privacy_policy_href'])
                # creating dict with name, append later to dataframe
                #print("*"*100,'\n', content,'\n', "*"*100)
                privacy.append(content)

            #.rename(columns = {'test':'TEST'}, inplace = True)
            # append new column containing privacy policy
            xl = xl.assign(privacy_policy = privacy)
            #xl['privacy policy content'] = privacys
            #print(xl)
            write_excel(outPath+f, xl)
    browser.stop_client()
    browser.close()
    browser.quit()
        
    

main()




