from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

#takes songs and puts them in a list
songList=[]
#lists of songs that are downloaded and not
good=[]
bad=[]
    
#main loop class
class Music:
    def start():
        song=input("Enter a list of songs 1 at a time (input ! to stop): ")
        songList.append(song)
        #indicater to stop taking input
        while song !="!":
            song=input("Enter a list of songs 1 at a time (input ! to stop): ")
            songList.append(song)
        #removes the last index(!)
        songList.pop()
        
    #output for results 
    def output():
        #if no songs were downloaded
        if len(good)==0 & len(bad)==0: 
            return "No songs were donwloaded"
        #if atleast 1 good song downloaded
        if len(good)>0:
            for j in good:
               return "Song: "+'"'+j+'"' + " was successfuly downloaded"
        #if atleast 1 bad song was download
        if len(bad)>0:
            for k in bad:
                return "Song: "+ '"'+k+ '"'+ " could not be downloaded"




    def musicLoop(songs):
        #install driver (not local)
        driver=webdriver.Chrome(ChromeDriverManager().install())
        
        #loops through songList and downloads them all 
        for i in songs:
            #url for youtube
            url="https://www.youtube.com/"
            #opens youtube
            driver.get(url)

            #finds search box on page
            search=driver.find_element_by_name("search_query")
            #searches for entered song
            search.send_keys(i)
            search.submit()
            
            #checking if i search has any results found: if no results
            if driver.find_elements_by_xpath("//*[@id='contents']/ytd-background-promo-renderer/div[1]"):
                bad.append(i)
                driver.close()
                continue
            
            page=BeautifulSoup(driver.page_source,"lxml")
            #find parent class of a tag that has title
            video=page.find("ytd-video-renderer")
            #finds sub class a in h3 then finds title attribute 
            song_title=video.h3.a.get("title")
            print(song_title+'/n')
           
            #clicks the first element with a video title
            driver.find_element_by_id("video-title").click()
            #stores video url
            song_url=driver.current_url
            print(song_url)
            #url for mp3 converter
            downloader="https://www.go-mp3.com/en20"    #does not work find new link
            #opens converter
            driver.get(downloader)
            #locates the search bar and enters in search bar of downoloader
            search2=driver.find_element_by_id("sf")
            search2.send_keys(song_url)
            search2.submit()
            #waits 5 seconds 
            time.sleep(5)
            #then clicks download button
            driver.find_element_by_id("download").click()
            driver.find_element_by_id("download").click()
            good.append(song_title)
            
            driver.switch_to.window(driver.window_handles[0]) #switches to first tab
            time.sleep(5)
        time.sleep(1)
        driver.quit()
        
main=Music()

# main.start() 
# main.musicLoop()
# main.output()