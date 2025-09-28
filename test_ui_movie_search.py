from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from KinopoiskUI import Searh_kinopoisk
import allure

@allure.id("Diploma_work_Kinopoisk")
@allure.description("Проверка корректности обработки поисковых запросов через UI")
@allure.feature("SEARCH")
@allure.title("Выполнение поисковых запросов")


def test_searh_kinopoisk_latin():
    with allure.step("Ввод в поле поиска текста на латинице"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        MySearh = Searh_kinopoisk(driver)
        res = MySearh.input_searh("Astral")
        assert res==True
        MySearh.quit_driver()
    


def test_searh_kinopoisk_сyrillic():
    with allure.step("Ввод в поле поиска текста на кириллице"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        MySearh = Searh_kinopoisk(driver)
        res = MySearh.input_searh("Астрал")
        assert res==True
        MySearh.quit_driver()
    
     
def test_searh_kinopoisk_simbol():
    with allure.step("Ввод в поле поиска данных содержащих в запросе специальные символы"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        MySearh = Searh_kinopoisk(driver)
        res = MySearh.input_searh("!!!!")
        assert res==True
        MySearh.quit_driver()
    
     
def test_searh_kinopoisk_ap():
    with allure.step("Ввод в поле поиска данных в верхнем регистре"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        MySearh = Searh_kinopoisk(driver)
        res = MySearh.input_searh("АСТРАЛ")
        assert res==True
        MySearh.quit_driver()
    
    
def test_searh_kinopoisk_a_few_words():
    with allure.step("Ввод в поле поиска нескольких слов"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        MySearh = Searh_kinopoisk(driver)
        res = MySearh.input_searh("Астрал. Глава 2")
        assert res==True
        MySearh.quit_driver()