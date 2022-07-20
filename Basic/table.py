from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")

driver.get("file:///C:/Users/Young%20Stachu/Desktop/Python/Selenium/LosowaTabela.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr")) #count nuber of rows in the table

cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))  #count nuber of columns

print(rows)
print(cols)

print("Product      Article     Price")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end ='   ')
    print()













