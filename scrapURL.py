import requests
from bs4 import BeautifulSoup

dataList = []
for n in range(1,23):
    url = 'https://www.mymetal.net/price/p-10005--020202--'+str(n)+'.html'
    #url = 'https://www.mymetal.net/price/p-10005--020202--1.html'
    strhtml = requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    time = soup.select('body > section.t_main_list > div.main_c > div.result_list > ul > li > span')
    data = soup.select('body > section.t_main_list > div.main_c > div.result_list > ul > li > a')

    timeList = []
    urlList = []
    for item in time:
        timeList.append(item.get_text())

    for item in data:
        result = {
            'title':item.get('title'),
            'link':item.get('href')
        }
        urlList.append(result)

    for time,url in zip(timeList,urlList):
        result = {
            'url':url['link'],
            'time':time[:time.find(' ')]
        }
        dataList.append(result)
#print(dataList)
import csv
headers = ['url','time']
with open('./urls.csv','w') as f:
    f_scv = csv.DictWriter(f,headers)
    f_scv.writeheader()
    f_scv.writerows(dataList)
    