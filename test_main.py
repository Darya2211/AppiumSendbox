import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from appium.options.android import UiAutomator2Options

# adb shell dumpsys window|find "mCurrentFocus"

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='R8YW707D0RL',
    # appPackage='com.sec.android.app.launcher',
    platformVersion='13',
    appActivity='.Camera',
    language='en',
    locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()


def test_find_battery(driver) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
    sleep(5)


def test_camera(driver):
    setting_button = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Go to Settings"]')
    setting_button.click()
    driver.press_keycode(3)
    sleep(5)


def test_facebank(driver):
    facebank_icon = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Facebank"]')
    facebank_icon.click()
    sleep(5)
    start_search = driver.find_element(AppiumBy.XPATH,
                                       '//android.widget.Button[@content-desc="Начать работу"]')
    start_search.click()
    sleep(5)