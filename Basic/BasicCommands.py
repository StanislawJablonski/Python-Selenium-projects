from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("https://www.google.pl/")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()  #znajduje po xpath i klika element, uwaga na apostrofy

time.sleep(5)

 #driver.close()     #currently focussed browser

 driver.quit()   #closes all the browsers

 