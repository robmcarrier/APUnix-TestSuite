import config
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def logIn(driver):
    driver.find_element_by_xpath('//input[@id="password"]').send_keys(config.password)
    driver.find_element_by_xpath('//input[@id="user"]').send_keys(config.username)
    driver.find_element_by_xpath('//input[@class="Btn2"]').click()

def checkIfExist(self, driver, xpath):
    try: driver.find_element_by_xpath(xpath)
    except NoSuchElementException: self.assertTrue(False)
    return True

def checkAlertText(self, driver, expectedText):
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alertone = self.driver.switch_to.alert
        alert_text = alertone.text
        self.assertEqual(alert_text, expectedText)
    except TimeoutException:
        self.assertTrue(False)

def clickLogin(driver):
    driver.find_element_by_xpath('//input[@class="Btn2"]').click()
