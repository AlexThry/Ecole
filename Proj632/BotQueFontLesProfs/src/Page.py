from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

class Page:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def load(self):
        self.driver.get(self.url)

    def findElement(self, XPATH:str=None, CLASS_NAME:str=None, CSS_SELECTOR:str=None):
        if XPATH:
            WebDriverWait(self.driver, 40).until(ec.element_to_be_clickable((By.XPATH, XPATH)))
            return self.driver.find_element(By.XPATH, XPATH)
        elif CLASS_NAME:
            WebDriverWait(self.driver, 40).until(ec.element_to_be_clickable((By.CLASS_NAME, CLASS_NAME)))
            return self.driver.find_element(By.CLASS_NAME, CLASS_NAME)
        elif CSS_SELECTOR:
            WebDriverWait(self.driver, 40).until(ec.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR)))
            return self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)

    def findElements(self, CLASS_NAME:str=None, CSS_SELECTOR:str=None):
        if CLASS_NAME:
            WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located((By.CLASS_NAME, CLASS_NAME)))
            return self.driver.find_elements(By.CLASS_NAME, CLASS_NAME)
        elif CSS_SELECTOR:
            WebDriverWait(self.driver, 40).until(ec.visibility_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR)))
            return self.driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR)

    def clickElement(self, XPATH:str=None, CLASS_NAME:str=None, CSS_SELECTOR:str=None):
        self.findElement(XPATH, CLASS_NAME, CSS_SELECTOR).click()


    def writeElement(self, text, XPATH:str=None, CLASS_NAME:str=None, CSS_SELECTOR:str=None):
        self.findElement(XPATH, CLASS_NAME, CSS_SELECTOR).send_keys(text)

