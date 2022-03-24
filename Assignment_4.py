import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("/Users/adam/Documents/rando/chromedriver")
driver = webdriver.Chrome(service=s)

"""
Open Facebook.com. Enter username, Password and click submit button, using below wait function.
i.      Explicit/SMART Wait
ii.      Implicit Wait
iii.      Hard Wait
"""


def myThreeWaits():
    # implicit wait/between each call/fix race conditions
    driver.implicitly_wait(1)
    driver.get("https://www.facebook.com")
    # explicit wait
    w = WebDriverWait(driver, 10)
    w.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@name='login']")))
    driver.find_element(By.XPATH, "//*[@id='email']").send_keys("fakeEmail234234234@gmail.com")
    driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("password")
    # hard wait
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@name='login']").click()


"""
2.       Open Facebook,, then manually open few more tabs. Get the count of total open window handles, then Switch between desired window handles.
"""


def tabSwitch():
    url = "https://www.facebook.com"
    driver.get(url)

    for i in range(1, 6):
        driver.switch_to.new_window()

    handles = driver.window_handles
    len_handles = len(handles)

    for i in range(1, len_handles):
        driver.switch_to.window(handles[i])
        time.sleep(2)


tabSwitch()
time.sleep(3)
driver.quit()

