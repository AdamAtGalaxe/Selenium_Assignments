from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import constants
from selenium.webdriver.common.by import By

def initDriver():
    s = Service("/Users/adamroberts/Documents/Selenium/chromedriver")
    myDriver = webdriver.Chrome(service=s)
    myDriver.get(constants.url)
    return myDriver

def findElement(name: str):
    xpath = "//*[@id='" + name +"' or @name='" + name + "']"
    print(xpath)
    return constants.driver.find_element(By.XPATH, xpath)

def sendKeys(element, string):
    element.send_keys(string)

def click(element):
    element.click()