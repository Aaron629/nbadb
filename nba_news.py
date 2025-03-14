import requests
import sys,os
import django
django.setup()
sys.path.append('C:/Users/nbadb/nbadb/nbadb')
os.environ["DJANGO_SETTINGS_MODULE"]="nbadb.settings"
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from nbadata.models import Nba_news 
import time,datetime

s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://tw-nba.udn.com/nba/index")
res = requests.get('https://tw-nba.udn.com/nba/index')
soup = BeautifulSoup(res.text, "html.parser")
titles = soup.find_all('div', class_='box_body') 
# print(titles)
title_items =[]
memo_items =[]
up_time = datetime.now()
up_user="aaron"
total = 0 
target_count = 500
while target_count > len(title_items):
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  # 等待頁面加載
  time.sleep(3)
  for i in titles:
    for j in i.find_all('h3'):
      title_items.append(j.text[4:])
      Nba_news.objects.create(title=j.text[4:],ldate=up_time,luser=up_user,iobool=True)
      for k in i.find_all('p'):
        memo_items.append(k.text)
        Nba_news.objects.update_or_create(defaults={'title':j.text[4:]},memo=k.text,ldate=up_time,luser=up_user,iobool=True)
    
    

