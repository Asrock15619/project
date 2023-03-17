
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from Test_data import data
from Test_locator import locator
import pytest

class Test_Hrm:
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(data.Hrm_Data().url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

                  
    def test_login(self,booting_function):
        try:   
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().searchbox_upper) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Admin)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Admin).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().searchbox_lower) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Admin)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Admin).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().searchbox_pimU) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pim)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pim).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().searchbox_pimL) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pim)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pim).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().leaveup) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().leave)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().leave).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().leavelow) 
          
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().leave)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().leave).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().timeup) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Time)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Time).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().timelow) 

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Time)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Time).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().recruitmentup)           
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Recruitment)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Recruitment).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().recruitmentlow) 
                      
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Recruitment)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Recruitment).click()
                     
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().myinfoup) 
                      
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().My_info)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().My_info).click()                                 
                      
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().myinfolow)                                                                                                       
                      
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().My_info)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().My_info).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().performanceup) 
    
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().performance)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().performance).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().performancelow) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().performance)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().performance).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().dashboardup) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Dashboard)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Dashboard).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().dashboardlow) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Dashboard)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Dashboard).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().directoryup) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Directory)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Directory).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().directorylow) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Directory)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Directory).click()  
                    
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().maintanenceup) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Maintenance)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Maintenance).click()
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().admin_password)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().admin_password).send_keys(data.Hrm_Data().a_password)           
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().conform_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().conform_button).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().maintanancelow) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Maintenance)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Maintenance).click()                
                                                               
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().buzzup) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Buzz)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Buzz).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_box)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_box).send_keys(data.Hrm_Data().buzzlow) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Buzz)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Buzz).click()             
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all individual menu upper name lower name should be displayed under search textbox")
        except NoSuchElementException:
              print('Some elements are missing !')  
              
    def test_adminpage(self,booting_function):
        try:     
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username)  
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Admin)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Admin).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().usermanagement)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().usermanagement).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().user)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().user).click()  
           self.driver.execute_script("window.stop();");  
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee).send_keys(data.Hrm_Data().employeename)                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().userrole)))
           userrole1=self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().userrole)
           userrole1.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue19=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           if drop_downvalue19.__contains__("Admin"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Admin'",userrole1)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().status)))
           status1=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().status)
           status1.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down1)))
           drop_downvalue20=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down1).text
           if drop_downvalue20.__contains__("Enabled"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Enabled'",status1)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Admin)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Admin).click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().usermanagement)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().usermanagement).click() 
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().user)))
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see activation on job  Details page")
        except NoSuchElementException:  
            print('no') 
              
    
              
    def test_search_employee(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click()                              
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the  tabs  present in Employee list page")
        except NoSuchElementException :  
            print('yes')                    
            
    def test_personal_employee(self,booting_function):
        try:
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().other_id)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().other_id).send_keys(data.Hrm_Data().otherid)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().driving_licence)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().driving_licence).send_keys(data.Hrm_Data().license_number)           

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().expiry_date)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().expiry_date).send_keys(data.Hrm_Data().license_expire_date)
                       
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().ssnnumber)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().ssnnumber).send_keys(data.Hrm_Data().ssn_number)           
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().sinnumber)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().sinnumber).send_keys(data.Hrm_Data().sin_number)                                    
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().nationality)))
           value=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().nationality)
           value.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().country)))
           place=self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().country)
           place.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue2=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue2)
           if drop_downvalue2.__contains__("India"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='India'",place)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().home)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().home).send_keys(data.Hrm_Data().home_no)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().moblie)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().moblie).send_keys(data.Hrm_Data().mobile_no)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().work)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().work).send_keys(data.Hrm_Data().work_name)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().w_mail)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().w_mail).send_keys(data.Hrm_Data().work_mail)
        
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().other_mail)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().other_mail).send_keys(data.Hrm_Data().other_mail)        
           sleep(5)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().save_button2)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().save_button2).click()        
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in contact details page")
        except NoSuchElementException:  
            print('some element are missing')

    def test_contact_detail(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click() 

           self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator.Hrm_locator().contact_detail)))
           self .driver.find_element(by=By.LINK_TEXT, value=locator.Hrm_locator().contact_detail).click() 

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().street_1)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().street_1).send_keys(data.Hrm_Data().street)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().street_2)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().street_2).send_keys(data.Hrm_Data().state_name)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().city)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().city).send_keys(data.Hrm_Data().city_name)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().state)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().state).send_keys(data.Hrm_Data().state_name)           

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().code)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().code).send_keys(data.Hrm_Data().zip_code)
           
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().country)))
           place=self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().country)
           place.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue2=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue2)
           if drop_downvalue2.__contains__("India"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='India'",place)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().home)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().home).send_keys(data.Hrm_Data().home_no)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().moblie)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().moblie).send_keys(data.Hrm_Data().mobile_no)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().work)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().work).send_keys(data.Hrm_Data().work_name)

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().w_mail)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().w_mail).send_keys(data.Hrm_Data().work_mail)
        
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().other_mail)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().other_mail).send_keys(data.Hrm_Data().other_mail)        
           sleep(5)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().save_button2)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().save_button2).click()        
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in contact details page")
        except NoSuchElementException:  
            print('some element are missing')
       
       
    def test_emergency_details(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click() 
             
           self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator.Hrm_locator().emergency_contact)))
           self.driver.find_element(by=By.LINK_TEXT, value=locator.Hrm_locator().emergency_contact).click()  
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().emergency_add)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().emergency_add).click()  
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().name)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().name).send_keys(data.Hrm_Data().Name)
                      
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().relationship)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().relationship).send_keys(data.Hrm_Data().Relationship)                      
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().home_number)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().home_number).send_keys(data.Hrm_Data().Home_Telephone)           

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().mobile_number)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().mobile_number).send_keys(data.Hrm_Data().Mobile_number)           
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().work_no)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().work_no).send_keys(data.Hrm_Data().work_Telephone)           
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().save_button3)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().save_button3).click()           
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in emerengcy details page")
        except NoSuchElementException:  
            print('some element are missing')                 
    
    def test_dependents_details(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()    
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Dependent)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Dependent).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Dependents_add)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Dependents_add).click()  
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Dependents_name)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Dependents_name).send_keys(data.Hrm_Data().Relation_name)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().relationship_member)))
           relative = self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().relationship_member)
           relative.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           dropdown3=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(dropdown3)
           if dropdown3.__contains__("Child"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Child'",relative)
                   
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().date_of_year)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().date_of_year).send_keys(data.Hrm_Data().Relation_dob)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().ok_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().ok_button).click()     
           assert self.driver.title == "OrangeHRM"
           print("The user should be able to see all the filled details present in dependent details page")
        except NoSuchElementException:
            print("not defiend")   
            
    def test_job_detail(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().job)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().job).click()
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().joined)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().joined).send_keys(data.Hrm_Data().start_date) 
           sleep(2)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().job_title)))
           job_name=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().job_title)
           job_name.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           dropdown_value4=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           if dropdown_value4.__contains__("Software Engineer"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Software Engineer'",job_name)

           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().job_category)))
           job_role=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().job_category)
           job_role.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           dropdown_value5=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           if dropdown_value5.__contains__("Technicians"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Technicians'",job_role)
                   
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().sub_unit)))
           sub_name=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().sub_unit)
           sub_name.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           dropdown_value6=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           if dropdown_value6.__contains__("Engineering"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Engineering'",sub_name)    
               
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().location)))
           area=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().location)
           area.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           dropdown_value7=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           if dropdown_value7.__contains__("New York Sales Office"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='New York Sales Office'",area)    
               
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_status)))
           employee_position=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_status)
           employee_position.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           dropdown_value8=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           if dropdown_value8.__contains__("Full-Time Contract"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Full-Time Contract'",employee_position)
           sleep(5)  
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Yes_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Yes_button).click()
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in job details page")
        except NoSuchElementException:  
            print('no')  

    def test_terminate_employee(self,booting_function):
          try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click()  
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().job)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.job).click()       
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Terminate)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.Terminate).click()
           sleep(2)  

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Terminate_employee)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Terminate_employee).send_keys(data.Hrm_Data().exit_DOB)
           

           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Terminate_reason)))
           Terminate=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.Terminate_reason)
           Terminate.click()
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           dropdown_value9=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.drop_down).text
           if dropdown_value9.__contains__("Other"):
               self.driver.execute_script("var a=arguments[0];a.innerHTML='Other'",Terminate)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().note)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.note).send_keys(data.Hrm_Data().Text)    
    
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().save_button5)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.save_button5).click()
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in terminate details page")
          except NoSuchElementException:  
            print('no')  
            

    def test_activate_employee(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click()  
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().job)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.job).click()       
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().activate)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator.activate).click()  
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see activation on job  Details page")
        except NoSuchElementException:  
            print('no') 
            
    def test_salarydetails(self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click()  

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().salary)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().salary).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().add_salary)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().add_salary).click()           
                      
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().salary_component)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().salary_component).send_keys(data.Hrm_Data().salarycomponent)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pay_grade)))
           value=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pay_grade)
           value.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue10=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue10)
           if drop_downvalue10.__contains__("Grade 1"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Grade 1'",value)
                
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pay_frequency)))
           name=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pay_frequency)
           name.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue11=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue11)
           if drop_downvalue11.__contains__("Monthly"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Monthly'",name)     
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().currency)))
           money=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().currency)
           money.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue12=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue12)
           if drop_downvalue12.__contains__("Indian Rupee"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Indian Rupee'",money)          
                      
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().salary_amount)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator.salary_amount).send_keys(data.Hrm_Data().salary_amount)                      

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().source_3)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().source_3).click()     
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().account)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().account).send_keys(data.Hrm_Data().account_no)                      
     
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().account_type)))
           account=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().account_type)
           account.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue13=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue13)
           if drop_downvalue13.__contains__("Savings"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Savings'",account) 
     
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().routing)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().routing).send_keys(data.Hrm_Data().Routing_no) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().amount)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().amount).send_keys(data.Hrm_Data().deposit_amount) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().save)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().save).click()
                                                    
           assert self.driver.title == 'OrangeHRM'
           print("The user should be able to see all the filled details present in salary details page")
        except NoSuchElementException:  
            print('some element are missing')   

    def test_tax (self,booting_function):
        try:
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().username_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().username_inputBox).send_keys(data.Hrm_Data().username) 
           
           self.wait.until(EC.element_to_be_clickable((By.NAME, locator.Hrm_locator().password_inputBox)))
           self.driver.find_element(by=By.NAME, value=locator.Hrm_locator().password_inputBox).send_keys(data.Hrm_Data().password)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().LoginButton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().LoginButton).click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().pimbutton)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().pimbutton).click()

           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().employee_name)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().employee_name).send_keys(data.Hrm_Data().employeename)
           sleep(3)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().search_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().search_button).click()     
           sleep(2)           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().edit_button)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().edit_button).click() 
           
           self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator.Hrm_locator().Tax)))
           self .driver.find_element(by=By.LINK_TEXT, value=locator.Hrm_locator().Tax).click() 
           sleep(2)
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().federal_status)))
           status=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().federal_status)
           status.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue14=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue14)
           if drop_downvalue14.__contains__("Married"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Married'",status) 
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().Exemptions)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().Exemptions).send_keys(data.Hrm_Data().value_Exemptions)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().state_2)))
           state=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().state_2)
           state.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue15=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue15)
           if drop_downvalue15.__contains__("Indiana"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Indiana'",state)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().status_data)))
           tax=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().status_data)
           tax.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue16=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue16)
           if drop_downvalue16.__contains__("Single"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='Single'",tax)
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().tax_Exemptions)))
           self .driver.find_element(by=By.XPATH, value=locator.Hrm_locator().tax_Exemptions).send_keys(data.Hrm_Data().per_Exemptions)
                     
                
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().unemployee_state)))
           unemployee=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().unemployee_state)
           unemployee.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue17=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue17)
           if drop_downvalue17.__contains__("American Samoa"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='American Samoa'",unemployee)
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().work_state)))
           work=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().work_state)
           work.click()
           
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().drop_down)))
           drop_downvalue18=self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().drop_down).text
           print(drop_downvalue18)
           if drop_downvalue18.__contains__("American Samoa"):
                self.driver.execute_script("var a=arguments[0];a.innerHTML='American Samoa'",work) 
                    
                       
           self.wait.until(EC.element_to_be_clickable((By.XPATH, locator.Hrm_locator().complete)))
           self.driver.find_element(by=By.XPATH, value=locator.Hrm_locator().complete).click()           
           assert self.driver.title == 'OrangeHRM'        
           print("The user should be able to see all the filled details present in Tax Exemptions details page")
        except NoSuchElementException:
            print("not defiend")   

           
Test_Hrm().test_login() 
Test_Hrm().test_adminpage()
Test_Hrm().test_search_employee()
Test_Hrm().test_personal_employee()
Test_Hrm().test_contact_detail()
Test_Hrm().test_emergency_details()
Test_Hrm().test_dependents_details()
Test_Hrm().test_job_detail()
Test_Hrm().test_terminate_employee()
Test_Hrm().test_activate_employee()
Test_Hrm().test_salarydetails()
Test_Hrm().test_tax()

       
