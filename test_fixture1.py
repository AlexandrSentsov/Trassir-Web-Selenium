from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

@pytest.fixture
def browser():
    link = "https://localhost:8080/webgui/"
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    browser.quit()

class Test_autorization_page():
    @pytest.mark.parametrize('pages', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
    def test_parametrizatsiya(self, browser, pages):
        answer = math.log(int(time.time()))
