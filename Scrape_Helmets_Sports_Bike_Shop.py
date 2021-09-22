
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import date
from selenium.webdriver.common.by import By
import random

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

df = pd.DataFrame(list_of_brands)
df.columns = ["Brand"]
file_name = "Brands "+str(today)+".csv"
print(file_name)
df.to_csv(file_name)

#**********************************************************************************************
# Get the list of Helmets that are for sale and the price

# connect to the URL
site_url = "https://www.sportsbikeshop.co.uk/motorcycle_parts/content_search?s=helmets"
driver.get(site_url)
soup = BeautifulSoup(driver.page_source, "html.parser")

#create a variable to loop through the 50 pages of reesults
page_num = 1
#declare the empty list to store the products
product_list = []

for page_num in range(1,50):
    if page_num == 1:
        time.sleep(random.randint(5,12))

    else:
        site_url = "https://www.sportsbikeshop.co.uk/motorcycle_parts/content_search?s=helmets&p=" + str(page_num)
        driver.get(site_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        time.sleep(random.randint(5,12))

    #print(site_url)

    item_list = soup.find_all(class_="product-card__main")

    for x in range(len(item_list)):
        prod_title = str(item_list[x].find(class_="product-card__title").text)
        prod_cost = str(item_list[x].find(class_="product-price").text)
        prod_cost_mod = prod_cost[2:]
        prod_tuple = () #clear the product list
        prod_tuple = (today, prod_title, prod_cost_mod)
        product_list.append(prod_tuple)
        print(len(product_list), prod_tuple)
        x = +1

    page_num =+1

driver.quit()
#print(product_list)
df_data = pd.DataFrame(product_list)
df_data.columns = ["Date", "Title", "Cost GBP"]
file_name = "SBS Helmets "+str(today)+".csv"
print(file_name)
df_data.to_csv(file_name)



