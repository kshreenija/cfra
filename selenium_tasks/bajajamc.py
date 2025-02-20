from datetime import date
from datetime import datetime
import calendar
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

root = os.path.dirname(__file__)
download_folder = os.path.join(root, __file__.replace('.py', ''))
os.makedirs(download_folder, exist_ok=True)
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_folder,  
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    }
options.add_experimental_option("prefs", prefs)

CHROMEDRIVER_PATH = "/home/shreenija/Downloads/chromedriver-linux64/chromedriver"
executable_path = Service(CHROMEDRIVER_PATH)

driver = webdriver.Chrome(service=executable_path,options=options)
url = 'https://www.bajajamc.com/downloads?portfolio'
driver.get(url)

monthly_portfolio_xpath='//div[@class="view-footer"]/button[1]'
select_year_xpath='//*[@id="edit-term-node-tid-depth--19--level-0"]'
select_month_xpath='//*[@id="edit-term-node-tid-depth--19--level-1"]'
download_xpath='//*[@id="quicktabs-tabpage-downloads_disclosure_tabs-4"]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/span/a'


monthly_portfolio_button = driver.find_element(By.XPATH, monthly_portfolio_xpath)
monthly_portfolio_button.click()
time.sleep(3)

select_year_dropdown=driver.find_element(By.XPATH,select_year_xpath)
all_options=select_year_dropdown.find_elements(By.CLASS_NAME,"has-children")
for option in all_options:
    if option == "2024-25":
        option.click()
today_date = datetime.today()
if today_date.month == 1:
    previous_month = 12
else:
    previous_month = today_date.month-1
    previous_month_name=calendar.month_name[previous_month]

select_month_dropdown=driver.find_element(By.XPATH,select_month_xpath)
options=select_month_dropdown.find_elements(By.XPATH,'//select[@id="edit-term-node-tid-depth--19--level-1"]/option')
for option in options:
    if option.text == previous_month_name:
        option.click()
time.sleep(3)
download_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,download_xpath)))
dowloaded_file=download_button.click()
time.sleep(10)  

driver.quit()


    
