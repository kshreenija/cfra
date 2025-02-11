from datetime import datetime
from datetime import timedelta
# from helpers import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# current_file = __file__
# print(current_file)

root = os.path.dirname(__file__)
download_folder = os.path.join(root, __file__.replace('.py', ''))
os.makedirs(download_folder, exist_ok=True)
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_folder,  #
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    }
options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(options=options)

CHROMEDRIVER_PATH = "/home/shreenija/Downloads/chromedriver-linux64/chromedriver"
executable_path = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=executable_path,options=options)


# driver=get_driver()
input_file = "https://www.eq8.com.my/eq8-dow-jones-us-titans-50-etf"  
driver.get(input_file)

# chrome_options = Options()
# chrome_options.add_experimental_option("prefs", {
#         "download.default_directory": "/home/shreenija/cfra/selenium_tasks/myetf",
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "safebrowsing.enabled": True
#     }) 

downloads_xpath='/html/body/div[9]/div/div/ul/li[3]/a'
element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,downloads_xpath))
    )
element.click()
driver.implicitly_wait(5)
date_dropdown_xpath='//*[@id="pills-fund_download"]/div/div/div/table[1]/tbody/tr[2]/td[2]/div/select'
date_options_xpath='//*[@id="pills-fund_download"]/div/div/div/table[1]/tbody/tr[2]/td[2]/div/select/option'
download_button_xpath='//*[@id="pills-fund_download"]/div/div/div/table[1]/tbody/tr[2]/td[2]/i'

dropdown_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,date_dropdown_xpath))  
)
dropdown_element.click()
download_button=driver.find_element(By.XPATH,download_button_xpath)

yesterday = (datetime.today() - timedelta(days=1)).strftime("%d-%m-%Y")  
date_options=driver.find_elements(By.XPATH,date_options_xpath)
for option in date_options:
        if option.text==yesterday:
            option.click()
            time.sleep(3)
            download_button.click() 
      
driver.quit()    