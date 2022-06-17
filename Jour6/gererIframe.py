import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')

driver.switch_to.frame("packageListFrame")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

time.sleep(3)

#Sortir du premier frame pour retourner à la page par défault:
driver.switch_to.default_content()

#switcher de frame pour pouvoir aller cliquer sur webDriver

driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT,"WebDriver").click()

driver.close()



