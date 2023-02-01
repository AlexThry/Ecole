from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Page:
	def __init__(self, url):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager.install()))
		self.url = url

	def load(self):
		self.driver.get(self.url)

	

