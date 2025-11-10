import requests
import allure
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.data import Constants

class TestGetOrder:

    @allure.title('Получение заказов авторизованного пользователя')
    @allure.description('Отправляем GET запрос, проверяем тело и статус ответа')
    def test_get_orders_auth_user_response_status_code_200(self, create_user_order):

        login_pass_name_token = create_user_order

        response = requests.get(f"{Constants.url_burger}/api/orders", headers={'Authorization': login_pass_name_token[3]})


        assert response.status_code == 200 and response.json()['success'] == True and response.json()['orders']!= []


    @allure.title('Получение заказов не авторизованного пользователя')
    @allure.description('Отправляем GET запрос, проверяем тело и статус ответа')
    def test_get_orders_not_auth_user_response_status_code_401(self):



        response = requests.get(f"{Constants.url_burger}/api/orders")


        assert response.status_code == 401 and response.json()['message'] == Constants.error_message_not_authorised