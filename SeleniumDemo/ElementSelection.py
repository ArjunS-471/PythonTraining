from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)

driver.get("https://www.duckduckgo.com/")
#driver.get("https://www.google.com/")
#driver.get("https://www.imdb.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("John Wick")
search_box.send_keys(Keys.RETURN)

#Selenium specific instruction
#driver.implicitly_wait(5)

#print("Title:", driver.title)

#Program specific instruction
time.sleep(10)

driver.quit()