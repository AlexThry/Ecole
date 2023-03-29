from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from src.DBAgent import DBAgent
from tqdm import tqdm
import time
import re

class Page:
    def __init__(self, url):
        self.dbagent = DBAgent()
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
        
    def wait(self, duration:float):
        time.sleep(duration)
        
        
        
        
    def connection(self, login:str, password:str):
        self.writeElement(login, CSS_SELECTOR='input[type="text"][id="user"][name="user"]')
        self.writeElement(password, CSS_SELECTOR='input[type="password"][id="pass"][name="pass"]')
        self.clickElement(CSS_SELECTOR='button[type="button"][id="tarteaucitronPersonalize"][onclick="tarteaucitron.userInterface.respondAll(true);"]')
        self.clickElement(CSS_SELECTOR='input[class="submit"][type="submit"]')
        
    def getLinks(self):
        self.driver.get("https://www.polytech.univ-smb.fr/intranet/scolarite/programmes-ingenieur.html")
        self.clickElement(CSS_SELECTOR='button[name="tx_savfilters_default[submit]"][class="submit"]')
        listeElements = self.findElements(CSS_SELECTOR='div[class="item "]')
        
        
        linkList = []
        for element in listeElements:
            linkList.append(element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))
        return linkList[40:]
    
    def getInfosProfs(self, linkList):
        profList = []
        for link in tqdm(linkList):
            self.driver.get(link)
            self.wait(0.2)
            prof = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="item"]')[2].find_element(By.CSS_SELECTOR, 'div[class="value"]').text
            profs = re.split("[,;]", prof)
            
            for prof in profs:
                if (prof != ""):
                    self.dbagent.addProf(prof.upper().strip())
                module = self.findElement(CSS_SELECTOR='div[class="titleLabel"]').text
                if (module != ": -"):
                    self.dbagent.addModule(module.strip())
                    self.dbagent.addParticipation(module.strip(), profs)
                    
        
                
            
                