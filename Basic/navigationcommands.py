from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get('https://antyweb.pl/')

print(driver.title)



driver.get('https://www.onet.pl/')

print(driver.title) 

driver.back()
print(driver.title)

driver.forward()
print(driver.title)


driver.quit()