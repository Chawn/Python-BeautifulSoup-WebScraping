import os 
import sys 
import pandas as pd 
from bs4 import BeautifulSoup 
import requests
import re
import json
import csv
   

# path = 'index.html'
URL = 'http://asset.led.go.th/newbidreg/asset_search_province.asp?search_asset_type_id=001&search_tumbol=&search_ampur=&search_province=%CD%D8%B4%C3%B8%D2%B9%D5&search_sub_province=&search_price_begin=&search_price_end=&search_bid_date=&search_rai=&search_rai_if=1&search_quaterrai=&search_quaterrai_if=1&search_wa=&search_wa_if=1&search_status=1&search_person1=&search=ok&page=1'
try: # need to open with try
   page = requests.get(URL)
except:
   raise Exception("Sorry, URL not Found")

soup = BeautifulSoup(page.content, 'html.parser')

with open("main.html", "w") as file:
   file.write(str(soup))


path = 'main.html'
data = [] 
soup = BeautifulSoup(open(path),'html.parser')
table = soup.find(id="box-table-a").find("table")

# tbody = table.find("tbody")
unwanted = table.find('thead')
unwanted.extract()


rows = list()
data_list = list()
titles = ['ล๊อตที่ - ชุดที่','เลขที่โฉนด','ลำดับที่การขาย','หมายเลขคดี','ประเภททรัพย์','ไร่','งาน','ตร.วา','ราคาประเมิน','ตำบล','อำเภอ','จังหวัด']

with open('data.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(titles)
   try: # need to open with try
      for row in table.findAll("tr"):
         deed_no = re.findall("deed_no=.+&amp;", str(row))[0]
         deed_no = deed_no.replace("deed_no=","").replace("&amp;","")
         for index,column in enumerate(row.findAll("td")):
            if index!=1 :
               for data in column:
                  data.strip()
                  data = data.replace('"','')
                  data = data.replace('\n','')
                  data = data.replace('\t','')
                  data = data.replace('\xa0','')
                  data = data.replace('&nbsp;','')
                  data = data.replace(' ','')
            else:
               data = deed_no
            data_list.append(data)
         writer.writerow(data_list)
         data_list = list()
   except:
      raise print("Sorry, Page not Found")   


# Html_file= open("table.txt","w")
# Html_file.write(str(table))
# Html_file.close()

# # print(table)

