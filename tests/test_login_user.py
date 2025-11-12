import requests
import allure
import sys
from datetime import datetime
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.data import Constants

class TestLogunUser:

    @allure.title('Авторизация пользователя')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_login_user_email_password_response_status_code_200(self, create_user_and_delete_after):

        login_pass_name = create_user_and_delete_after

        payload = {
            "email": login_pass_name[0],
            "password": Constants.password
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/login", data=payload)


        assert response.status_code == 200 and response.json()['success'] == True and response.json()['user'] == {"email": login_pass_name[0], "name": login_pass_name[2]}


    @allure.title('Авторизация пользователя c некорректным паролем')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_login_user_email_wrong_password_response_status_code_401(self, create_user_and_delete_after):

        login_pass_name = create_user_and_delete_after

        payload = {
            "email": login_pass_name[0],
            "password": Constants.wrong_password
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/login", data=payload)


        assert response.status_code == 401 and response.json()['message'] == Constants.error_message_wrong_password_or_email


    @allure.title('Авторизация пользователя c некорректным email')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_login_user_wrong_email_password_response_status_code_401(self, create_user_and_delete_after):

        login_pass_name = create_user_and_delete_after

        payload = {
            "email": login_pass_name[1],
            "password": Constants.password
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/login", data=payload)


        assert response.status_code == 401 and response.json()['message'] == Constants.error_message_wrong_password_or_email