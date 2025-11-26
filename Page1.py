from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
import logging
import pyperclip

# Configurer les logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Chemin vers ChromeDriver
chrome_driver_path = 'C:/Program Files (x86)/chromedriver-win32/chromedriver.exe'

# Configurer le service Chrome
service = Service(executable_path=chrome_driver_path)

# Configurer le driver Chrome
driver = webdriver.Chrome(service=service)
driver.get('https://sky.coflnet.com/flipper')

# Attendre que l'utilisateur configure les conditions
time.sleep(10)  # Ajustez le temps de pause si nécessaire

logging.info("Début de la recherche de l'élément 'cost'...")


def search_and_click_first_cost():
    # Localiser tous les éléments contenant le texte "cost"
    try:
        cost_elements = driver.find_elements_by_xpath("//*[contains(text(), 'cost')]")
        if cost_elements:
            logging.info(f"{len(cost_elements)} éléments 'cost' trouvés.")

            # Parcourir les éléments "cost" et cliquer sur le premier
            cost_element = cost_elements[0]
            location = cost_element.location
            size = cost_element.size
            logging.info(f"Premier élément 'cost' trouvé à la position : {location}")

            # Calculer la position de clic
            x = location['x'] + size['width'] / 2
            y = location['y'] + size['height'] / 2

            # Cliquer sur l'élément trouvé
            pyautogui.moveTo(x, y)
            time.sleep(1)  # Délai pour observer le déplacement de la souris
            pyautogui.click(button='left')
            logging.info("Premier élément 'cost' cliqué et lien copié.")
        else:
            logging.error("Aucun élément 'cost' trouvé.")
    except Exception as e:
        logging.error(f"Erreur lors de la localisation des éléments 'cost' : {e}")

    # Afficher le lien copié dans les logs
    copied_link = pyperclip.paste()
    if copied_link.startswith('/viewauction'):
        logging.info(f"Lien copié : {copied_link}")
    else:
        logging.error("Le lien copié ne semble pas correct.")


search_and_click_first_cost()

driver.quit()
logging.info("Recherche terminée. Fenêtre du navigateur fermée.")
