from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get('http://www.newtours.demoaut.com/')

user_ele = driver.find_element_by_name("userName")
print(user_ele.is_displayed())   #returns true/false based on element status
print(user_ele.is_enabled())     # returns true/false

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())   #returns true/false based on element status
print(pwd_ele.is_enabled())     # returns true/false

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("status of round trip radio button ",roundtrip_radio.is_selected())   #print status of radio button round trip

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("status of one trip radio button ",onetrip_radio.is_selected())


driver.quit()

