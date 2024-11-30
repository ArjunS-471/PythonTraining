from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)

driver.get("https://www.github.com/login")
#driver.get("https://practicetestautomation.com/practice-test-login/")
#driver.manage().window().maximize()
#search_box = driver.find_element(By.ID, "login_field")
search_box = driver.find_element(By.CLASS_NAME, "js-login-field")
search_box.send_keys("student")
search_box = driver.find_element(By.CLASS_NAME, "js-password-field")
search_box.send_keys("Password123")
#search_box.send_keys(Keys.RETURN)
#search_box = driver.find_element(By.ID, "submit")
#search_box.click()

#Selenium specific instruction
#driver.implicitly_wait(5)

#print("Title:", driver.title)

#Program specific instruction
time.sleep(10)

driver.quit()