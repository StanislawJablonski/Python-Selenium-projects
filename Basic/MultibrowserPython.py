from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("https://www.google.pl/")

print(driver.title)  #title of the page

print(driver.current_url)  # returns URL of the page

print(driver.page_source)   # HTML code of the page




driver.close()  #closing browser



