from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# no_of_articles = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# # no_of_articles.click()
# print(no_of_articles.text)

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# # all_portals.click()

# search = driver. find_element (By.NAME, value="search")
# search.send_keys("Python",Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME,"fName")
lname = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")

fname.send_keys("Apoorv",Keys.ENTER)
lname.send_keys("Gupta",Keys.ENTER)
email.send_keys("abcd@email.com",Keys.ENTER)
