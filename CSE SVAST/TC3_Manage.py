from selenium import webdriver
from os.path import exists  ## imported the  exist method
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from TC1_loginCSE import login
import time


def manage(driver):
    login()
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[3]/a[1]").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[3]/ul[1]/li[8]/a[1]").click()
    time.sleep(10)
# driver=login()
# manage(driver)
