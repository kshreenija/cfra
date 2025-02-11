from helpers import * 

driver = get_driver() 
url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
driver.get(url)

prod_name_xpath='//div[@class="yKfJKb row"]/div/div[@class="KzDlHZ"]'
prod_price_xpath='//div[@class="yKfJKb row"]/div/div[@class="KzDlHZ"]/../../div[2]/div[1]/div[1]/div[1]'
prod_specs_xpath='//div[@class="yKfJKb row"]/div/div[@class="KzDlHZ"]/../../div[1]/div/ul/li[1]'

product_names=driver.find_elements(By.XPATH,prod_name_xpath)
data_list=[]
for product in product_names:
    product_price=product.find_element(By.XPATH,'../../div[2]/div[1]/div[1]/div[1]').text
    product_specs=product.find_element(By.XPATH,'../../div[1]/div/ul/li[1]').text
    data_list.append({"name":product.text,"price":product_price,"specs":product_specs})
print(data_list)    


# data_list=[]
# for i in range(len(prod_name)):
#     data_list.append({"name":prod_name[i].text,"price":prod_price[i].text,"specs":prod_specs[i].text}) 

output_file = "flipkart.csv"
headers=["name","price","specs"]

write_to_csv(output_file, headers, data_list)
# write_to_csv_using_pandas(output_file,headers,data_list)
