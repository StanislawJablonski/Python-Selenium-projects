from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Windows\chromedriver.exe")

driver.get("http://www.newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links: ",len(links))

for link in links:
    print(link.text)

#clicking on the link
#driver.find_elements(By.LINK_TEXT,"REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()



