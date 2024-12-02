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


hdng = driver.find_element(By.CLASS_NAME, "adv_arw")
#actions = ActionChains(driver)
#actions.move_to_element(hdng).perform()
driver.execute_script("arguments[0].scrollIntoView();",hdng)
driver.execute_script("arguments[0].scrollIntoView();",hdng)
driver.execute_script("arguments[0].scrollIntoView();",hdng)
driver.implicitly_wait(10)
#time.sleep(20)
driver.save_screenshot("ShareMarketChart.jpg")
driver.implicitly_wait(10)
#time.sleep(10)
print('Done')

#driver.implicitly_wait(10)
time.sleep(10)

driver.quit()