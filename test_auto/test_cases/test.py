# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestRunner
import xmlrunner
import logging

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.facebook.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.email = "geenathp@gmail.com"
        self.password = "0717141385353017"
        #self.shortDescription = "attemting to loggin to facebook"
    
    def test_facebook_loggin(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        log = logging.getLogger( "SomeTest.testSomething" )
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(self.email)
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("pass").send_keys(self.password)
        driver.find_element_by_id("u_0_p").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
   # unittest.main()
    #HTMLTestRunner.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
