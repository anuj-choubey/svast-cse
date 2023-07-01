from selenium import webdriver
from os.path import exists  ## imported the  exist method
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from TC1_loginCSE import login
import time

def re_port(driver):
    login()
    x=500
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]").click()
    time.sleep(3)
    ar_report=driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]")
    ar_report.click()
    time.sleep(10)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-ar-reports[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[2]/span[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[contains(text(),'Advanced Care for Women LLC')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-ar-reports[1]/div[1]/div[2]/div[2]/p-tabview[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0," + str(x) + ")")
    x += 500
    time.sleep(3)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-ar-reports[1]/div[1]/div[3]/div[2]/p-tabview[1]/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]/span[1]").click()
    time.sleep(3)
    # scroll=driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-ar-reports[1]/div[1]/div[3]/div[2]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/p-table[1]/div[1]/div[1]")
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-ar-reports[1]/div[1]/div[3]/div[1]/button[1]").click()
    time.sleep(10)

driver= login()
re_port(driver)