import pyautogui
import time
import pyperclip
import pygetwindow as gw
import logging

# Configurer les logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def activate_minecraft_window():
    # Rechercher la fenêtre Minecraft
    window = gw.getWindowsWithTitle('Minecraft')
    if window:
        window[0].activate()
        return True
    return False

def execute_minecraft_command():
    # Activer la fenêtre Minecraft
    if not activate_minecraft_window():
        logging.error("La fenêtre Minecraft n'a pas été trouvée.")
        return

    # Ouvrir le chat Minecraft et exécuter la commande
    pyautogui.press('1')
    time.sleep(6)
    command = f"        /viewauction {pyperclip.paste()}"  # Ajouter le préfixe /viewauction
    time.sleep(3)
    logging.info(f"Exécution de la commande Minecraft : {command}")
    pyautogui.write(command)
    pyautogui.press('enter')
    time.sleep(5)

# Vérifier si le presse-papiers contient la commande
while not pyperclip.paste().startswith('/viewauction'):
    logging.info("La commande n'a pas encore été copiée. Attente de 10 secondes.")
    time.sleep(10)

# Exécuter la commande Minecraft
execute_minecraft_command()
logging.info("Commande Minecraft exécutée.")
