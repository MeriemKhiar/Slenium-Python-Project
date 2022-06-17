import time

from gererIframe import webdriver
from gererIframe.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()
#Récup l alerte
alertWindows = driver.switch_to.alert
print(alertWindows.text)

#Cliquez sur le button ok de l'alérte
alertWindows.accept()

time.sleep(6)
driver.quit() #fermer toute les fenétres ouverte par le script