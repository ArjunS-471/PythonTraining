#Multiple companies in single list, loop and download in same folder
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = r'geckodriver.exe'

service = Service(driver_path)

dict = {
    'Reliance' : "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI",
    'Swiggy':'https://www.moneycontrol.com/india/stockpricequote/online-services/swiggy/SL24',
    'SBI':'https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI',
    'MRF':'https://www.moneycontrol.com/india/stockpricequote/tyres/mrf/MRF',
    'Ola':'https://www.moneycontrol.com/india/stockpricequote/auto-ancillaries-brakes/olaelectricmobility/OEM'
}

driver = webdriver.Firefox(service = service)
driver.maximize_window()

for d in dict:
    driver.get(dict[d])
    driver.implicitly_wait(5)

    driver.refresh()
    time.sleep(5)
    driver.refresh()

    navElement = driver.find_element(By.ID,"advchart")
    driver.implicitly_wait(2)
    time.sleep(1)
    navElement.screenshot(d + '.png')
    time.sleep(2)