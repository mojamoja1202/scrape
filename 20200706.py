from selenium import webdriver
import time
from bs4 import BeautifulSoup 

driver=webdriver.Chrome('chromedriver.exe')



# link to airitilibrary
driver.get("https://www.airitilibrary.com/")

#sleep 5s
time.sleep(5)

#keyin what i want in the input element
driver.find_element_by_id("ArticlesViewModel_SearchField").send_keys("data mining")

#press button
driver.find_element_by_id("images1").click()

time.sleep(6)

#get all code and put to beautifulsoup

soup=BeautifulSoup(driver.page_source,'html.parser')

#print(soup)


title=soup.find('td','titleB')

print('title:'+title.text)




#quit web
driver.quit()
