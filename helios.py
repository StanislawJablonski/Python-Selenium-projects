from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#dodawanie adBlocka
path_to_extension = r'C:\Users\Young Stachu\Desktop\Python\miejsce na syf\3.61.1_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
#driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.create_options()


driver = webdriver.Chrome(chrome_options=chrome_options ,executable_path = "C:\Windows\chromedriver.exe")
driver.create_options()

driver.get("https://www.helios.pl/49,Gdansk/StronaGlowna/")

driver.maximize_window()
time.sleep(3)


driver.find_element_by_xpath('//*[@id="page-header"]/div/nav/ul/li[1]/a').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="page-view"]/section/ul/li[3]/div[2]/div[3]/ul/li[2]/a').click()
time.sleep(2)

driver.find_element_by_link_text("Rezerwuj / Kup bilet").click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="6fb84b50-dce2-4d77-b751-5ffdaba35014"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="seats-container"]/div[3]/div[6]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="btnbuy"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="btnnext"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="User_Firstname"]').send_keys("Panie poruczniku melduje")
driver.find_element_by_xpath('//*[@id="User_Lastname"]').send_keys("ze pierwsza wersja programu kupujacego bilet do kina")
driver.find_element_by_xpath('//*[@id="User_Email"]').send_keys("wlasnie zostala napisana woho")

time.sleep(4)
driver.quit()
