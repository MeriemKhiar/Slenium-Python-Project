import time

from gererIframe import webdriver
from gererIframe.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]").click()
#Récup l alerte
confirmWindows = driver.switch_to.alert
print(confirmWindows.text)

#Cliquez sur le button ok de l'alérte
confirmWindows.dismiss()

time.sleep(6)
driver.quit() #fermer toute les fenétres ouverte par le script