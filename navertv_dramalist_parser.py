#tv cast drama list parser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import odbc

connect=odbc.odbc('tv')
db=connect.cursor()

driver=webdriver.Chrome('C:\Python34\chromedriver.exe')

#pre-build list and variable
db.execute("SELECT max(drama_id) FROM tv.tvcast_drama_list;")
table = db.fetchall()
if table[0][0] is None:
    i=0
else:
    i=int(table[0][0])+1

db.execute("SELECT * FROM tv.tvcast_drama_list;")
table = db.fetchall()
pre_drama_list = []
for row in table:
    pre_drama_list.append(row[1])
    

driver.get('http://tv.naver.com/c/drama/channels')
##first parse drama number = 663 / 2017.03.21
##second parse drama number = 803 / 2017.07.21
while(True):
    time.sleep(0.7)
    try:
        driver.find_elements_by_xpath("//a[@class='bt_more _click_more']")[-1].click()
    except:
        break;

soup = BeautifulSoup(driver.page_source,'html.parser')

drama_card_list = soup.find('div','thematic_list thematic_list3 _list')
drama_list_tag = drama_card_list.find_all('ul','ch_list')
drama_tag = []
for drama_list_tag_list in drama_list_tag:
    iterator = drama_list_tag_list.find_all('li')
    for element in iterator:
        drama_tag.append(element)
      
t0 = time.time()  
pre_exist_num=0
for drama in drama_tag: 
    info = drama.find('a','info_a')
    drama_url = info['href']
    drama_title = info.find('strong','title').string
    drama_title = drama_title.replace("'",'')
    if drama_title in pre_drama_list:
        print("already exist",pre_exist_num,drama_title)
        pre_exist_num+=1
    else:
        print(i,drama_title)
        db.execute("insert into tv.tvcast_drama_list VALUES(%d,'%s','%s')"%(i,drama_title,drama_url))
        i+=1
        
parse_time = time.time() - t0
print("insert : ",i,"already exist : ",pre_exist_num,"parse time : ",parse_time)