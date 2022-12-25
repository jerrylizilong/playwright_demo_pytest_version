import pytest
from playwright.sync_api import Page,expect
import time

@pytest.fixture(scope='function')
def homepage_driver(page:Page):
    page.goto('https://fanyi.baidu.com/')
    for i in range(5):
        try:
            page.locator("xpath=//span[@class='app-guide-close']").click()
            time.sleep(1)
            break
        except Exception as e:
            print(e)
            time.sleep(1)
    yield page

