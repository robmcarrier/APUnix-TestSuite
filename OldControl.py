import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import config
import qatools


class logInScreen(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        ##You need to download the chromedriver(google "chromedriver") and put directory below
        self.driver = webdriver.Chrome(config.chromeDriverlocation, chrome_options=chrome_options)

    def test_userField(self):
        """Check if Username Field is present"""
        driver = self.driver
        driver.get(config.url)
        qatools.checkIfExist(self, driver,"//input[@id='user']")

    def test_password(self):
        driver = self.driver
        driver.get(config.url)
        qatools.checkIfExist(self, driver,"//input[@id='password']")

    def test_page_exists(self):
        driver = self.driver
        driver.get(config.url)
        pageTitle = driver.title
        self.assertEqual(pageTitle, "Log In - Summit Control")

    def test_has_username_no_password(self):
        driver = self.driver
        driver.get(config.url)
        driver.find_element_by_xpath('//input[@id="user"]').send_keys(config.username)
        driver.find_element_by_xpath('//input[@class="Btn2"]').click()
        qatools.checkAlertText(self, driver, "You must fill in both User Login and Password fields to continue.")

    def test_version_alert(self):
        driver = self.driver
        driver.get(config.url)
        driver.find_element_by_xpath('//*[@class="MstLnkLft"]').click()
        qatools.checkAlertText(self, driver, "Summit Enterprise Services 2.01.020b")

    def test_no_username_no_password(self):
        driver = self.driver
        driver.get(config.url)
        driver.find_element_by_xpath('//input[@class="Btn2"]').click()
        qatools.checkAlertText(self, driver, "You must fill in both User Login and Password fields to continue.")

    def test_no_username_has_password(self):
        driver = self.driver
        driver.get(config.url)
        driver.find_element_by_xpath('//input[@id="password"]').send_keys(config.username)
        qatools.clickLogin(driver)
        qatools.checkAlertText(self, driver, "You must fill in both User Login and Password fields to continue.")

    def test_copyright(self):
        driver = self.driver
        driver.get(config.url)
        copyrightText = driver.find_element_by_xpath('//div[@class="logTxtCpy"]').text
        copyrightText = copyrightText[0:10] + copyrightText[11:]
        self.assertEqual(copyrightText, "Copyright 2012 - 2018 by Fire King Security Products, LLC")

    def test_successful_Login(self):
        driver = self.driver
        driver.get(config.url)
        driver.find_element_by_xpath('//input[@id="password"]').send_keys(config.password)
        driver.find_element_by_xpath('//input[@id="user"]').send_keys(config.username)
        driver.find_element_by_xpath('//input[@class="Btn2"]').click()
        pageTitle = driver.title
        self.assertEqual(pageTitle, 'Summit - Reports')
        self.assertEqual(driver.find_element_by_xpath('//td[@class="MstBtmLeft"]/a').text, 'Robert Carrier (SuperAdmin)' )

    def test_forgot_password(self):
        driver = self.driver
        driver.get(config.url)
        driver.find_element_by_xpath('//a[@class="bbLink"]').click()
        forgotTitle = driver.title
        self.assertEqual(forgotTitle, 'Summit - Link Request for Password Reset')

    def tearDown(self):
        self.driver.quit()

class reportsScreen(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        ##You need to download the chromedriver(google "chromedriver") and put directory below
        self.driver = webdriver.Chrome(config.chromeDriverlocation, chrome_options=chrome_options)
        
    def test_regions_available(self):
        """See if Regions dropdown is present"""
        driver = self.driver
        driver.get(config.url)
        qatools.logIn(driver)
        qatools.checkIfExist(self, driver, "//select[@name='region']")


    def test_cities_availables(self):
        driver = self.driver
        driver.get(config.url)
        qatools.logIn(driver)
        qatools.checkIfExist(self, driver,"//select[@name='city']")


    def tearDown(self):
        self.driver.quit()





'''class oldSummitControlHasUser(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        ##You need to download the chromedriver(google "chromedriver") and put directory below
        self.driver = webdriver.Chrome("/home/apunix/robertc/Downloads/chromedriver", chrome_options=chrome_options)


    def tearDown(self):
        self.driver.quit()

'''
if __name__ == '__main__':
    unittest.main()
