# from Class_Database import Database
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec



class WebRequests:
    def __init__(self, url=None):
        if url:
            self.response = requests.get(url).json()


    def get_pokemons(self):
        return self.response["results"]



    def get_pokemons_infos(self):
        pokemons = self.get_pokemons()
        pokemons_infos = []
        for pokemon in tqdm(pokemons, desc="Récupération des pokémons", ncols=150):
            name = pokemon["name"]
            pokemonPage = requests.get(pokemon["url"]).json()
            abilities = pokemonPage["abilities"]
            sprites = pokemonPage["sprites"]
            pokemon_info = {"name": name, "abilities": abilities, "sprites": sprites}
            pokemons_infos.append(pokemon_info)
        return pokemons_infos






    def get_abilities(self, pokemons_infos):
        """
        Récupère toutes les abilités des pokémons
        :param pokemons_infos: liste de dict renvoyés par get_pokemons_infos
        :return: un dictionnaire d'abilitées {nomAbilité: description}
        """
        abilities = {}
        for pokemon in tqdm(pokemons_infos, desc="Récupération des abilitées", ncols=150):
            for ability in pokemon["abilities"]:
                name = ability["ability"]["name"]
                response = requests.get(ability["ability"]["url"]).json()
                for entrie in response["effect_entries"]:
                    try:
                        if entrie["language"]["name"] == "en":
                            description = entrie["effect"]

                        abilities[name] = description
                    except UnboundLocalError:
                        abilities[name] = "Pas de description"
        return abilities


    def get_items(self, nbPages=None):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://bulbapedia.bulbagarden.net/wiki/Category:Items")
        self.driver.delete_cookie("addtl_consent")
        self.driver.add_cookie({'name': 'gdpr-dau-log-sent', 'value': 'true'})
        self.driver.add_cookie({'name': 'euconsent-v2', 'value': 'CPqucEAPqucEAADABBFRC4CsAP_AAH_AAAAAIBoF5CpURCFD4GJoIJIUIAEXwFAAACAgBgQBA4AASBCAMAwEkAAAEAAAIAAAAAAAIAIAAAAACAkAAAAAQIABAQAAAAQAAAAAIAAAAAAAEAAAAAgAAoAAEAAAAAAAACAAgAAAAAIAQAAAAAAAAQAAAAAAAAAAAAAAAAAAQAAAQAAAAIHyIF5CpURCFDYGBoIJIUIAEXQFAAACAgBgABAwAACBCAMAwAkAAAAAAAIAAAAAAAIAIAAAAAAAkAAAAAQIABAQAAAAQAAAAAIAAAAAAAEAAAAAgAAoAAEAAAAAAAACAAgAAAAAIAQAAAAAAAAQAAAAAAAAAAAAAAAAAAQAAAQAAA.YAAAAAAAA4AA'})
        self.driver.add_cookie({'name': 'gdpr-dau', 'value': 'true'})
        self.driver.add_cookie({'name': '__adblocker', 'value': 'false'})
        self.driver.add_cookie({'name': '_lr_geo_location', 'value': 'FR'})
        self.driver.add_cookie({'name': 'addtl_consent', 'value': '1~7.162.440.448.505.867.1215.1516.2133.2544.2595.2642.3033.3111'})
        self.driver.add_cookie({'name': '_pbjs_userid_consent_data', 'value': 'CPqucEAPqucEAADABBFRC4CgAPgAAAAAAAABmbwHwAEgAMAA6AGEAUIAqoBpAGnANoA24BwAHCAOsAeIA9gCKAEWAI0AR0ApQnFxPZCjIFGgKQkVOYrzxZ-C9lGIAMTMYsQy6RmbgAAAAA.YAAAAAAAAAA'})
        self.driver.add_cookie({'name': 'cconsent-v2', 'value': '120946179071196'})
        self.driver.add_cookie({'name': 'gdpr-auditId', 'value': '0ba47353135f4976b73892e2d07e7d1b'})
        self.driver.get("https://bulbapedia.bulbagarden.net/wiki/Category:Items")
        links = self.driver.find_element(By.CSS_SELECTOR, "#mw-subcategories > div > div").find_elements(By.CSS_SELECTOR, "a")

        items_cat = {}
        links_txt = []
        if nbPages:
            for link in links[7:7+nbPages]:
                links_txt.append(link.get_attribute("href"))
        else:
            for link in links[7:]:
                links_txt.append(link.get_attribute("href"))

        for link in tqdm(links_txt, desc="Ajout des items", ncols=150):
            self.driver.get(link)
            cat = self.driver.find_element(By.CSS_SELECTOR, "h1").text
            resp = self.driver.find_element(By.CSS_SELECTOR, "#mw-content-text").find_elements(By.CSS_SELECTOR, "a")
            items = {}
            for i in resp:
                items[i.text] = i.get_attribute("href")
            items_cat[cat] = items
        self.driver.quit()
        self.driver.stop_client()
        return items_cat













if __name__ == "__main__":

    wr = WebRequests()
    print(wr.get_items())
