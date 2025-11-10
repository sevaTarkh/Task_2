import requests
import allure
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.data import Constants

class TestCreateOrder:

    @allure.title('Создание заказа авторизованного пользователя')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_create_order_hash_ingredients_response_status_code_200(self, create_user_and_delete_after):

        login_pass_name_token = create_user_and_delete_after

        payload = {
            "ingredients": Constants.ingredients_hash
        }

        response = requests.post(f"{Constants.url_burger}/api/orders", data=payload, headers={'Authorization': login_pass_name_token[3]})


        assert response.status_code == 200 and response.json()['success'] == True


    @allure.title('Создание заказа не авторизованного пользователя')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_create_order_hash_ingredients_not_auth_user_response_status_code_200(self):

        payload = {
            "ingredients": Constants.ingredients_hash
        }

        response = requests.post(f"{Constants.url_burger}/api/orders", data=payload)


        assert response.status_code == 200 and response.json()['success'] == True and response.json()['name'] == Constants.name_burger


    @allure.title('Создание заказа без ингредиентов')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_create_order_with_out_ingredients_response_status_code_400(self, create_user_and_delete_after):

        login_pass_name_token = create_user_and_delete_after
        payload = {
            "ingredients":[]
        }

        response = requests.post(f"{Constants.url_burger}/api/orders", data=payload, headers={'Authorization': login_pass_name_token[3]})


        assert response.status_code == 400 and response.json()['message'] == Constants.error_message_ingredient_ids_must_be_provided


    @allure.title('Создание заказа с некорректным хешом ингредиентов')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_create_order_wrond_ingredients_response_status_code_500(self, create_user_and_delete_after):

        login_pass_name_token = create_user_and_delete_after
        payload = {
            "ingredients": Constants.wrong_hash
        }

        response = requests.post(f"{Constants.url_burger}/api/orders", data=payload, headers={'Authorization': login_pass_name_token[3]})


        assert response.status_code == 500