import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
from selenium.webdriver.common.by import By

# Declare global variables
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
today = date.today()

#**********************************************************************************************
# Get the list of Helmet brands from https://www.sportsbikeshop.co.uk/motorcycle_parts/brands
site_url = "https://www.sportsbikeshop.co.uk/motorcycle_parts/brands"
driver.get(site_url)
#driver.maximize_window()
driver.implicitly_wait(5)

#Find the elements of the URL that contain the brands using XPATH
brand_list = driver.find_elements(By.XPATH,"//img[contains(@class, 'lazy tablet-l')]")

#declare the empty list to hold the brands
list_of_brands = []

#loop through the brands and identify then alt attribute which includes the brand text
for brand in brand_list:
    brand_string = brand.get_attribute('alt')
    if "Helmets" in brand_string: #find the suppliers that have helmet in the string
        include_in_list = True
    else:
        include_in_list = False

    #if the brand included helmet in the description, include it into the table
    if len(brand_string) > 0 and include_in_list == True:
        list_of_brands.append(brand_string[0:-8]) #exclude the last 9 characters which are 'Helmets'
        print("Brand", brand_string, "Brand [0:-8]", brand_string[0:-8])

#print("*"*50)
#print("Total elements:", len(brand_list), " **** Total Brands:", len(list_of_brands))

driver.quit()

df = pd.DataFrame(list_of_brands)
df.columns = ["Brand"]
file_name = "Brands "+str(today)+".csv"
print(file_name)
df.to_csv(file_name)


