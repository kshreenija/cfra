from helpers import *
import time
driver=get_driver()
url="https://www.edelweiss.in/oyo/equity/top-long-term-stock-recommendations"
driver.get(url)
midcap_stocks='//div[@class="ed-tab-heading forScroll ng-scope"]/ul/li[2]'
element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,midcap_stocks))
    )
# driver.implicitly_wait(5) 
# midcap_stocks_button=driver.find_element(By.XPATH,midcap_stocks)
element.click()
driver.implicitly_wait(5) 
reco_date='//label[@class="ed-lbl date ng-binding"]'
stock='//div[@class="stock-name ed-cell all"]/a'
current_price='//div[@class="trw raw allrecos remBelowPadding"]/label[1]'
target_price='//div[@class="trw raw allrecos remBelowPadding"]/label[2]'
market_cap='//div[@class="trw raw allrecos remBelowPadding"]/label[4]/label[1]'
sector='//div[@class="trw raw allrecos remBelowPadding"]/label[5]'

reco_date=driver.find_elements(By.XPATH,reco_date)
stock=driver.find_elements(By.XPATH,stock)
current_price=driver.find_elements(By.XPATH,current_price)
target_price=driver.find_elements(By.XPATH,target_price)
market_cap=driver.find_elements(By.XPATH,market_cap)
sector=driver.find_elements(By.XPATH,sector)

data_list=[]
for i in range(len(reco_date)):
    data_list.append({"reco_date":reco_date[i].text.replace("\n", " "),
                      "stock":stock[i].text.replace("\n", " "),
                      "current_price":current_price[i].text.replace("\n", " "),
                      "target_price":target_price[i].text.replace("\n", " "),
                      "market_cap":market_cap[i].text.replace("\n", " "),
                      "sector":sector[i].text.replace("\n", " ")})
    
output_file="edelweiss.csv" 
headers=["reco_date","stock","current_price","target_price","market_cap","sector"]
write_to_csv(output_file,headers,data_list)
driver.quit()