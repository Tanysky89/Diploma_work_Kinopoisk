import allure
from KinopoiskApi import kinopoiskApi
from authorization import token
import allure

api = kinopoiskApi()
api_token = token()
api_key = api_token._api_key

@allure.id("Diploma_work_Kinopoisk")
@allure.description("Проверка корректности обработки поисковых запросов через API")
@allure.feature("SEARCH")
@allure.title("Выполнение поисковых запросов")


def test_api_movie_search_by_ID():
    with allure.step("Получение ID первого фильма из списка"):
        id_movie = api.get_first_film_id(api_key)
        
    with allure.step("Поиск фильма по {id_movie}"):
        Movie_srh = api.searh_film_id(api_key, id_movie)
        
    with allure.step("Проверка на корректность вывода результата поиска"):
        assert Movie_srh['id'] == id_movie, "ОШИБКА"
    

def test_api_movie_search_2025():
    with allure.step("Поиск российских фильмов за 2025 год"):
        year = 2025
        str_type = "movie"
        country_name = "Россия"
    
        search_struct = {
            "year":year,
            "type":str_type,
            "countries.name":country_name
        }
        res = api.searh_film(api_key, search_struct) 
        first_film = res["docs"][0]
        assert first_film['year'] == year ,"Ошибка отбора по году!"
        assert first_film['type'] == str_type, "Ошибка отбора по типу"
        assert first_film['countries'][0]['name'] == country_name, "Ошибка отбора по стране"
       
    
def test_api_movie_search_18():
    with allure.step("Поиск фильмов с возрастным ограничением 18+"):
        str_ageRating = 18
        str_type = "movie"
    
        search_struct = {
            "ageRating":str_ageRating,
            "type":str_type
        }
        res = api.searh_film(api_key, search_struct) 
        first_film = res["docs"][0]
        assert first_film['ageRating'] == str_ageRating ,"Ошибка отбора по возрстному ограничению!"
        assert first_film['type'] == str_type, "Ошибка отбора по типу"
     

def test_api_movie_search_kp7():
    with allure.step("Поиск фильмов в жанре ужасы с рейтингом Кинопоиска 7"):
        str_genres = "ужасы"
        str_type = "movie"
        str_rating = 7
    
        search_struct = {
            "genres.name":str_genres,
            "type":str_type,
            "rating.kp": str_rating
        }
        res = api.searh_film(api_key, search_struct) 
        first_film = res["docs"][0]
        assert first_film['genres'][0]['name'] == str_genres ,"Ошибка отбора по жанрам!"
        assert first_film['type'] == str_type, "Ошибка отбора по типу"
        assert first_film['rating']['kp'] == str_rating, "Ошибка отбора по рейтингу Кинопоиска"


def test_api_series_search():
    with allure.step("Поиск сериалов с продолжительностью одной серии 20 минут"):
        str_seriesLength = 20
        str_type = "tv-series"
    
        search_struct = {
            "seriesLength":str_seriesLength,
            "type":str_type
        }
        res = api.searh_film(api_key, search_struct) 
        first_film = res["docs"][0]
        assert first_film['seriesLength'] == str_seriesLength ,"Ошибка отбора по длинне серии!"
        assert first_film['type'] == str_type, "Ошибка отбора по типу"
    

    
        



