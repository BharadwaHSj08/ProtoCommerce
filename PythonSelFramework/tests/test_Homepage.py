import time

import pytest
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.Homepage import HomePage
from TestData.HomepageData import HomepageData
from utilities.BaseClass import BaseClass


class TestHomepage(BaseClass):

    def test_formSubmission(self,getData):
        #driver = webdriver.Chrome()
        #driver.get("https://rahulshettyacademy.com/angularpractice/")

        logger =self.get_Logger()
        # Locators can be ID, Xpath, CSS Selectors, Name, Class Name, Link text
        #self.driver.find_element(By.CSS_SELECTOR,"[name = 'name']").send_keys("Ram")
        homePage =HomePage(self.driver)

        homePage.getName().send_keys(getData["firstname"])
        logger.info("The First Name is" + getData["firstname"])

        #self.driver.find_element(By.NAME, "email").send_keys("Sai@")
        homePage.getEmail().send_keys(getData["email"])

        #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("@123456")
        homePage.enterPassword().send_keys("@123456")

        # Static Drop using Select class
        #dropdown = Select(self.driver.find_element(By.ID, 'exampleFormControlSelect1'))
        #dropdown = Select(homePage.getGender())
        #dropdown.select_by_visible_text("Female")
        self.selectOptionbyText(homePage.getGender(),getData["Gender"])

        # driver.find_element(By.ID,"exampleFormControlSelect1").send_keys("Male")

        #self.driver.find_element(By.ID, "exampleCheck1").click()
        homePage.employeSts().click()

        # driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("Sai")
        #self.driver.find_element(By.CLASS_NAME, 'form-control').send_keys("Ram")
        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        homePage.submitClick().click()

        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        #message = homePage.getSuccesstext()
        print(message)
        #self.driver.find_element(By.XPATH, "(//input[@type ='text'])[3]").send_keys(" Hello Again")
        assert ("Success" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.getTestData("TC2"))
    def getData(self,request):
        return request.param
