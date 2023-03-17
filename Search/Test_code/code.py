from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from time import sleep
from Test_data import data
from Test_locator import locator

class Anup:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def __init__(self):
        self.driver.get(data.Anup.url)

    def login(self):
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locator.Anup.username).send_keys(data.Anup.username)
        self.driver.find_element(by=By.NAME,value=locator.Anup.password).send_keys(data.Anup.password)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.login_Button).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.PIM)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.leave)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.Time)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.Recruitment)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.My_info)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.Performance)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.Dashboard)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.Directory)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.Maintenance)
        self.driver.find_element(by=By.XPATH,value=locator.Anup.Search).send_keys(data.Anup.Buzz)
        

Anup().login()
