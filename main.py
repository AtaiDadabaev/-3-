from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import conftest

def right(driver):
    return ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()

def _input(driver, type, value, text):
    time.sleep(2)
    if (type == "x"):
        driver.find_element(By.XPATH, value).send_keys(text)
        time.sleep(2)
    elif (type == "lt"):
        driver.find_element(By.LINK_TEXT, value).send_keys(text)
        time.sleep(2)
    elif (type == "css"):
        driver.find_element(By.CSS_SELECTOR, value).send_keys(text)
        time.sleep(2)

def find_click(driver, type, value):
    time.sleep(2)
    if (type == "x"):
        driver.find_element(By.XPATH, value).click()
        time.sleep(2)
    elif (type == "lt"):
        driver.find_element(By.LINK_TEXT, value).click()
        time.sleep(2)
    elif (type == "css"):
        driver.find_element(By.CSS_SELECTOR, value).click()
        time.sleep(2)


def test_first(driver):
    time.sleep(2)
    product = driver.find_element(By.LINK_TEXT,"MacBook")
    product.click()
    time.sleep(2)
    screen = driver.find_element(By.XPATH, "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]")
    screen.click()
    time.sleep(1)
    right(driver)
    time.sleep(1)
    right(driver)
    time.sleep(1)
    right(driver)
    time.sleep(4)

def test_second(driver):
    time.sleep(2)
    buy_product = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(1) div.product-thumb.transition div.button-group > button:nth-child(1)")
    buy_product.click()
    time.sleep(2)
    basket = driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[3]/div[1]/button[1]")
    basket.click()
    time.sleep(4)

def test_third(driver):
    find_click(driver, "lt", "Компьютеры")
    find_click(driver, "lt", "PC (0)")
    time.sleep(2)

def test_fouth(driver):
    time.sleep(2)
    authentication = driver.find_element(By.XPATH,"//span[contains(text(),'Личный кабинет')]" )
    authentication.click()
    time.sleep(2)
    regestration = driver.find_element(By.LINK_TEXT, "Регистрация")
    regestration.click()
    time.sleep(2)
    _input(driver, "css", "#input-firstname", "Atai")
    _input(driver, "css", "#input-lastname", "Dadabaev")
    _input(driver, "css", "#input-email", "Dadabaevataj@gmail.com")
    _input(driver, "css", "#input-telephone", "89261226509")
    _input(driver, "css", "#input-password", "Atai")
    _input(driver, "css", "#input-confirm", "Atai")
    find_click(driver, "x", "//body/div[@id='account-register']/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label[1]/input[1]")
    find_click(driver, "x", "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
    find_click(driver, "x", "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]")
    time.sleep(2)


def test_fifth(driver):
    find_click(driver, "x", "//header/div[1]/div[1]/div[2]/div[1]/input[1]")
    _input(driver, "x", "//header/div[1]/div[1]/div[2]/div[1]/input[1]", "pc")
    find_click(driver, "x", "//header/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]")
    time.sleep(4)
