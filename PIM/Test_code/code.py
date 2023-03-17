from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_data import data
from Test_locator import locators

class Anup:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def __init__(self):
        self.driver.get(data.Anup.url)

    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Anup.username).send_keys(data.Anup.username)
        self.driver.find_element(by=By.NAME,value=locators.Anup.password).send_keys(data.Anup.password)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.loginButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.PIM).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.add).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.firstname).send_keys(data.Anup.firstname)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.lastname).send_keys(data.Anup.lastname)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.employee_id).send_keys(data.Anup.employee_id)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.login_button).click()
        self.driver.find_element(by=By.XPATH,value=locators.Anup.user).send_keys(data.Anup.user)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.password1).send_keys(data.Anup.password1)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.password2).send_keys(data.Anup.password2)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.save).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.employee).send_keys(data.Anup.employee)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.search).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Anup.search_button).click()

       
       
Anup().login()
