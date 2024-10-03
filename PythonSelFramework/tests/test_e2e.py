import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Checkoutpage import CheckoutPage
from PageObjects.Homepage import HomePage
from PageObjects.confirmpage import ConfirmPage
from utilities.BaseClass import BaseClass

#"BaseClass" inherits the methods and props of the fixture "setup".Now,"Baseclass" is the parent class
#Testone can inherit all the props and methods of fixtures through base class,so we do not need the below code for fixture
#@pytest.mark.usefixtures("setup")


class TestOne(BaseClass):

    def test_e2e(self):

        logger = self.get_Logger()
        # clicking on the Shop option in the page
        homepage = HomePage(self.driver)
        logger.info("Clicking on the Shop of Home page")
        #homepage.shopItems().click()
        time.sleep(3)

        # scrolling down
        self.driver.execute_script("window.scrollBy(0,500);")

        # selecting the Items
        #checkOutPage = CheckoutPage(self.driver)
        #Items_list = checkOutPage.Itemslist()
        checkOutPage = homepage.shopItems()
        Items_list = checkOutPage.Itemslist()
        time.sleep(2)

        # Required item
        required_item = "Blackberry"

        # selecting the required Item from the list
        for items in Items_list:
            item_name = items.find_element(By.XPATH, "div/h4").text
            logger.info(item_name)
            if item_name == required_item:
                items.find_element(By.XPATH, "div/button").click()
                #checkOutPage.clickrequiredItem.click()
                break

        # clicking on the checkout after selecting the item in the item page
        checkOutPage.Itemscheckout().click()
        time.sleep(3)

        # again clicking on the Checkout button in the final checkout page
        #self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]/button").click()
        #checkOutPage.CheckoutConfirm().click(
        time.sleep(3)

        # Giving the Address for delivery
        country_name = "India"
        #self.driver.find_element(By.ID, "country").send_keys(country_name)
        #confirmpage = ConfirmPage(self.driver)
        confirmpage = checkOutPage.CheckoutConfirm()
        confirmpage.Addressinput().send_keys(country_name)
        #confirmpage.Addressinput().send_keys(country_name)

        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, country_name)))
        self.VerifyLinkPresence("India")
        #self.driver.find_element(By.LINK_TEXT, country_name).click()
        confirmpage.Addressinput().click()

        #click on submit
        #self.driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
        confirmpage.Submitting().click()

        alert_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        #alert_text = confirmpage.Alerttext().text
        #print(alert_text)
        logger.info(alert_text)

        assert "Success!" in alert_text


