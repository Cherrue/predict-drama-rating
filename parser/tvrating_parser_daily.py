#tv rating parser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import odbc
import dbi
import urllib.request as re
import datetime

connect=odbc.odbc('tv')
db=connect.cursor()
#00:전국 01:수도권/// 1:지상파(2007부터) 2:종편(2013부터) 3:케이블(2014부터)
url_list = ["http://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=00","http://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=1_1&area=01","http://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=2_1&area=00","http://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=2_1&area=01","http://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=3_1&area=00","http://www.nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu=3_1&area=01"]


driver=webdriver.Chrome('C:\Python34\chromedriver.exe')
print('start')

#pre-build list and variable
db.execute("SELECT max(rating_id) FROM tv.tv_rating;")
table = db.fetchall()
i=int(table[0][0])+1

db.execute("SELECT max(date) FROM tv.tv_rating;")
table = db.fetchall()
LAST_PARSE_DATE=table[0][0]
TODAY = datetime.datetime.today()
delta = TODAY-LAST_PARSE_DATE

db.execute("SELECT * FROM tv.channel;")
table = db.fetchall()
channel_lst = []
for x in range(len(table)):
    channel_lst.append(table[x][1])
    
db.execute("SELECT * FROM tv.drama;")
table = db.fetchall()
drama_lst = []
for x in range(len(table)):
    drama_lst.append(table[x][2])

for iter_day in range(1,delta.days):
    datediff=datetime.timedelta(delta.days-iter_day)
    for url in url_list:
        #set pre-defined variable
        driver.get(url)
        if(url[73]=='1'):
            delivery = 'terrestrial'
        elif(url[73]=='2'):
            delivery = 'gpcs'
        elif(url[73]=='3'):
            delivery = 'cable'
        if(url[-1]=='0'):
            area = 'nationwide'
        else:
            area = 'capital'
        #set date
    
        today = datetime.date.today() - datediff
        print(today,datetime.date.today(),datediff)
        driver.find_element_by_name('sYear').send_keys(str(today.year))
        if(today.month<10):
            driver.find_element_by_name('sMonth').send_keys("0"+str(today.month))
        else:
            driver.find_element_by_name('sMonth').send_keys(str(today.month))            
        if(today.day<10):
            driver.find_element_by_name('sDay').send_keys("0"+str(today.day))    
        else:
            driver.find_element_by_name('sDay').send_keys(str(today.day))
        driver.execute_script("goSearch()")
        time.sleep(0.3)
        
        print(today,delivery)        
        #go page
        soup = BeautifulSoup(driver.page_source,'html.parser')
        RankingTable = soup.find('table','ranking_tb')
        rows = RankingTable.find_all('tr')
        if rows[3].find('td').string=="데이터가 존재하지 않습니다. 날짜를 다시 선택해 주세요.":
            print(today,"date Error")
            continue            
        
        for row in rows[3:]:
            columns=row.find_all('td')
            
            #casting parse data to variable
            rank=int(columns[0].string.strip())
            channel=columns[1].string.strip()
            name=columns[2].string.strip()
            rating=float(columns[3].string.strip())
            house_num=0
            
            if channel not in channel_lst:
                db.execute("insert into tv.channel VALUES(%d,'%s')"%(len(channel_lst),channel))
                channel_id = len(channel_lst)
                channel_lst.append(channel)
            else:
                channel_id = channel_lst.index(channel)
            
            if name not in drama_lst:
                db.execute("insert into tv.drama VALUES(%d,%d,'%s')"%(len(drama_lst),channel_id,name))
                drama_id = len(drama_lst)
                drama_lst.append(name)
            else:
                drama_id = drama_lst.index(name)
            db.execute("INSERT into tv.tv_rating(rating_id,delivery,area,date,ranking,channel_id,drama_id,rating,house) VALUES(%d,'%s','%s','%s',%d,%d,%d,%f,%d)" %(i,delivery,area,today, rank,channel_id,drama_id,rating,house_num))
            i=i+1
    print('end')
driver.close()