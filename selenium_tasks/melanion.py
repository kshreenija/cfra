from helpers import *
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
    data_list.append({"name":name[i].text,
                      "ticker":ticker[i].text,
                      "country":country[i].text,
                      "weight":weight[i].text,
                      "sector":sector[i].text,
                      "isin":isin.text,"currency":currency.text,"as_of_date":as_of_date.text.split(" ")[2]}) 

output_file = "melanion.csv"
headers = ["name","ticker","country","weight","sector","isin","currency","as_of_date"] 

write_to_csv(output_file,headers,data_list) 



etf_file_path = '/home/shreenija/Downloads/Melanion Capital_etf.csv'
etf_data=[]
with open(etf_file_path , mode="r" ) as etf_file:
    reader= csv.DictReader(etf_file)
    for row in reader:
        etf_data.append(row)      


nav_aum_url = "https://melanion.com/wp-content/uploads/documents/Nav-Aum-Heading.csv"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(nav_aum_url, headers=headers)
with open("nav_aum.csv", "wb") as file:
    file.write(response.content)

  

final_data=[]
with open("nav_aum.csv",mode="r") as nav_file:
    nav_reader=csv.DictReader(nav_file)
    for nav_row in nav_reader:
        for etf_row in etf_data:
            if isin.text==etf_row['isin']:
                final_data.append({
                    "firstbridge_id": etf_row["firstbridge_id"],
                    "date": nav_row["Date"], 
                    "NAV": nav_row["NAV"],
                    "AUM":float(nav_row["AUM"])*100000,
                })               
with open("melanion_single_mapping.csv",mode="w") as final_csv:
    writer=csv.DictWriter(final_csv,fieldnames=['firstbridge_id', 'date','NAV','AUM'])
    writer.writeheader()
    for row in final_data:
        writer.writerow(row)

driver.quit() 




