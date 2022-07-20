from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

actions = ActionChains(driver)

actions.context_click(button).perform()       #right click action





