from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)
#driver.maximize_window()

driver.get("https://demo.guru99.com/test/delete_customer.php")

search_box = driver.find_element(By.NAME, "cusid")
search_box.send_keys("arjun")
search_box.send_keys(Keys.RETURN)

#handle an alert
alert = driver.switch_to.alert

print("Alert text:", alert.text)
alert.accept()

search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(5)