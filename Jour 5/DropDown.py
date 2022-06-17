from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")
drop_Country = driver.find_element(By.ID,"input-country")
#
country = Select(drop_Country)
#Selection par texte visible
# country.select_by_visible_text("Algeria")
# country.select_by_index(6)
country.select_by_value("3")
# recuperer toutes les options dans select
touteOption= country.options
totalOption = len(touteOption)
print("Le nombre total d'options:", totalOption)
# for opt in touteOption:
#     print(opt.text)
for opt in touteOption:
    if opt.text == "Canada":
        opt.click()
        break