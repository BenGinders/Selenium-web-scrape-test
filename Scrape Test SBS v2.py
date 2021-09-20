
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time


path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.sportsbikeshop.co.uk/motorcycle_parts/content_search?s=helmets")

time.sleep(2)

page_title = driver.title

main_results = driver.find_element_by_class_name("ais-Hits")
print(1, main_results.text)

results = main_results.find_elements_by_tag_name('li')
print( len(results))

i = 0

for i in range(len(results)):
    product = results[i].find_element_by_tag_name('product-card__main')
    print("Item: ", i, product.text)


##prod_wrap > div.product-grid.product-grid--wide.spin-group > div > div > ol > li:nth-child(2) > div > div.product-card__main > div.product-card__stars.stars > a

