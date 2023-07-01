from selenium import webdriver
from os.path import exists  ## imported the  exist method
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from TC1_loginCSE import login
import time


def buckets_report(driver):
    login()
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/ul[1]/li[3]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-buckets[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[2]/span[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/div[1]/div[1]/ul[1]/p-dropdownitem[3]/li[1]/span[1]").click()
    time.sleep(4)
driver=login()
buckets_report(driver)