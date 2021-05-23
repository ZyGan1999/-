import requests
from bs4 import BeautifulSoup
import csv
with open('urls.csv','r') as cf:
    f_csv = csv.reader(cf)
    headers = next(f_csv)
    for row in f_csv:
        url = 'http:'+row[0]
        name = row[1]
        print(name)

        strhtml = requests.get(url)
        soup=BeautifulSoup(strhtml.text,'lxml')
        data = soup.select('#text > table')
        try:
            data = str(data[0])
            '''
            if data.find('?') != -1:
                continue
            '''
            header = ['日期','连云港','青岛港','三门峡','滨州','吕梁','百色','贵阳','乌鲁木齐','内蒙古']

            data = data[data.find('<td>2'):]
            data = data.split('\n')


            cleanData = []
            for item in data:
                if item.find('\xa0</td>') != -1:
                    item = item.split('<td>',1)[1]
                    item = item.split(' \xa0</td>',1)[0]
                    cleanData.append(item)
            avePriceInfo = []
            idx = 0
            for i,item in enumerate(data):
                if item.find('均价') != -1:
                    idx = i
                    break
            for i in range(i,len(data)):
                avePriceInfo.append(data[i])

            for item in avePriceInfo:
                if item.find('td') != -1:
                    if item.find('colspan') != -1:
                        item = item.split('<td colspan=\"3\">',1)[1]
                        item = item.split('</td>',1)[0]
                        cleanData.append(item)
                    else:
                        item = item.split('<td>',1)[1]
                        item = item.split('</td>',1)[0]
                        cleanData.append(item)

            import csv
            with open('./result/'+name+'.csv','w') as f:
                print(header[0],end='',file=f)
                for i in range(1,len(header)):
                    print(','+header[i]+"low",end='',file=f)
                    print(','+header[i]+"high",end='',file=f)
                    print(','+header[i]+"ave",end='',file=f)
                print('',file=f)
                for i in range(len(cleanData)-9):
                    if (i+1) % 28 == 0:
                        print(cleanData[i],file=f)
                    elif i != len(cleanData) - 1:
                        print(cleanData[i],end=',',file=f)
                    else:
                        print(cleanData[i],file=f)
                for i in range(len(cleanData)-9,len(cleanData)):
                    if i != len(cleanData)-9:
                        print(",,,"+cleanData[i],end='',file=f)
                    else:
                        print(",,"+cleanData[i],end='',file=f)
        except:
            continue


'''
url = 'https://lv.mymetal.net/p/21/0521/15/B8B1975331E45E74.html'
strhtml = requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#text > table')

data = str(data[0])

header = ['日期','连云港','青岛港','三门峡','滨州','吕梁','百色','贵阳','乌鲁木齐','内蒙古']

data = data[data.find('<td>2'):]
data = data.split('\n')


cleanData = []
for item in data:
    if item.find('\xa0</td>') != -1:
        item = item.split('<td>',1)[1]
        item = item.split(' \xa0</td>',1)[0]
        cleanData.append(item)
avePriceInfo = []
idx = 0
for i,item in enumerate(data):
    if item.find('均价') != -1:
        idx = i
        break
for i in range(i,len(data)):
    avePriceInfo.append(data[i])

for item in avePriceInfo:
    if item.find('td') != -1:
        if item.find('colspan') != -1:
            item = item.split('<td colspan=\"3\">',1)[1]
            item = item.split('</td>',1)[0]
            cleanData.append(item)
        else:
            item = item.split('<td>',1)[1]
            item = item.split('</td>',1)[0]
            cleanData.append(item)

print(cleanData[0],cleanData[28],cleanData[56])

import csv
with open('./test.csv','w') as f:
    print(header[0],end='',file=f)
    for i in range(1,len(header)):
        print(','+header[i]+"low",end='',file=f)
        print(','+header[i]+"high",end='',file=f)
        print(','+header[i]+"ave",end='',file=f)
    print('',file=f)
    for i in range(len(cleanData)-9):
        if (i+1) % 28 == 0:
            print(cleanData[i],file=f)
        elif i != len(cleanData) - 1:
            print(cleanData[i],end=',',file=f)
        else:
            print(cleanData[i],file=f)
    for i in range(len(cleanData)-9,len(cleanData)):
        if i != len(cleanData)-9:
            print(",,,"+cleanData[i],end='',file=f)
        else:
            print(",,"+cleanData[i],end='',file=f)
'''