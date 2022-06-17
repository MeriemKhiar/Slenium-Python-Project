from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")
drop_Country = driver.find_element(By.ID,"input-country")

country = Select(drop_Country)

#country.select_by_visible_text("Algeria")
# country.select_by_index(3)
country.select_by_value("3")
all_option=country.options
total_option = len(all_option)
print("le nombre total de country :", total_option)
# for opt in all_option:
#     print(opt.text)
for opt in all_option:
    if opt.text == "Canada" :
        opt.click()
        break

