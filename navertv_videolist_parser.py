#tv rating parser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import odbc

connect=odbc.odbc('tv')
db=connect.cursor()

driver=webdriver.Chrome('C:\Python34\chromedriver.exe')

#pre-build list and variable
db.execute("SELECT count(*) FROM tv.tvcast_video_list;")
table = db.fetchall()
i=table[0][0]

# 172 : no clip
db.execute("SELECT * FROM tv.tvcast_drama_list where drama_id > 172;")
drama_list = db.fetchall()

db.execute("SELECT * FROM tv.tvcast_video_list;")
table = db.fetchall()
pre_clip_list = []
for row in table:
    pre_clip_list.append(row[1])

pre_clip_exist=0
for drama in drama_list:
    drama_url = drama[2]
    if 'playlists' in drama_url:
        drama_url = drama_url[:-10]
    driver.get(drama_url+'/clips')
    while(True):
        time.sleep(0.7)
        try:
            driver.find_element_by_xpath("//a[@class='bt_more']").click()
        except:
            break
        
    soup = BeautifulSoup(driver.page_source,'html.parser')
    time.sleep(0.7)
    
    video_list_tag = soup.find('div','wrp_cds _cardArea')
    try:
        video_list = video_list_tag.find_all('div','cds _MM_CARD ')
    except:
        print(drama[0],'no clip in channel!')
        continue
    for video_tag in video_list:
        drama_id = drama[0]
        video_id = int(video_tag.find('a')['href'][3:])
        if video_id in pre_clip_list:
            print('already exist',pre_clip_exist,drama_id,video_id)
            pre_clip_exist+=1
        else:
            print(i,drama_id,video_id)
            i+=1
            db.execute("insert into tv.tvcast_video_list VALUES(%d,%d)"%(drama_id,video_id))
