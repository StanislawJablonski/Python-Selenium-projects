from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": r"C:\Users\Young Stachu\Desktop\Python\miejsce na syf"})

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe",chrome_options=chromeOptions)



driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#Download text file
driver.find_element_by_id("textbox").send_keys("testing download text file")

driver.find_element_by_id("createTxt").click()  #generate text file

driver.find_element_by_id("link-to-download").click()  #download link

#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("testing download pdf XD")

driver.find_element_by_id("createPdf").click()

driver.find_element_by_id("pdf-link-to-download").click()

driver.close()




