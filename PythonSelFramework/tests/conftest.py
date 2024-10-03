import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver = None
#def pytest_addoption(parser): ---> Syntax for invoking browser as per our interest or requirement
#    parser.addoption(
#        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
 #   )
#---> in cmd > give as py.test --broswer_name chrome or firefox or IE

#as in default, we have given it as chrome, if we are not mentioning any name then it will open with chrome
#---> Example: py.test --browser_name


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    url = "https://rahulshettyacademy.com/angularpractice/"

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "Internet Explorer":
        driver = webdriver.Ie()

    driver.get(url)
    driver.maximize_window()
    #here we are assigning the local driver to the class object.
    #driver is in fixture but to use it in the class object TestOne,we need to assign in below way
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)