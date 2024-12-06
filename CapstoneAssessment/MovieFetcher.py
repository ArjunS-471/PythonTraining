import streamlit as st
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

#Movie list to be shown in the webpage as a drop down
MovieList = [
    'Godfather','Inception','Interstellar','Fight Club','Seven Samurai', 'Metropolis', 'The General', '12 Angry Men'
]

def MovieReviewFetch(Movie):
    print ('Movie fetch task starting -',Movie)
    driver_path = r'geckodriver.exe'

    service = Service(driver_path)

    driver = webdriver.Firefox(service = service)
    driver.maximize_window()
    driver.get("https://www.rottentomatoes.com/")
    #Search box
    search_box = driver.find_element(By.XPATH, """//*[@id="header-main"]/search-results-nav/search-results-controls/input""")
    search_box.send_keys(Movie)
    driver.implicitly_wait(1)
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)
    #From result list
    result_suggestion = driver.find_element(By.XPATH, """//*[@id="search-results"]/search-page-result[1]/ul/search-page-media-row[1]/a[2]""")
    result_suggestion.click()
    driver.implicitly_wait(3)
    #Extract 4 movie parameters
    ReviewT = driver.find_element(By.XPATH, """//*[@id="modules-wrap"]/div[4]/section/div[2]/carousel-slider/media-review-card-critic[1]/drawer-more/rt-text""")
    ReviewText = ReviewT.text
    print('Review -',ReviewT.text)
    Tomatometer = driver.find_element(By.XPATH, """//*[@id="modules-wrap"]/div[1]/media-scorecard/rt-text[1]""")
    TomatometerText = Tomatometer.text
    print('Tomatometer -',Tomatometer.text)
    Popcornmeter = driver.find_element(By.XPATH, """//*[@id="modules-wrap"]/div[1]/media-scorecard/rt-text[3]""")
    PopcornmeterText = Popcornmeter.text
    print('Popcornmeter -',Popcornmeter.text)
    CriticsConsensus = driver.find_element(By.XPATH, """//*[@id="critics-consensus"]/p""")
    CriticsConsensusText = CriticsConsensus.text
    print('CriticsConsensus -',CriticsConsensus.text)
    review = []
    review.append(ReviewText)
    review.append(TomatometerText)
    review.append(PopcornmeterText)
    review.append(CriticsConsensusText)
    driver.quit()
    #Return the list
    return review
    
#Streamlit section
st.title("Movie Review Fetcher")
option = st.selectbox(
        "Select movie name from the following list - ",MovieList)
st.write("You selected:", option)
#Click search button to initiate search
if st.button("Search"):
    #Progress animation
    with st.spinner("Please wait while data is being fetched"):
        output = []
        output = MovieReviewFetch(option)
    #Result
    st.write("Review:", output[0])
    st.write("Tomatormeter:", output[1])
    st.write("Popcornmeter:", output[2])
    st.write("Critics Consensus:", output[3])