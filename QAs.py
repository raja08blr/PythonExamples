# print only prime numbers
def prime_num_check(num):
    if num < 1:
        print("Not a prime num")
    if num == 1:
        print("not a prime num")
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not prime num")
                break
            # else:
            #     print(num,"is a prime number")
        else:
            print(num, "is a prime number")


prime_num_check(9)
# prime_num_check(7)
# prime_num_check(2)
# prime_num_check(5)
prime_num_check(15)


def prime_range(str, end):
    for i in range(str, end):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, "is a prime num")


prime_range(15, 20)


### paramiko program
def paramiko_f():
    import paramiko
    client = paramiko.SSHClient()
    client.connect(hostname="asxd", password="assa", port=22)
    cmd = "ls -lat"
    stdin, stdout, stderr = client.exec_command(cmd)
    print(stdout)


## read json file
import json

dic = {"name": "raja", "age": 30}
dic_to_json = json.dumps(dic)  # dumps to convert the dict to json format
print(dic_to_json)
json_to_dic = json.loads(dic_to_json)  # loads to convert json format to dictionary format
print(json_to_dic["name"])

dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
# dump to write dic data to a file
path = r"C:\Users\QuickboostTest\Documents\RajareddyV\\"
file_path = r"C:\Users\QuickboostTest\Documents\RajareddyV\json_sample.txt"
with open(file_path, 'w') as w_j:
    json.dump(dictionary, w_j)

with open(file_path, 'r') as f_s:
    data = json.load(f_s)
    print(data)

# read xml data
# xml.tree is for api manipulating XML
import xml.etree.ElementTree as ET
import requests
import csv

url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
resp = requests.get(url)
print(resp.content)
with open(path + "xmlcontent.xml", 'wb') as xml_w:
    xml_w.write(resp.content)


# parsing
def parsing_xml(file):
    with open(file, 'rb') as read_xml:
        tree = ET.parse(read_xml)
        # print(tree)
        # get root elemts
        root = tree.getroot()
        print(root)
        # create empty list for news items
        newsitems = []

        # iterate news items
        for item in root.findall('./channel/item'):

            # empty news dictionary
            news = {}

            # iterate child elements of item
            for child in item:

                # special checking for namespace object content:media
                if child.tag == '{http://search.yahoo.com/mrss/}content':
                    news['media'] = child.attrib['url']
                else:
                    news[child.tag] = child.text

                    # append news dictionary to news items list
            newsitems.append(news)

            # return news items list
        # print(newsitems)


parsing_xml(path + "xmlcontent.xml")

# read xml dom file using xml mini dom

# from xml.dom import minidom
#
# doc = minidom.parse(path + "test.xml")
#
# # doc.getElementsByTagName returns NodeList
# name = doc.getElementsByTagName("name")[0]
# print(name.firstChild.data)
#
# staffs = doc.getElementsByTagName("staff")
# for staff in staffs:
#     sid = staff.getAttribute("id")
#     nickname = staff.getElementsByTagName("nickname")[0]
#     salary = staff.getElementsByTagName("salary")[0]
#     print("id:%s, nickname:%s, salary:%s" %
#           (sid, nickname.firstChild.data, salary.firstChild.data))

##########
# find valid ip address from a filr
input = "10.3.111.52"
import re

# print(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',input))
lt = input.split(".")
print(len(lt))
if len(lt) != 4:
    print("Not a valid ipv4 address")
else:
    for j in lt:
        for i in range(0, 256):
            if j == i:
                break
                print("valid ipv4")
                # break
            else:
                # break
                print("not valid ip address")
                exit()
    print("valid ipv4 address")


def f():
    city = "Hamburg"

    def g():
        global city
        city = "Geneva"

    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)


f()
print("Value of city in main: " + city)


def sort_without_sort_function():
    l = [-2, -22, 10, 1, 11, -8, 0]
    i = 0
    # for j in range(len(l) + 1):
    for j in l:
        print(j)
        # if l[i] > l[i]:
        #     l[i], l[i + 1] = l[i + 1], l[i]
        # i = i + 1
    # print(l)


sort_without_sort_function()
