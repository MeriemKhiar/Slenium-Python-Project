# Test case
# 1 lancer le navigateur
# 2 accéder à l'application https://demo.nopcommerce.com/register?returnUrl=%2F
# 3 cliquer sur le lien register
# 4 remplir le formulaire
# 5 cliquer sur le bouton register
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 1 lancer le navigateur
driver = webdriver.Chrome()
driver.maximize_window()
# 2 accéder à l'application https://demo.nopcommerce.com/register?returnUrl=%2F
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
#3 cliquer sur le lien register
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_elements
# (By.PARTIAL_LINK_TEXT,"Regi").click()
driver.find_element(By.ID, "FirstName").send_keys("meriem")
driver.find_element(By.NAME, "LastName").send_keys("khiar")
driver.find_element(By.ID, "Email").send_keys("khiar@gmail.com")
driver.find_element(By.ID, "Password").send_keys("123456")
driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
driver.find_element(By.ID, "register-button").submit()
driver.find_element(By.CLASS_NAME,"ico-login").submit()
time.sleep(4)
driver.close()