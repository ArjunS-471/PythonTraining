from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
driver.implicitly_wait(3)

search_box = driver.find_element(By.XPATH, "//*[@id='searchInput']")
search_box.send_keys("India")
#search_box.send_keys(Keys.RETURN)
search_button = driver.find_element(By.XPATH, """//*[@id="search-form"]/fieldset/button/i""")
search_button.click()
driver.implicitly_wait(5)

#heading= driver.find_element(By.XPATH, "//h1[contains(text(), 'India')]")
heading= driver.find_element(By.XPATH, "//span[contains(text(), 'India')]")
print(heading)

heading2= driver.find_element(By.XPATH, "//h2[contains(text(), 'Etymology')]")
print(heading2.text)

driver.quit()