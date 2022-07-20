from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_name("RESULT_FileUpload-11").send_keys("C:/Users/Young Stachu/Desktop/Nowy dokument tekstowy.txt")
#w sciezce musza byc slashe a nie backslashe,








