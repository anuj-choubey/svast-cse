from selenium import webdriver
from os.path import exists  ## imported the  exist method
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
import time



def login ():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://localhost:4200/#/")
    driver.find_element(By.CLASS_NAME, "other-login").click()
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]") \
        .send_keys("cse@mistpl.com")
    # Enter password
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]") \
        .send_keys("Svast@1209")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(3)
    return driver
# login()
def Wrong_mail ():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://localhost:4200/#/")
    driver.find_element(By.CLASS_NAME, "other-login").click()
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]") \
        .send_keys("cse@mitp.com")
    time.sleep(3)
    # Enter password
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]") \
        .send_keys("Svast@1209")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    time.sleep(10)
# Wrong_mail()
def Wrong_password():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://localhost:4200/#/")
    driver.find_element(By.CLASS_NAME, "other-login").click()
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]") \
        .send_keys("cse@mistp.com")
    time.sleep(3)
    # Enter password
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]") \
        .send_keys("Svast@120")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(4)
# Wrong_password()
def blank_login():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("http://localhost:4200/#/")
    driver.find_element(By.CLASS_NAME, "other-login").click()
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]") \
        .send_keys("")
    time.sleep(3)
    # Enter password
    driver.find_element(By.XPATH,
                        "//body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]") \
        .send_keys("")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    time.sleep(4)
# blank_login()
