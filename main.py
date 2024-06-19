import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np

number_of_matches = 36
driver = webdriver.Chrome()
driver.get("https://www.championat.com/football/_euro/tournament/5754/calendar/")
driver.maximize_window()
driver.implicitly_wait(5)
last_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

try:        
    results_table = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, 
        '//table[@class="table table-stripe-with-class table-row-hover stat-results__table _is-active"]')))
finally:        
    print('loaded')

results = results_table.text.split("\n")
matches = np.array_split(results[1:], number_of_matches)
for match in matches:
    date = match[0].split(" ")
    print("date of the match: ", date[3])#date of the match 
    print("time of the match: ", date[5])#time of the match
    countries = match[1].split(" ")
    print("home country: ", countries[0])#home country
    print("away country: ", countries[2])#away country
    score = match[2].split(" ")
    print("Home team score: ", score[0])
    print("Away team score: ", score[2])

