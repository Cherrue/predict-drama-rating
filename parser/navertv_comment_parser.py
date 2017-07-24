from bs4 import BeautifulSoup
from selenium import webdriver
import time
import odbc
import dbi
import datetime

connect=odbc.odbc('tv')
db=connect.cursor()
driver=webdriver.Chrome('C:\Python34\chromedriver.exe') 

db.execute("SELECT * FROM tv.tvcast_video_list_re2;")
video_list = db.fetchall()
###----------running time : about 6 days----------###


for video in video_list:
    print(video[1])
    isDelete_video = 0
    url = "http://tvcast.naver.com/v/"+str(video[1])
    
    once_more = True
    
    while once_more:
        driver.get(url)
        time.sleep(2)
        try:
            once_more = False
            driver.find_elements_by_xpath("//a[contains(@ class,'u_cbox_select')]")[1].click()
        except:
            once_more = True
            time.sleep(2)
            print("can't find ÀüÃ¼´ñ±Û button!!!!")
            isDelete_video+=1
            if(isDelete_video>10):
                break
        time.sleep(0.3)
    if(isDelete_video>10):
        continue
        
    #parse
    i=0
    while(True):
        print(i)
        soup=BeautifulSoup(driver.page_source,"html.parser")
        comment_list_tag = soup.find_all('div',{'class' : 'u_cbox_comment_box'})
        for comment in comment_list_tag:
            if(comment.find('span','u_cbox_delete_contents')!=None):
                print('deleted comment')
                continue
            nick = comment.find('span','u_cbox_nick').string.strip()
            if(comment.find('span','u_cbox_contents').string == None):
                contents = ''
            else:
                contents = comment.find('span','u_cbox_contents').string.replace("'",'')
            date = comment.find('span','u_cbox_date')['data-value'].replace('T',' ')
            date = date[:19]
            good = int(comment.find('em','u_cbox_cnt_recomm').string.strip())
            bad = int(comment.find('em','u_cbox_cnt_unrecomm').string.strip())
            
            try:
                db.execute("INSERT into tv.tvcast_comment_list2 VALUES(%d, %d,'%s','%s','%s',%d, %d,'%s')" %(int(video[0]),int(video[1]),nick,contents,date,good,bad,datetime.datetime.now()))
            except:
                db.execute("INSERT into tv.tvcast_comment_list2 VALUES(%d, %d,'%s','%s','%s',%d, %d,'%s')" %(int(video[0]),int(video[1]),nick,'including imoticon',date,good,bad,datetime.datetime.now()))
        try: #go next page
            if(i%5==0):
                driver.find_elements_by_xpath("//a[contains(@ class,'u_cbox_page')]")[0].click()
            elif(i%5==1):
                driver.find_elements_by_xpath("//a[contains(@ class,'u_cbox_page')]")[1].click()
            elif(i%5==2):
                driver.find_elements_by_xpath("//a[contains(@ class,'u_cbox_page')]")[2].click()
            elif(i%5==3):
                driver.find_elements_by_xpath("//a[contains(@ class,'u_cbox_page')]")[3].click()
            elif(i%5==4):
                driver.find_elements_by_xpath("//a[contains(@ class,'u_cbox_next')]")[0].click()
        except:
            break
        i+=1
        time.sleep(0.7)

