from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Опции для обхода Cloudflare
options = webdriver.EdgeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable automation"])
options.add_experimental_option("useAutomationExtension", False)

fifa = random.randint(17, 22) #Fifa
page = random.randint(1, 15) # Страница игроков
random_player = random.randint(0, 29) # Выбор игрока на странице

# Функция для выбора рандомного игрока
def random_url(a, b):
    player_url = f"https://www.futbin.com/{a}/players?page={b}&order=desc&sort=likes"
    return player_url

driver = webdriver.Edge(executable_path="msedgedriver.exe", options=options)

# Опции для обхода Cloudflare
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    '''
})

try:
    url = random_url(fifa, page)
    driver.maximize_window() # 
    driver.get(url=url)
    time.sleep(10)

    element = driver.find_elements(By.CLASS_NAME, "player_name_players_table")[random_player]
    element.click()
    time.sleep(10)

    # Убрать часть картинки
    player_image = driver.find_element(By.ID, "Player-card").screenshot("img/4-player.png") # Скришнот игрока

    # Легкий уровень
    driver.execute_script("document.getElementsByClassName('pcdisplay-name')[0].style.visibility='hidden';") # Имя
    driver.execute_script("document.getElementsByClassName('pcdisplay-rat')[0].style.visibility='hidden';") # Рейтинг
    driver.execute_script("document.getElementsByClassName('pcdisplay-picture')[0].style.visibility='hidden';") # Фото
    easy_image = driver.find_element(By.ID, "Player-card").screenshot("img/3-easy.png") # Скришнот игрока

    # Средний уровень
    driver.execute_script("document.getElementsByClassName('pcdisplay-club')[0].style.visibility='hidden';") # Клуб
    mid_image = driver.find_element(By.ID, "Player-card").screenshot("img/2-mid.png") # Скришнот игрока

    # Тяжелый уровень
    driver.execute_script("document.getElementsByClassName('pcdisplay-country')[0].style.visibility='hidden';") # Страна
    image = driver.find_element(By.ID, "Player-card").screenshot("img/1-hard.png") # Скришнот игрока

    # driver.execute_script("document.getElementsByClassName('pcdisplay-pos')[0].style.visibility='hidden';") # Позиция

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()