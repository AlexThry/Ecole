import time

from selenium.webdriver.common.by import By

from src.Page import Page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import re


if __name__ == "__main__":
    print(os.path.join(os.getcwd(), "DB"))
    page = Page("https://www.polytech.univ-smb.fr/intranet/scolarite/programmes-ingenieur.html")
    page.load()
    page.connection("thierale", "xotgap-5byzwo-qaMqyb")
    linkList = page.getLinks()
    page.getInfosProfs(linkList)


