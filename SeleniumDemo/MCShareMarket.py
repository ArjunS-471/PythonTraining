from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)
driver.maximize_window()
driver.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")
driver.implicitly_wait(5)

driver.refresh()
time.sleep(5)
driver.refresh()

navElement = driver.find_element(By.ID,"advchart")
driver.implicitly_wait(5)
time.sleep(5)
navElement.screenshot('test.jpg')
time.sleep(2)