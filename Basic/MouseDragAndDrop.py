from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_element = driver.find_element_by_xpath('//*[@id="box6"]')
target_element = driver.find_element_by_xpath('//*[@id="box106"]')

actions = ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()   #drag and drop










