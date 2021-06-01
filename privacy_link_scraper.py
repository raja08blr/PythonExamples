'''Author ***RAJAREDDY*****'''

import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import time
import ast

    
# url to scrape
url = "https://www.microsoft.com/en-in/store/top-free/apps/pc"

base = "https://www.microsoft.com"

# get all categories
def getCategory(url):
    content = requests.get(url)

    ref = BeautifulSoup(content.text,'lxml')
    cat_list = []

    # find all the items in category
    for item in ref.find('div',{"id": "refine-by-menu-title-Category"}).findAll('a'):
        # replace  ' & ' with '_and_' in name
        # append (name, href) tuple to list  
        cat_list.append((item['aria-label'].replace(' & ','_and_'), item['href']))   # href = /en-in/store/top-free/apps/pc?category=xyz

    return cat_list[1:] # remove "all category" item from list


# info of the app
# add error handling
def writeItemInfo(url,row,category,sheet):

    policy = "NULL"
    app_page = requests.get(url)
    i = 0
    while app_page.status_code != 200:
        print("status code "+ str(app_page.status_code))
        i +=1
        if i>10:
            return -1
        if app_page.status_code == 404:
            input("continue?")         

        else:
            time.sleep(5)
        app_page = requests.get(url)
    # ----------------here --------
    data = BeautifulSoup(app_page.text,'lxml')
    name = data.find('h1',{"id":"DynamicHeading_productTitle"}).getText()
    print("name : "+ name)

    itemTemp = data.find('h4',text="Additional terms")
    items = []
    if itemTemp != None:
        items = itemTemp.find_parent('div').findAll('a')
    # check atteribute valu-pairs 
    for item in items:
        
        cn = ast.literal_eval(item.attrs['data-m'])['cN']
        if cn == 'PrivacyPolicy Uri':
            policy = item['href']
        


    content = [name,category,policy]
    print(content)
    for t in range(len(content)):
        sheet.write(row,t,content[t])
    return 0
    
    



# get links of all items on current page
def getLinksOnPage(ref):
    print("got link on page\n")
    item_list = []
    items = ref.find('div',{"class": "c-group f-wrap-items context-list-page"}).findAll('a')
    for item in items:
        item_list.append(item['href'])   

    return item_list


# creates .xls file , use pandas for xlsx
def create_excel(cat_url,category):

    print("creating excel \n")
    file = "C:\\Users\\rmishra1\\Desktop\\work\\policyReader\\scraper\\"+category+".xls"
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(category)
    content = ["name","category","privacy policy"]

    for i in range(len(content)):
        sheet.write(0,i,content[i])
    val = 1
    while True:
        
        content = requests.get(cat_url)
        while content.status_code != 200:
            time.sleep(5)
            content = requests.get(cat_url)

        ref = BeautifulSoup(content.text,'lxml')

        next_btn = ref.find('a', {"aria-label": "next page"})
        if next_btn != None:
            next_btn = next_btn['href']
        elif cat_url[-2] != '-':
            time.sleep(15)
            content = requests.get(cat_url)
            ref = BeautifulSoup(content.text,'lxml')
            next_btn = ref.find('a', {"aria-label": "next page"})
            next_btn = next_btn['href']
        else:
            next_btn = '-1'   


        #print(next_btn)
        list = getLinksOnPage(ref)
        
        for l in list:
            print(l)
            
            val+=1 + writeItemInfo(base+l,val,category,sheet)
        print(next_btn[-2])
        workbook.save(file)
        if next_btn[-2] == '-':
            break
        cat_url = base+next_btn
        

   



def scrape():
     
    cat = getCategory(url)
    print(cat)
    
    for c in cat:
        print("now scraping: "+ str(c[0]))
        create_excel(base+c[1],c[0]) 
       
        
     
        
scrape()




    


