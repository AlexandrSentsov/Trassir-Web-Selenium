import pytest
from selenium import webdriver

link = "https://172.16.14.151:8080/webgui/"

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.get(link)
    try:
        browser.find_element_by_id("details-button").click()
        browser.find_element_by_id("proceed-link").click()
    except:
        pass
    yield browser
    print("\nquit browser..")
    browser.quit()