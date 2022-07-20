from selenium import webdriver


driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("http://www.newtours.demoaut.com/")

driver.save_screenshot(r"C:\Users\Young Stachu\Desktop\Python\miejsce na syf\Screenshot.png")

driver.get_screenshot_as_file(r"C:\Users\Young Stachu\Desktop\Python\miejsce na syf\Screenshot1.jpg")






