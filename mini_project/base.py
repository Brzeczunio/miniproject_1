from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):
    def __init__(self, driver, wait=30, base_url='http://getistqb.com/'):
        self.base_url = base_url
        self.driver = driver
        self.wait = WebDriverWait(driver,wait)

    def find_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def scroll_to_elemet(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        scroll = ActionChains(self.driver).move_to_element(element)
        scroll.perform()
        return element
