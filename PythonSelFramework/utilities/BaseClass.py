from telnetlib import EC
import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass():

    def get_Logger(self):
        #to print the name of Method which called the get_Logger
        loggerName = inspect.stack()[1][3]
        #Passing the method name which called the get_Logger to the logger object to print
        logger = logging.getLogger(loggerName)

    #To get the location where the logger needs to print the logs to
        fileHandler = logging.FileHandler("Logfile.log")

    #the format which the logfile needs to be printed
        file_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    #passing the format to the filehandler
        fileHandler.setFormatter(file_format)

    #to print the log file
        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO) #--> to print from which level we need to print the log
        return logger

    #logger.debug("A debug statement is printed")
    #logger.info("A info statement is printed")
    #logger.warning("A warning statement is printed")
    #logger.error("A error statement is printed")
    #logger.critical("A critical statement is printed")


    def VerifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOptionbyText(self,locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)