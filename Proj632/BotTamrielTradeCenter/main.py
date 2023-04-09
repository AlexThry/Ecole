from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import datetime
from Class_Database import Database
import random
import os


def random_double():
	return random.randint(3, 7)

def create_database() -> Database:
	"""
	Crée un objet de type Database pour interargire avec la base de donnée
	:return: database : Database
	"""
	database = Database("database.database")
	database.curs.execute(
		"CREATE TABLE IF NOT EXISTS Item (idItem INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, level VARCHAR, image VARCHAR)")
	database.curs.execute(
		"CREATE TABLE IF NOT EXISTS Sale (idSale INTEGER PRIMARY KEY AUTOINCREMENT, vendor VARCHAR, location VARCHAR, guild VARCHAR, price DOUBLE, date DATE, idItem INTEGER REFERENCES Item (idItem))")
	database.conn.commit()
	return database


# def sleep():
# 	time.sleep(random_double())


def set_nb(msg):
	"""
	Permet à l'utilisateur de choisir un nombre entier
	:param msg: Message à afficher
	:return: Un nombre entier
	"""
	try:
		res = int(input(msg))
		if res <= 5000:
			return res
		else:
			print("Veuillez entrer une valeur correcte")
	except ValueError:
		print("Veuillez entrer une valeur numérique")


def get_items() -> list:
	"""
	Permet de récupérer la liste des élement items sur la page actuelle
	:return: liste d'objets 'WebElement'
	"""
	try:
		WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.cursor-pointer")))
		item_list = driver.find_elements(By.CSS_SELECTOR, "tr.cursor-pointer")
	except :
		WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.cursor-pointer")))
		item_list = driver.find_elements(By.CSS_SELECTOR, "tr.cursor-pointer")
	return item_list


def get_page_item_info(item):
	"""
	Permet de récupérer les infos d'un item
	:param item: WebElement: un item
	:return: tuple: la liste des charactéristiques d'un objet
	"""
	try:
		item_text = item.text.split('\n')
		item_name = item_text[0].translate(str.maketrans('', '', "'"))
		item_image = item.find_element(By.CSS_SELECTOR, "img.trade-item-icon").get_attribute("src")
		level = item_text[1].split(' ')
		if level[0] == "Level":
			item_level = item_text[1]
		else:
			item_level = "Level 1"
		return item_name, item_level, item_image
	except:
		print("Erreur : Impossible d'accéder à l'item")


def get_page_sale_info(item) -> tuple:
	"""
	Permet de récupérer les infos d'une vente
	:param item: WebElement: un item
	:return: tuple: la liste des charactéristiques d'une vente
	"""
	item_text = item.text.split('\n')
	vendor = item_text[2].translate(str.maketrans('', '', "'"))
	location = item_text[3].translate(str.maketrans('', '', "'"))
	guild = item_text[4].translate(str.maketrans('', '', "'"))
	price = ""
	for i in item_text[5].split("\u202f"):
		price += i

	date = datetime.datetime.now().strftime("%Y-%m-%d").split(' ')[0]
	return vendor, location, guild, price, date


def get_all_price(item_name) -> list:
	"""
	Renvoie la liste de tous les prix anisi que les dates de vente stocké dans la base de donnée pour un item donné.
	:param item_name: str: nom de l'objet (en anglais)
	:return: list: liste de tupe sous la forme (prix, date_de_vente)
	"""
	db = Database("database.db")
	sale_info = db.get_sale_info(item_name)
	price_by_date = []
	for item in sale_info:
		price_by_date.append((item[4], item[5]))
	return price_by_date


def medium_price_by_day(item_name) -> dict:
	"""
	Renvoie le dict des prix moyen de vente d'un item par jour d'après les données récupérées
	:param item_name: str: nom de l'objet (en anglais)
	:return: dict: dictionnaire des prix moyens de l'item par jour
	"""
	price_by_date = get_all_price(item_name)
	medium_price_by_day = {}
	sum_price = price_by_date[0][0]
	date = price_by_date[0][1]
	nb_item = 1
	for item in price_by_date:
		if item[1] == date:
			sum_price += item[0]
			nb_item += 1
		else:
			medium_price_by_day[date] = sum_price / nb_item
			sum_price = item[0]
			date = item[1]
			nb_item = 1
	medium_price_by_day[date] = sum_price / nb_item
	return medium_price_by_day


def graph_price(item_name) -> None:
	"""
	Permet d'afficher l'évolution du prix moyen d'un item d'apres les données récupérées
	:param item_name:
	:return:
	"""
	lists = sorted(medium_price_by_day(item_name).items())
	date, price = zip(*lists)
	plt.figure()
	plt.plot(date, price)
	plt.show()


def add_page(item_list) -> None:
	"""
	Permet d'ajouter une page entière à la base de donnée
	:param item_list: list: liste d'objets WebElement
	:return: None
	"""
	database = Database("database.db")
	for item in item_list:
		try:
			name, level, image = get_page_item_info(item)
			database.add_item(name, level, image)
			vendor, location, guild, price, date = get_page_sale_info(item)
			idItem = database.get_idItem(name, level)
			database.add_sale(vendor, location, guild, price, date, idItem)
		except:
			print("Erreur : item/vente non ajouté")


def get_last_user_agent() -> list:
	"""
	Permet de récupérer une liste d'user_agent recente pour le bot
	:return: list
	"""
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
	try:
		driver.get("https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome")
		WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "code")))
		user_agents = driver.find_elements(By.CLASS_NAME, 'code')
		text_user_agents = []
		for ua in user_agents:
			text_user_agents.append(ua.text)
		driver.close()
	except:
		text_user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
							"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"]

	return text_user_agents


if __name__ == "__main__":
	continue_ = True
	while continue_:
		res = input("1. Scrapper \n2. Comparer les prix\n3. Quitter\n")
		if res == "1":

			# Récupération de la page max de récupération des données
			nb_pages = None
			while not nb_pages:
				nb_pages = set_nb("Jusqu'ou voullez vous 'Scrapper' ? (max = 5000) \n")
			print("On my way ...")

			# Récupération des derniers user agent disponibles pour éviter la détéction du bot
			user_agents = get_last_user_agent()
			print("Je suis invisible ... ")

			# Crée un point de départ aléatoire pour éviter la détéction du bot
			starting_page = int(random.randint(1, nb_pages)/2)

			# Création d'un objet Database pour interargire avec la BDD
			db = create_database()

			# récupère le chemin actuel pour trouver l'extension AdBlock
			current_path = os.getcwd()
			adblock = os.path.join(current_path, "extension_5_3_3_0.crx")

			# Création des options pour le lancement de Chrome
			options = webdriver.ChromeOptions()

			# choix aléatoire du user_agent pour éviter la détéction du bot
			ua = random.choice(user_agents)
			options.add_argument(f'user-agent={ua}')

			# Ajout de AdBlock pour éviter le bloquage du bot à cause des pubs
			options.add_extension(adblock)

			# Taille de la fenetre aléatoire pour éviter la détéction du bot
			length = random.randint(1000, 1100)
			width = random.randint(700, 800)
			options.add_argument(f"window-size={length},{width}")

			# Création d'une fenetre chrome avec le téléchargement et la mise a jour automatique du driver
			driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

			# Aquisition de la page voulue
			driver.get(f"https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?page={starting_page}")

			i = 0

			# Passage sur le bon onglet
			while i < len(driver.window_handles):
				driver.switch_to.window(driver.window_handles[i])
				if driver.title == "Search Result - Tamriel Trade Centre":
					break
				i += 1

			page = starting_page
			while page <= nb_pages:

				# Fermeture du message d'avertissement sur adblock si il apparait
				try:
					driver.find_element(By.XPATH, '//*[@id="adblock-detected-modal"]/div/div/div[2]/button').click()
				except:
					pass

				# Récupération et ajout des items dans la BDD
				items = get_items()
				add_page(items)

				# Attente d'un temps aléatoire pour éviter la détéction du bot
				driver.implicitly_wait(random_double())

				# L'adresse du bouton pour passer à la page suivante change à partir de la page 6
				if page <= 6:
					driver.find_element(By.XPATH, '//*[@id="search-result-view"]/div[1]/div/div/ul/li[14]/a').click()
				else:
					driver.find_element(By.XPATH, '//*[@id="search-result-view"]/div[1]/div/div/ul/li[16]/a').click()
				driver.implicitly_wait(random_double())
				page += 1
			driver.quit()
		elif res == "3":
			break
		else:
			# affichage du graph pour l'item demandé
			try:
				graph_price(input("Veuillez donner le nom de l'item :\n"))
			except IndexError:
				print("L'item demandé n'a pas été trouvé")
