# # headers = ["name","ticker","country","weight","sector","isin","currency","as_of_date"] 
# # import requests
# # nav_aum_url = "https://melanion.com/wp-content/uploads/documents/Nav-Aum-Heading.csv"
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# # }
# # respose=requests.get(nav_aum_url,headers=headers)
# # with open("nav_aum_url.csv" , mode="wb")as file:
# #     file.write(respose.content)
# # import csv

# # etf_file_path = '/home/shreenija/Downloads/Melanion Capital_etf.csv'
# # etf_data=[]
# # with open(etf_file_path , mode="r" ) as etf_file:
# #     reader= csv.DictReader(etf_file)
# #     for row in reader:
# #         etf_data.append(row)
# import pandas as pd


# # Define the file path
# etf_file_path = '/home/shreenija/Downloads/Melanion Capital_etf.csv'

# # Read the CSV file into a DataFrame
# etf_data = pd.read_csv(etf_file_path)

# # etf_data.to_csv('outputssss.csv', index=False)


# import pandas as pd

# # URL of the CSV file
# import pandas as pd
# import requests
# from io import StringIO

# # URL of the CSV file
# nav_aum_url = "https://melanion.com/wp-content/uploads/documents/Nav-Aum-Heading.csv"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# # Send GET request to fetch the CSV content
# response = requests.get(nav_aum_url, headers=headers)

# # Convert the response content to a pandas DataFrame
# if response.status_code == 200:
#     csv_data = StringIO(response.text)  # Convert text to file-like object
#     etf_data = pd.read_csv(csv_data)  # Read CSV content into DataFrame

#     # Save it as a local CSV file without an index
#     etf_data.to_csv("nav_aum.csv", index=False)

# import pandas as pd

# # Load the scraped ISIN value from CSV
# isin_df = pd.read_csv("scraped_isin.csv")  # Assuming this file contains the scraped ISIN
# isin_value = isin_df["isin"].iloc[0]  # Extract the first ISIN value (modify if needed)

# # Load ETF data (which contains the ISIN column)
# etf_df = pd.read_csv("etf_data.csv")

# # Load NAV data
# nav_df = pd.read_csv("nav_aum.csv")

# # Filter etf_df where 'isin' matches the scraped ISIN
# etf_filtered = etf_df[etf_df["isin"] == isin_value]

# # Ensure both DataFrames have the same index for .join()
# etf_filtered.set_index("firstbridge_id", inplace=True)
# nav_df.set_index("Date", inplace=True)

# # Perform join
# final_df = nav_df.join(etf_filtered, how="inner")

# # Select relevant columns
# final_df = final_df[["firstbridge_id", "NAV", "AUM", "currency"]]

# # Convert AUM to the required format
# final_df["AUM"] = final_df["AUM"].astype(float) * 100000

# # Reset index if needed
# final_df.reset_index(inplace=True)

# # Display the first few rows
# print(final_df.head())

# # Save the final DataFrame
# final_df.to_csv("final_data.csv", index=False)

# yesterday = (datetime.today() - timedelta(days=1)).strftime("%d-%m-%Y")



# def function(a,b=None):
#     if b is None:
#         b=6   
#     return a*b
# result=function(5)
# print(result)


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
CHROMEDRIVER_PATH = "/home/shreenija/Downloads/chromedriver-linux64/chromedriver"
executable_path = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=executable_path)


# driver=get_driver()
input_file = "https://www.eq8.com.my/eq8-dow-jones-us-titans-50-etf"  
driver.get(input_file)
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