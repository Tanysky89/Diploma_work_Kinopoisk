from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import allure

@allure.epic("Функция поиска контента. Фильмы, сериалы, персоны") 
@allure.severity("blocker")

class Searh_kinopoisk:
    @allure.step("Открытие сайта")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.kinopoisk.ru")
        WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable((By.NAME, 'kp_query'))
        )
        
    @allure.step("Ввод текста в поиск")
    def input_searh(self, searh_txt):
        searh_input = self._driver.find_element(By.NAME, 'kp_query')
        searh_input.send_keys(searh_txt)
        searh_input.send_keys(Keys.ENTER)
        res = self._driver.find_element(By.CLASS_NAME, 'search_results_topText')
        if searh_txt in res.text:
            return True
        else:
            return False
         
    @allure.step("Закрытие сессии")
    def quit_driver(self):
       self._driver.quit()