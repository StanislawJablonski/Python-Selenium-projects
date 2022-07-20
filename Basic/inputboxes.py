from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Windows\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


#  1) How to find how many inputboxes are in web page

inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')

print(len(inputboxes))    #8

#  2) How to provide value into text box

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Stanislao")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Jabloa")
driver.find_element_by_id("RESULT_TextField-3").send_keys("333333333")

#  3) How to get the status

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Displayed or not: ", status)

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("Enabled or not: ", status)

