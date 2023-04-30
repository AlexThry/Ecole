import time

from selenium.webdriver.common.by import By

from src.Page import Page
import matplotlib.pyplot as plt
from src import DBAgent

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import re


if __name__ == "__main__":
    db = DBAgent.DBAgent()
    res = True
    while res:
        response = input("1: Scrapper\n2: Quitter\n")
        if response == "1":
            # login = input("Login Intranet :\n")
            # password = input("Password Intranet :\n")
            print("ok...")
            page = Page("https://www.polytech.univ-smb.fr/intranet/scolarite/programmes-ingenieur.html")
            page.load()
            #page.connection("thierale", "xotgap-5byzwo-qaMqyb")
            #linkList = page.getLinks()
            #page.getInfosProfs(linkList)
            page.getArticlesProfs(page.dbagent.getAllProfs())
        else:
            res = False





