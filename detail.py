import pandas as pd 
from bs4 import BeautifulSoup 
import requests
import re
import csv
   
URL = 'http://asset.led.go.th/newbidreg/asset_open.asp?law_suit_no=8274&law_suit_year=2551&Law_Court_ID=039&deed_no=171367&addrno=-'
# URL = 'http://asset.led.go.th/newbidreg/asset_open.asp?law_suit_no=1377&law_suit_year=2544&Law_Court_ID=417&deed_no=4163&addrno=-'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


deed_no = soup.findAll("div", class_="card-text")
deed_no = re.findall("ที่ดิน </strong></font>.+", str(deed_no))[0]
deed_no = deed_no.replace("ที่ดิน </strong></font> ", "")
deed_no = deed_no.replace("\xa0", " ")
deed_no = deed_no.replace("\r", "")


print(deed_no)