import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.get("https://www.championat.com/football/_euro.html")
driver.maximize_window()
driver.implicitly_wait(3)
last_game_button = driver.find_element(By.CLASS_NAME, 
    "tabs-item _primary _accordion js-tournament-tab")
last_game_button.click()
try:        

    elem = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, 
        "table-row-hover stat-results__table table-stripe dpyjeh js-results-table-rates-parent table")))
finally:        
    print('loaded')

soup = BeautifulSoup(driver.page_source, 'html.parser')  
all = soup.findAll("tbody")[2] #the <tbody> we want is the third one
rows = all.findAll('td')

rest_info = [] # empty array populated with the info of each rowfor i in rows: #i is a row
for i in rows: #i is a row
        infos_row = i.findAll('td')   # get the info of a single row
        for index, j in enumerate(infos_row): #j is a col of row i 
            info = None
            if index == 0: #in this case the first col has the event information
                info = j.find('span') #the info is within a span
                event = info.text #we extract the text from the span            if index == 4:
                info = j.find('span')
                areas = info.text            
            if index == 1:
                issued_time = j.text
            if index == 3:
                country = j.text            
            if index == 5:
                regions = j.text            
            if index == 2:
                continue
        #finally we append the infos to the list (for each row) 
        rest_info.append([event,issued_time,country,areas,regions])

df = pd.DataFrame(rest_info, columns=
    ['Event_type','Issued_time','Country','Areas','Regions','Date'])
df.to_csv("scraped_weather.csv",mode='a', index=False,header=False)