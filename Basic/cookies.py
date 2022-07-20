from selenium import webdriver


driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("https://www.amazon.com/")

#Capture all the cookies  created by browser
cookies = driver.get_cookies()
print(len(cookies)) #print number of cookies  have been created
print(cookies)   #print all the cookie pairs

#Adding new cookie to the browser
cookie = {'name': 'Mycookie','value': '1234567890'}
driver.add_cookie(cookie)

#Capture all the cookies  created by browser
cookies = driver.get_cookies()
print(len(cookies)) #print number of cookies after adding new cookie
print(cookies)   #print all the cookie pairs

#Deleting cookie
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print(len(cookies)) #print number of cookies after deleting a cookie
print(cookies)   #print all the cookie pairs


driver.delete_all_cookies()







