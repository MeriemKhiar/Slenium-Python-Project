# Lancer le navigateur
# Acceder a http://www.google.ca# Taper selenium dans la barre de recherche
# selectionner le resultat de recherche selimium webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.ca/")

driver.find_element(By.NAME, "q").send_keys("selenium")

time.sleep(8)
recherche = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li/descendant::div[@class='wM6W7d']")

print(len(recherche))
for opt in recherche:
    print(opt.text)

for opt in recherche:
    if (opt.text == "selenium webdriver"):
        opt.click()
        break

