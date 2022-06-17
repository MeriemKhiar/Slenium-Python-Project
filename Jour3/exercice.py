# Test case
# 1 lancer le navigateur
# 2 accéder à l'application https://www.saucedemo.com/
# 3 Entrer username (standard_user)
# 4 Entrer password (secret_sauce)
# 5 cliquer sur le lien Login
# 6 cliquer sur le lien Add a la carte
# 7 cliquez sur le panier
# 8 cliquez sur Remove
import time

from selenium import webdriver

# 1 lancer le navigateur
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

# 2 accéder à l'application https://www.saucedemo.com/
driver.get("https://www.saucedemo.com/")

# 3 Entrer username (standard_user)
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# 4 Entrer password (secret_sauce)
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# 5 cliquer sur le lien Login
driver.find_element(By.ID, "login-button").submit()

# 6 cliquer sur le lien Add a la carte

driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

 # 7 cliquez sur le panier
driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
#
# 8 cliquez sur Remove

driver.find_element(By.NAME, "remove-sauce-labs-bolt-t-shirt").click()

driver.find_element(By.ID, "checkout").click()
time.sleep(6)
driver.close()


