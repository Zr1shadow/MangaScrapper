from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from database import generateDB

#get number 
def getNum():
    num = []
    chap = chapterNum.split()
    for item in chap:
        for subitem in item:
            if subitem.isdigit():   
                num.append(subitem)
    res = int("".join(num))
    return res
# Get data 
def getManga():
    
    #start browser
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome('/Users/RA/Documents/chromedriver', options = chrome_options)
    print("Openings browser")
    #go to X site
    driver.get(mangaURL)
    print("Made it to site")
    #begin finding elements that you want. 

    global title, chapterNum, URL
    title = driver.find_element_by_tag_name('h1').text
    
    chapters = driver.find_elements_by_css_selector('a[class *= \'chapter-name text-nowrap\']')
    print("GOT elements")
    for chapter in chapters:
        URL = chapter.get_attribute('href')
        chapterNum = chapter.text
        print(title + " " + URL + " " + str(getNum()))
        generateDB(title, getNum(), getNum())
        
    # import database
    time.sleep(1)
    driver.close()
    driver.quit()
    

if __name__ == "__main__":
    
# Enter new manga to be tracked 
    mangaURL = input('URL')
    getManga()
