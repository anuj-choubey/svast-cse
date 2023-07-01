from selenium import webdriver
from os.path import exists  ## imported the  exist method
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from TC1_loginCSE import login
import time

def pr_report(driver):
    login()
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/ul[1]/li[2]/a[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p-multiselect[1]/div[1]/div[3]/span[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p-multiselect[1]/div[1]/div[4]/div[1]/div[1]/div[2]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p-multiselect[1]/div[1]/div[4]/div[2]/ul[1]/p-multiselectitem[2]/li[1]").click()
    time.sleep(6)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p-multiselect[1]/div[1]/div[4]/div[1]/button[1]/span[1]").click()
    time.sleep(4)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]/span[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/p-multiselect[1]/div[1]/div[3]/span[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/p-multiselect[1]/div[1]/div[4]/div[2]/ul[1]/p-multiselectitem[2]/li[1]/div[1]/div[1]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/p-multiselect[1]/div[1]/div[4]/div[1]/button[1]/span[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-production-reports[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[1]/span[1]").click()
    time.sleep(4)
driver=login()
pr_report(driver)
