import time

from selenium.webdriver.common.by import By

from src.Page import Page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == "__main__":
    page = Page("https://www.polytech.univ-smb.fr/intranet/scolarite/programmes-ingenieur.html")
    page.load()

    page.writeElement("thierale", CSS_SELECTOR='input[type="text"][id="user"][name="user"]')
    page.writeElement("xotgap-5byzwo-qaMqyb", CSS_SELECTOR='input[type="password"][id="pass"][name="pass"]')
    page.clickElement(CSS_SELECTOR='button[type="button"][id="tarteaucitronPersonalize"][onclick="tarteaucitron.userInterface.respondAll(true);"]')
    page.clickElement(CSS_SELECTOR='input[class="submit"][type="submit"]')
    page.driver.get("https://www.polytech.univ-smb.fr/intranet/scolarite/programmes-ingenieur.html")
    page.clickElement(CSS_SELECTOR='button[name="tx_savfilters_default[submit]"][class="submit"]')
    listeElements = page.findElements(CSS_SELECTOR='div[class="item "]')
    linkList = []
    for element in listeElements:
        linkList.append(element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))

    print(linkList)

