from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle) #CDwindow-D865B169F9C5A5C9786B7426D8409901 - parent window

handles = driver.window_handles   #return all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()  # close only  parent browser

driver.quit()


