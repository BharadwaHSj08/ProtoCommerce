from selenium.webdriver.common.by import By


class ConfirmPage():

    def __init__(self,driver):
        self.driver = driver


    addressGiven = (By.ID,"country")
    #self.driver.find_element(By.ID, "country").send_keys(country_name)


    submit = (By.CSS_SELECTOR,"[type = 'submit']")
    #self.driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()

    alertText = (By.CLASS_NAME, "alert_success")
    #self.driver.find_element(By.CLASS_NAME, "alert-success").text

    def Addressinput(self):
        return self.driver.find_element(*ConfirmPage.addressGiven)

    def Submitting(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def Alerttext(self):
        return self.driver.find_element(*ConfirmPage.alertText)