import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

class Test_001_Login:
    base_url = "https://admin-demo.nopcommerce.com/"

    logger = LogGen.loggen()


    def test_HomePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title== "nopCommerce demo store. Login":
            assert  True
        else:
            assert False
        print("test_HomePageTitle passed")
        self.logger.info("test_HomePageTitle passed")



    def test_login(self, setup):
          self.driver = setup
          self.driver.get(self.base_url)
          act_title = self.driver.title
          if act_title== "nopCommerce demo store. Login":
              assert  True
          else:
             assert False
          print("test_HomePageTitle passed")
          self.logger.info("test_HomePageTitle passed")

          self.lp= LoginPage(self.driver)
          self.lp.enter_email("admin@yourstore.com")
          self.logger.info("email given")
          self.lp.enter_password("admin")
          self.logger.info("password given")
          self.lp.click_login()
          self.logger.info("login success passed")







