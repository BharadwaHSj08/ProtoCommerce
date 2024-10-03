from selenium.webdriver.common.by import By

from PageObjects.Checkoutpage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    shop = (By.XPATH,"//ul/li[2]")

    name = (By.CSS_SELECTOR,"[name = 'name']")
    #self.driver.find_element(By.CSS_SELECTOR, "[name = 'name']").send_keys("Ram")

    emaiName = (By.NAME,"email")
    #self.driver.find_element(By.NAME, "email").send_keys("Sai@")

    password = (By.ID,"exampleInputPassword1")
    #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("@123456")

    empStatus = (By.ID,"exampleCheck1")
    #self.driver.find_element(By.ID, "exampleCheck1").click()

    submitclik =(By.XPATH,"//input[@type ='submit']")
    #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    gender_select = (By.ID,"exampleFormControlSelect1")
    #self.driver.find_element(By.ID, 'exampleFormControlSelect1'

    success_text = (By.CLASS_NAME,"alert_success")
    #self.driver.find_element(By.CLASS_NAME, "alert-success").text


    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.emaiName)

    def enterPassword(self):
        return self.driver.find_element(*HomePage.password)

    def employeSts(self):
        return self.driver.find_element(*HomePage.empStatus)

    def submitClick(self):
        return self.driver.find_element(*HomePage.submitclik)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender_select)

    def getSuccesstext(self):
        return self.driver.find_element(*HomePage.success_text).text

    def shopItems(self):

        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        #we use star to homepage because it needs to deserialize into the below way
        #driver.find_element(By.XPATH, "//ul/li[2]")
