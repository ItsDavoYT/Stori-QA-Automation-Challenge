# Program Name : StoriChallenge               #
# Developer Name : David Rodriguez de la Cruz #
# Date of code Development : 11/27/2021       #

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class StoriChallenge():

    def __init__(self):

        self.radioStep()
        self.suggestionBoxStep()
        self.dropDownStep()
        self.checkBoxesStep()
        self.switchToAlertStep()
        self.elementDisplayedStep()

    def radioStep(self):
        driver = self.webBrowserInit()
        # Radio Button
        radio = driver.find_element_by_css_selector(
            'input[value=\'radio2\']').click()
        time.sleep(1)
        radio = driver.find_element_by_css_selector(
            'input[value=\'radio3\']').click()
        time.sleep(1)
        radio = driver.find_element_by_css_selector(
            'input[value=\'radio1\']').click()
        time.sleep(3)
        driver.close()

    def suggestionBoxStep(self):

        driver = self.webBrowserInit()
        # Suggestion
        suggestionBox = driver.find_element_by_xpath(
            '//input[@id=\'autocomplete\']')
        suggestionBox.send_keys('Me')
        time.sleep(2)
        selection = driver.find_element_by_xpath(
            '//div[@id=\'ui-id-7\']').click()
        time.sleep(3)
        driver.close()

    def dropDownStep(self):

        driver = self.webBrowserInit()
        # Drop Down
        dropList = driver.find_element_by_xpath(
            '//select[@id=\'dropdown-class-example\']').click()
        time.sleep(1)
        option = driver.find_element_by_xpath(
            '//*[@id="dropdown-class-example"]/option[3]').click()
        time.sleep(1)
        dropList = driver.find_element_by_xpath(
            '//select[@id=\'dropdown-class-example\']').click()
        time.sleep(1)
        dropList = driver.find_element_by_xpath(
            '//select[@id=\'dropdown-class-example\']').click()
        time.sleep(1)
        option = driver.find_element_by_xpath(
            '//*[@id="dropdown-class-example"]/option[4]').click()
        time.sleep(1)
        dropList = driver.find_element_by_xpath(
            '//select[@id=\'dropdown-class-example\']').click()
        time.sleep(3)
        driver.close()

    def checkBoxesStep(self):

        driver = self.webBrowserInit()
        # Check Boxes
        check2 = driver.find_element_by_css_selector(
            '#checkBoxOption1').click()
        time.sleep(1)
        check2 = driver.find_element_by_css_selector(
            '#checkBoxOption2').click()
        time.sleep(3)
        driver.close()

    def switchToAlertStep(self):

        driver = self.webBrowserInit()
        # Switch to Alert
        alertBoxText = driver.find_element_by_xpath('//input[@id=\'name\']')
        alertBoxText.send_keys('Stori Card')
        time.sleep(1)
        alertButton = driver.find_element_by_css_selector('#alertbtn').click()
        time.sleep(1)
        alert = driver.switch_to.alert
        print("*---------------Text in Alert-----------------*")
        print("Text in alert: " + alert.text)
        alert.accept()
        time.sleep(3)
        driver.close()

    def elementDisplayedStep(self):

        driver = self.webBrowserInit()
        # Element Displayed Example
        print("*---------- -Element Displayed----------------*")

        textBox = driver.find_element_by_css_selector('#displayed-text')

        hideButton = driver.find_element_by_xpath(
            '//input[@id=\'hide-textbox\']').click()
        time.sleep(1)

        if textBox.is_displayed():
            print("Element is visible")
        else:
            print("Element is hidden")

        showButton = driver.find_element_by_xpath(
            '//input[@id=\'show-textbox\']').click()
        time.sleep(1)

        if textBox.is_displayed():
            print("Element is visible")
        else:
            print("Element is hidden")

        time.sleep(3)
        driver.close()

    def webBrowserInit(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')

        return driver


test = StoriChallenge()
test.__init__
