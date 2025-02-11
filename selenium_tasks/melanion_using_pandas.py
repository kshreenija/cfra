from helpers import *
import requests
import pandas as pd
from io import StringIO
import requests
driver=get_driver()
url = "https://melanion.com/bitcoin-equities-etf/"
driver.get(url)

name_xpath = '//*[@id="companiesTable"]/tbody/tr'
ticker_xpath = '//*[@id="companiesTable"]/tbody/tr/td[2]'
country_xpath = '//*[@id="companiesTable"]/tbody/tr/td[3]'
weight_xpath = '//*[@id="companiesTable"]/tbody/tr/td[4]'
sector_xpath = '//*[@id="companiesTable"]/tbody/tr/td[5]'
isin_xpath = '//div[@class="data-row"][2]/div[1]/p[1]'
currency_xpath = '//div[@class="data-row"][2]/div[2]/p[1]'
as_of_date_xpath = '//div[@class="custom-date-container"]/span'

name = driver.find_elements(By.XPATH,name_xpath)
ticker = driver.find_elements(By.XPATH,ticker_xpath)
country = driver.find_elements(By.XPATH,country_xpath)
weight = driver.find_elements(By.XPATH,weight_xpath)
sector = driver.find_elements(By.XPATH,sector_xpath)
isin = driver.find_element(By.XPATH,isin_xpath)
currency = driver.find_element(By.XPATH,currency_xpath)
as_of_date=driver.find_element(By.XPATH,as_of_date_xpath)

data_list=[]
for i in range(len(name)):
    data_list.append({
        "constituent_name":name[i].text,
        "constituent_ticker":ticker[i].text,
        "country":country[i].text,
        "weight":weight[i].text,
        "sector":sector[i].text,
        "isin":isin.text,
        "currency":currency.text,
        "as_of_date":as_of_date.text.split(" ")[2]}) 

output_file = "melanion.csv"
headers = ["name","ticker","country","weight","sector","isin","currency","as_of_date"] 

write_to_csv(output_file,headers,data_list) 


etf_data=[]
etf_file_path = '/home/shreenija/Downloads/Melanion Capital_etf.csv'
etf_reader = pd.read_csv(etf_file_path)
for row in etf_reader:
    etf_data.append(row)
print(etf_reader)    


nav_aum_url = "https://melanion.com/wp-content/uploads/documents/Nav-Aum-Heading.csv"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(nav_aum_url, headers=headers)

if response.status_code == 200:
    csv_data = StringIO(response.text)  # Convert text to file-like object
    nav_reader = pd.read_csv(csv_data)
    nav_reader.to_csv("nav_aum.csv", index=False)
