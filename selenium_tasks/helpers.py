from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = "/home/shreenija/Downloads/chromedriver-linux64/chromedriver"

def get_driver():
    executable_path = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=executable_path)

    # chrome_options = Options()
    # chrome_options.add_experimental_option("prefs", {
    #     "download.default_directory": "/home/shreenija/cfra/selenium_tasks/myetf",
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing.enabled": True
    # })

    return driver

def write_to_csv(output_file, headers, data_list):
    with open(output_file, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_list)
    print(f"File saved to {output_file}")

def write_to_csv_using_pandas(output_file, headers, data_list):
    df = pd.DataFrame(data_list, columns=headers)  
    df.to_csv(output_file, index=False) 
    print(f"File saved to {output_file}")
