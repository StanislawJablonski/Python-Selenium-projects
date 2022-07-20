import ExcelUtils
from selenium import webdriver


driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("http://www.newtours.demoaut.com/")

driver.maximize_window()

path = r"C:\Users\Young Stachu\Desktop\Python\miejsce na syf\Login1.xlsx"

rows = ExcelUtils.getRowCount(path,'Arkusz1')

for r in range(2,rows+1):
    username = ExcelUtils.readData(path, "Arkusz1", r, 1)
    password = ExcelUtils.readData(path, "Arkusz1", r, 2)

    driver.find_element_by_name('userName').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)


    driver.find_element_by_name('login').click()


    if driver.title=="Find a Flight: Mercury Tours:":
        print("test is passed")
        ExcelUtils.writeData(path,'Arkusz1',r,3,"Test passed")
    else:
        print("Test failed")
        ExcelUtils.writeData(path, 'Arkusz1', r, 3, "Test failed")

    driver.find_element_by_link_text("Home").click()

driver.quit()



