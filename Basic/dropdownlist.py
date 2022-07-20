from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path = "C:\Windows\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

#select by visible text
drp.select_by_visible_text("Morning")  #morning

#select by index number
drp.select_by_index(2) #afternoon

#select by value
drp.select_by_value("Radio-2")

#Count number of options
print(len(drp.options))


#Capture all options and print as output

all_options = drp.options

for option in all_options:
    print(option.text)

