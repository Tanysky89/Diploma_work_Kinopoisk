import requests
import allure

@allure.epic("Функция поиска контента. Фильмы, сериалы, персоны") 
@allure.severity("blocker")

class kinopoiskApi:
    @allure.step("Получение полного списка контента. Выборка ID")
    def get_first_film_id(self, api_key):
        headers = {
            'X-API-KEY': api_key,
            'accept': 'application/json'
        }
    
        response = requests.get(
            'https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10',
            headers=headers
        )
    
        if response.status_code != 200:
            raise Exception(f'Ошибка при получении списка: {response.text}')
    
        data = response.json()
        first_film = data['docs'][0]['id']  
        return first_film
   
   
    @allure.step("Поиск по ID")
    def searh_film_id(self, api_key, id):
        headers = {
            'X-API-KEY': api_key,
            'accept': 'application/json'
            }
    
        response = requests.get(
            'https://api.kinopoisk.dev/v1.4/movie/' + str(id),
            headers=headers
        )
    
        if response.status_code != 200:
            raise Exception(f'Ошибка при получении списка фильмов: {response.text}')
    
        data = response.json()
        return data
        

    @allure.step("Универсальный поиск с фильтрами")
    def searh_film(self, api_key, filter_list):
        headers = {
            'X-API-KEY': api_key,
            'accept': 'application/json'
            }
        str_filter = "?"
        for key in filter_list:
            str_filter = str_filter + str(key) + "=" + str(filter_list[key]) + "&"
        str_filter = str_filter[:-1]
                
        response = requests.get(
            'https://api.kinopoisk.dev/v1.4/movie' + str_filter,
            headers=headers
        )
    
        if response.status_code != 200:
            raise Exception(f'Ошибка при получении списка: {response.text}')
    
        data = response.json()
        return data











    