
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import date

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
#driver.get("https://www.sportsbikeshop.co.uk/motorcycle_parts/content_search?s=helmets")

today = date.today()
print(today)

page_num = 1

#soup = BeautifulSoup(driver.page_source, "html.parser")


product_list = []

for page_num in range(1,50):
    if page_num == 1:
        site_url = "https://www.sportsbikeshop.co.uk/motorcycle_parts/content_search?s=helmets"
    else:
        site_url = "https://www.sportsbikeshop.co.uk/motorcycle_parts/content_search?s=helmets&p=" + str(page_num)
    
    print(site_url)

    driver.get(site_url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
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
df = pd.DataFrame(product_list)
df.columns = ["Date", "Title", "Cost GBP"]
file_name = "Selenium-web-scrape-test\Files\SBS Helmets "+str(today)+".csv"
print(file_name)
df.to_csv(file_name)



