from bs4 import BeautifulSoup
import requests
#asdghaksh


def scape():
    d = { }
    URL = "https://m.manganelo.com/manga-hm121832"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    title = soup.find('h1')
    d['title'] = title.text

    chapters = soup.find_all('div', class_ = "panel-story-chapter-list")
    for chapter in chapters:
        chapter_num = chapter.find('a', {'class':'chapter-name'})
        d['chapter'] = chapter_num.text
        
    return d

scape()
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options


# PATH = "C:\src\chromedriver.exe"
# from database import generateDB
# #get number 
# def getNum():
#     num = []
#     chap = chapterNum.split()
#     for item in chap:
#         for subitem in item:
#             if subitem.isdigit():   
#                 num.append(subitem)
#     res = int("".join(num))
#     return res
# # Get data 
# def getManga():
    
#     #start browser
# chrome_options = Options()
# chrome_options.headless = True
# driver = webdriver.Chrome(PATH, options = chrome_options)
#     print("Openings browser")
#     #go to X site
# driver.get("https://modesto.craigslist.org/")


#     print("Made it to site")
#     #begin finding elements that you want. 

#     global title, chapterNum, URL
#     title = driver.find_element_by_tag_name('h1').text
    
#     chapters = driver.find_elements_by_css_selector('a[class *= \'chapter-name text-nowrap\']')
#     print("GOT elements")
#     for chapter in chapters:
#         URL = chapter.get_attribute('href')
#         chapterNum = chapter.text
#         print(title + " " + URL + " " + str(getNum()))
#         generateDB(title, getNum(), getNum())
        
    # import database
# time.sleep(1)
# driver.close()
# driver.quit()
    

# if __name__ == "__main__":
    
# # Enter new manga to be tracked 
#     mangaURL = input('URL')
#     getManga()
