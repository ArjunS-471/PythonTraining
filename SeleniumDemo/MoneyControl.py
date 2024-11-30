from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)

driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")
driver.implicitly_wait(5)
driver.save_screenshot("ShareMarket.jpg")

link = driver.find_element(By.LINK_TEXT, "Zoroastrianism")
print(link)
print(link.text)
driver.get(link.get_attribute('href'))
driver.implicitly_wait(5)
driver.save_screenshot("zoropage.png")

print('Done')

driver.implicitly_wait(5)

driver.quit()