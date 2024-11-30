from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/India")

#links = driver.find_elements(By.TAG_NAME, "a")
link = driver.find_element(By.LINK_TEXT, "Zoroastrianism")
print(link)
print(link.text)

driver.get(link.get_attribute('href'))

driver.back()
driver.implicitly_wait(5)
driver.forward()
driver.implicitly_wait(5)

#for link in links:
#    print(link.text)

print('Done')

time.sleep(10)

driver.quit()