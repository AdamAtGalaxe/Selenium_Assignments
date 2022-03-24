import time

import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By


driver = uc.Chrome()


driver.get("https://gmail.com")
# driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys("pjamfan671@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys("anypasscode")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button").click()
time.sleep(1)
driver.get("https://www.facebook.com")
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("pjamfan671@gmail.com")

time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("anypasscode")

time.sleep(1)
driver.find_element(By.XPATH, "//button[@name='login']").click()
time.sleep(10)
driver.quit()