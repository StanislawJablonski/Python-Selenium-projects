from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)

actions.double_click(element).perform()









