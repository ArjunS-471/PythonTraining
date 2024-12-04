#Create a menu drivern program to take a movie name from the user and get its rating using selenium from an online source (imdb/rotten totamto/google) and other details
#The menu should have options for getting rating, writing all ratings to a file
#When he presses for quit the program, you need write all the movies and ratings that the user had asked in the session to a file
#Create components - e.g., 
#   1.First create a selenium program to do this and then make it menu driven
#   2.Later write to file
#   3.Store all searches in a container (list/dict) and then write to file

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

imdb = {}

driver_path = r'geckodriver.exe'

service = Service(driver_path)

driver = webdriver.Firefox(service = service)
driver.maximize_window()
driver.get("https://www.imdb.com/")

userInput = ""
while userInput != 2:
    print ("Choose a number from below - \n1. Enter a movie name\n2. Exit")
    
    try:
        userChoice = int(input())

        if userChoice == 1:
            print("Enter a movie name")
            ans = input()
            #imdb[ans] = ans

            #Searching movie name
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys(ans)
            driver.implicitly_wait(3)
            #Suggestion click
            result_suggestion = driver.find_element(By.XPATH, """//*[@id="react-autowhatever-navSuggestionSearch--item-0"]/a""")
            result_suggestion.click()
            #Trivia
            plot = driver.find_element(By.CLASS_NAME, "ipc-html-content-inner-div")
            #print(plot.text)
            imdb[ans] = plot.text
            driver.implicitly_wait(3)
            driver.back()

        elif userChoice == 2:
            print("Exiting app")
            for keys, values in imdb.items():
                print(keys, values)
            break         
        else:
            print("Enter correct choice")
    
    except Exception as e:
        print("Error -", e,"\nEnter correct choice")
        print()

with open('imdb.txt', 'w') as imdbfile:
    imdbfile.write(json.dumps(imdb))
