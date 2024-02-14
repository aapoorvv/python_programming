from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
# driver.get("https://www.amazon.in/Bluetooth-Tribit-Upgraded-Portable-Waterproof/dp/B078S4P3J9/ref=sr_1_2_sspa?crid=1MY8B9W4FYOKI&keywords=speaker&qid=1706963334&sprefix=speake%2Caps%2C217&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price)

driver.get("https://www.python.org")
# searchbar = driver.find_element(By.NAME, "q")
# print(searchbar)

# print(searchbar.get_attribute("placeholder"))

# submit_website_bug = driver.find_element(By.XPATH,"//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(submit_website_bug.get_attribute("href"))

dates = driver.find_elements(By.CSS_SELECTOR,".event-widget time") 
events = driver.find_elements(By.CSS_SELECTOR,".event-widget li a") 
print(events)
dict = {}
for n in range(len(dates)):
    dict[n]={
        "time":dates[n].text,
        "event":events[n].text
    }
print(dict)

# driver.close()
# driver.quit()