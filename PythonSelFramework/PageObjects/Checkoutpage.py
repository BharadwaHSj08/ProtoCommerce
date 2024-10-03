from selenium.webdriver.common.by import By

from PageObjects.confirmpage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    checkoutpage = (By.XPATH, "//div[@class = 'card h-100']")
    #Items_list = self.driver.find_elements(By.XPATH, "//div[@class= 'card h-100']")

    #clickrequiredItem = (By.XPATH,"div/button")
    #items.find_element(By.XPATH, "div/button")

    Checkout_items =(By.XPATH,"//div/ul/li/a")
    #self.driver.find_element(By.XPATH, "//div/ul/li/a")

    Confirm_checkout =(By.XPATH,"//tbody/tr[3]/td[5]/button")
    #self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]/button").click()

    def Itemslist(self):
        return self.driver.find_elements(*CheckoutPage.checkoutpage)

    def Itemscheckout(self):
        return self.driver.find_element(*CheckoutPage.Checkout_items)

    def CheckoutConfirm(self):
        self.driver.find_element(*CheckoutPage.Confirm_checkout).click()
        confirmining = ConfirmPage(self.driver)
        return confirmining

    # def clickItem(self):
    #   return self.driver.find_element(*CheckoutPage.clickrequiredItem)

