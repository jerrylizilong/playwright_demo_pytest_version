import os.path
import time

import pytest,allure
from playwright.sync_api import Page,expect
import playwright

@pytest.mark.parametrize('keyword,language,result',[
    ('test','英语','测验'),
    ('android','英语','安卓'),
    ('mobile','英语','可移动的'),
    ('country','英语','国'),
    ('value','英语','价值'),
    ('football','英语','足球运动'),
    ('篮球','中文(简体)','Basketball'),
    ('Futebol','葡萄牙语','足球运动'),
    ('ワールドカップ','日语','世界杯'),
    ('网球','中文(简体)','Tennis'),
    ('Copa del mundo','西班牙语','世界杯'),
    ('足球','中文(简体)','Football'),

])
@allure.story('test baidu translate with playwright')
def test_baidu_translate(homepage_driver,keyword,language,result):
    homepage_driver.locator('id=baidu_translate_input').clear()
    homepage_driver.locator('id=baidu_translate_input').fill(keyword)
    actual_language =  homepage_driver.locator("xpath=//span[@class='language-selected']/span").text_content()
    actual_result = homepage_driver.locator("xpath=//p[contains(@class,'target-output')]/span").text_content()

    current_timestamp = str(int(time.time()*100))

    filename = ("%s-%s-%s-%s.png" %(keyword,language,result,current_timestamp)).strip()
    filename = os.path.join(os.curdir,'screenshots',filename)
    homepage_driver.screenshot(path=filename)

    allure.attach.file(filename,name=filename)
    assert actual_result == result
    assert actual_language == language

