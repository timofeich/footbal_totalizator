import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.get("https://www.championat.com/football/_euro/tournament/5754/calendar/")
driver.maximize_window()
driver.implicitly_wait(5)
last_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

try:        

    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, 
        '//table[@class="table table-stripe-with-class table-row-hover stat-results__table _is-active"]')))
finally:        
    print('loaded')

all = elem.text.split("\n")
rest_info = [] 
for i in all[1:]: #i is a row
    print(i)
        #finally we append the infos to the list (for each row) 

#df = pd.DataFrame(rest_info, columns=
#    ['Event_type','Issued_time','Country','Areas','Regions','Date'])
#df.to_csv("scraped_weather.csv",mode='a', index=False,header=False)