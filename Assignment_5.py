import xlrd
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#1. Open flipkart.com. Verify whether Flipkart logo displays or not using, is_displayed method.
s = Service("/Users/adam/Documents/rando/chromedriver")
driver = webdriver.Chrome(service=s)
url = "https://flipkart.com"
driver.get(url)
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()
time.sleep(2)
if driver.find_element(By.XPATH, "//img[@alt='Flipkart']").is_displayed():
    print("FlipKart is opened")
else:
    print("nope")

#2. Open flipkart.com, hover to Electronics menu.
actions = ActionChains(driver)
element = driver.find_element(By.XPATH, "//img[@alt='Electronics']")
actions.move_to_element(element)
actions.perform()
time.sleep(4)
actions.release()

#3. Open flipkart.com., take a screenshot and save to your desired location.
driver.save_screenshot("/Users/adam/Documents/rando/my_screenshot.png")

#4. Create an excel sheet (.xls/.xlsx) with heading username and password, and create five data sets. Using XLRD , print all 5 username and password. Write all code using try, Except method.
try:
    wb = xlrd.open_workbook("/Users/adam/Documents/rando/my_data.xls")
    sheet = wb.sheet_by_index(0)
    cnt_row = sheet.nrows
    cnt_col = sheet.ncols
    print("Excel")

    for i in range(1, cnt_row):
        name = sheet.cell_value(i, 0)
        email = sheet.cell_value(i, 1)
        password = sheet.cell_value(i, 2)
        print("name: {}, email: {}, password: {}".format(name, email, password))
except Exception as e:
    print("error in reading excel")
    print(str(e))

time.sleep(5)
driver.quit()