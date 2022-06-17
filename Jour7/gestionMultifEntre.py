import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')
#cherche moi id de cette page
parentWindowId = driver.current_window_handle
print(parentWindowId)

driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
#Récup la liste des ids de fenetres couvertes
# récup la liste des ids
widowsHandelsIds = driver.window_handles
#2ere fenetre
parentWindowId = widowsHandelsIds[0]
childWindows = widowsHandelsIds[1]
#les ids générés sont dynamiques

print("parentWindowId : ",parentWindowId)
print("ChilWindows: " ,childWindows)
driver.switch_to.window(childWindows)
url = driver.current_url
title=driver.title
print(url)
print(title)

for winId in widowsHandelsIds:
    driver.switch_to.window(winId)
    if driver.title== title:
        driver.close()
time.sleep(4)
driver.quit()