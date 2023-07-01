from selenium import webdriver
from os.path import exists  ## imported the  exist method
from helpersUsers import cust_fun
from selenium.webdriver.common.by import By
from TC1_loginCSE import login
import time
y=2000
x=2000
def dash_Basc(driver):
    login()
    x=3000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    sort_by = driver.find_element(By.XPATH, "//span[contains(text(),'Sort By')]")
    sort_by.click()
    # choose dropdown asc
    ASC = driver.find_element(By.XPATH, "//span[contains(text(),'By Balance ASC')]")
    ASC.click()
    ## check button
    balance= driver.find_element(By.XPATH,"//thead/tr[1]/th[12]")
    balance.click()
    driver.execute_script("window.scrollTo(0," + str(x) + ")")
    x += 2000
    time.sleep(6)
    # driver.find_element(By.XPATH,"//tbody/tr[500]/td[12]").click()
    # time.sleep(3)
    driver.find_element(By.XPATH, "//tbody/tr[500]/td[12]")
    time.sleep(10)


# driver=login()
# dash_Basc(driver)
def dashboard_Bdesc(driver):
    login()
    x=3000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    sort_by = driver.find_element(By.XPATH, "//span[contains(text(),'Sort By')]")
    sort_by.click()
    DEC = driver.find_element(By.XPATH, "//span[contains(text(),'By Balance DESC')]")
    DEC.click()
    #   # check button
    balance = driver.find_element(By.XPATH, "//thead/tr[1]/th[12]")
    balance.click()
    driver.execute_script("window.scrollTo(0," + str(x) + ")")
    x += 2000
    time.sleep(6)
    driver.find_element(By.XPATH, "//tbody/tr[500]/td[12]").click()


# driver=login()
# dashboard_Bdesc(driver)
def dash_Bdd(driver):
    login()
    x=3000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    sort_by = driver.find_element(By.XPATH, "//span[contains(text(),'Sort By')]")
    sort_by.click()
    DEs = driver.find_element(By.XPATH, "//span[contains(text(),'By Billed Date DESC')]")
    DEs.click()
    time.sleep(5)
    # #check button
    # Billed_date=driver.find_element(By.XPATH,"//thead/tr[1]/th[10]")
    # Billed_date.click()
    driver.execute_script("window.scrollTo(0," + str(x) + ")")
    x += 2000
    time.sleep(6)
    time.sleep(5)
    driver.find_element(By.XPATH, "//td[contains(text(),'08/30/2022')]").click()
    time.sleep(3)


# driver=login()
# dash_Bdd(driver)
def dash_Bda(driver):
    login()
    x=3000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    sort_by = driver.find_element(By.XPATH, "//span[contains(text(),'Sort By')]")
    sort_by.click()
    asc = driver.find_element(By.XPATH, "//span[contains(text(),'By Billed Date ASC')]")
    asc.click()
    time.sleep(3)
    # # check button
    Bill_ed_date = driver.find_element(By.XPATH, "//thead/tr[1]/th[10]/p-sorticon[1]/i[1]")
    Bill_ed_date.click()
    driver.execute_script("window.scrollTo(0," + str(x) + ")")
    x += 2000
    time.sleep(6)
    time.sleep(3)


# driver=login()
# dash_Bda(driver)
def dash_Sdd(driver):
    login()
    x=2000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    sort_by = driver.find_element(By.XPATH, "//span[contains(text(),'Sort By')]")
    sort_by.click()
    # desc=driver.find_element(By.XPATH,"//span[contains(text(),'By Service Date DESC')]")
    # desc.click()
    time.sleep(10)
##check button
    service_date = driver.find_element(By.XPATH,"//thead/tr[1]/th[9]")
    service_date.click()
    driver.execute_script("window.scrollTo(0,"+str(x)+")")
    x +=2000
    time.sleep(6)
#     time.sleep(5)
# driver = login()
# dash_Sdd(driver)
def dash_Sasc(driver):
    login()
    x = 2000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    sort_by = driver.find_element(By.XPATH, "//span[contains(text(),'Sort By')]")
    sort_by.click()
    # asc=driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-workbench[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]/div[1]/ul[1]/p-dropdownitem[1]/li[1]")
    # asc.click()
    time.sleep(10)
    # check button
    service_Date=driver.find_element(By.XPATH,"//thead/tr[1]/th[9]")
    service_Date.click()
    driver.execute_script("window.scrollTo(0," + str(x) + ")")
    x += 2000
    time.sleep(6)
# driver = login()
# dash_Sasc(driver)
def assin_to(driver):
    login()
    x = 2000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    select=driver.find_element(By.XPATH,"//thead/tr[2]/th[2]/p-multiselect[1]/div[1]/div[3]/span[1]")
    select.click()
    time.sleep(3)
    Assign_to=driver.find_element(By.XPATH,"//body/div[1]/div[2]/ul[1]/p-multiselectitem[2]/li[1]")
    Assign_to.click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//body/div[1]/div[1]/button[1]/span[1]").click()
    time.sleep(3)
# driver = login()
# assin_to(driver)
def g_lobal(driver):
    login()
    x = 2000
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    time.sleep(10)
    Global=driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-workbench[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    Global.send_keys("CLAIM AT AARP MEDICARE COMPLET")
    time.sleep(5)
    # fillter button
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-workbench[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
    time.sleep(10)
    # clear button
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-workbench[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/button[1]").click()
    time.sleep(3)
    Global = driver.find_element(By.XPATH,
                                 "//body/app-root[1]/div[1]/app-workbench[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
    Global.send_keys("CLAIM AT HUMANA")
    time.sleep(5)
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-workbench[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
    time.sleep(5)
    # freez button
    driver.find_element(By.XPATH,"//body/app-root[1]/div[1]/app-workbench[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/button[2]").click()
    time.sleep(4)
    #     back to dashboard page
    driver.find_element(By.XPATH,"//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[1]/a[1]").click()
    time.sleep(4)
#     return to workbench
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    time.sleep(5)
# driver=login()
# g_lobal(driver)
def na_me(driver):
    login()
    workbench = driver.find_element(By.XPATH, "//body/app-root[1]/app-nav[1]/nav[1]/div[1]/div[1]/ul[1]/li[2]/a[1]")
    workbench.click()
    time.sleep(7)
    # name button
    n_ame=driver.find_element(By.XPATH,"//thead/tr[2]/th[20]/p-multiselect[1]/div[1]/div[3]/span[1]")
    n_ame.click()
    driver.find_element(By.XPATH,"//span[contains(text(),'Sapna Mary')]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//body/div[1]/div[1]/button[1]").click()
    time.sleep(4)
# driver=login()
# na_me(driver)
