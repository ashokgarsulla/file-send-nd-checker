
import requests
from bs4 import BeautifulSoup as bs
import csv
import os

from datetime import datetime

# time based file name
now = datetime.now().strftime("%d%m%Y%H%M%S")
filename = str(now+".csv")
headerList =['Txn Hash','Method','Block','Age','From','To','BNB','txn_fee']

with open(filename, 'w') as file:
    dw = csv.DictWriter(file, delimiter=',', 
                        fieldnames=headerList)
    dw.writeheader()




bscscan = 'https://bscscan.com/txs?p='
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36 Edge/12.246"}
count = 1

for page in range(1,10001):
    req = requests.get(bscscan + str(page),headers=headers)
    # req = requests.get(bscscan + str(page))

    soup = bs(req.content, 'html.parser')
    table = soup.find('table')
    print(soup.prettify())
    if table is None:
        continue
    Tbody = table.find('tbody')
    rows = Tbody.find_all('tr')
    # print(rows)
    # print(rows)
    data_list = []
    for tr in rows:
        cols = tr.findAll('td')
        d ={}
        for colNo in range(1,11):
            
            if colNo == 1:
                d['Txn Hash'] = cols[colNo].find("span",class_="hash-tag text-truncate").text
            if colNo == 2:
                d['Method'] = cols[colNo].text
            if colNo == 3:
                d['Block'] = cols[colNo].text
            if colNo == 4:
                continue
            if colNo == 5:
                d['Age'] = cols[colNo].text
            if colNo == 6:
                d['From'] = cols[colNo].text
            if colNo == 7:
                continue
            if colNo == 8:
                d['To'] = cols[colNo].text
            if colNo == 9:
                d['BNB'] = cols[colNo].text 
            if colNo == 10:
                d['txn_fee'] = cols[colNo].text
        data_list.append(d)
    with open(filename, 'a', newline='') as f:
        w = csv.DictWriter(f,['Txn Hash','Method','Block','Age','From','To','BNB','txn_fee'])
        # w.writeheader()
        w.writerows(data_list)
    
    print("page number: ",page," completed")
        
        




