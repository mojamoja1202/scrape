from selenium import webdriver
import time

driver=webdriver.Chrome()



# link to airitilibrary
driver.get("https://www.airitilibrary.com/")

#sleep 5s
time.sleep(5)

#keyin what i want in the input element
driver.find_element_by_id("ArticlesViewModel_SearchField").send_keys("data mining")

#press button
driver.find_element_by_id("images1").click()

time.sleep(10)

#get one title
title=driver.find_element_by_xpath("//*[@id='oTable']/tbody/tr[1]/td[3]/p[1]/a").text

#print it
print(title)



#quit web
driver.quit()