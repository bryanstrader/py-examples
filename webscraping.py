import os
from selenium import webdriver

# load chrome driver
chromedriver = 'C:\\Users\\Bryan\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

# fetch a url
driver.get('https://phoenix.craigslist.org/')

forsale = driver.find_element_by_xpath('''//*[@id="sss"]/h4/a''')

forsale.click()

forsale_items = driver.find_elements_by_class_name('result-title')

for item in forsale_items:
    print(item.text)