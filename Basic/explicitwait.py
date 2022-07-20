from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

#driver.find_element_by_id("tab-flight-tab-hp")+.click()    #to samo co linijke pod
driver.find_element(By.ID,'tab-flight-tab-hp').click()				#flights button


driver.find_element(By.ID,'flight-origin-hp-flight').send_keys("SFO")  #origin

time.sleep(2)

driver.find_element(By.ID,'flight-destination-hp-flight').send_keys("NYC")	#destination


driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("11/10/2019")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("11/31/2019")

driver.find_element(By.XPATH,'//*[@id="gcw-flights-form-hp-flight"]/div[7]/label/button').click()

#Explicit waits
wait = WebDriverWait(driver,10)

#driver.find_element(By.XPATH,'//*[@id="stopFilter_stops-0"]')
element =  wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="stopFilter_stops-0"]')))      #expected conditions to sie nazywa xd
element.click()

time.sleep(3)

driver.quit()






