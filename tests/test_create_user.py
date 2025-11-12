import requests
import allure
import sys
from datetime import datetime
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.data import Constants

class TestCreateUser:


    @allure.title('Создаю пользователя')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_create_user_email_name_password_response_status_code_200(self, delete_user):

        unique_email = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}@mail.ru"
        unique_name = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}"

        payload = {
            "email": unique_email,
            "password": Constants.password,
            "name": unique_name,
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/register", data=payload)


        assert response.status_code == 200 and response.json()['user'] == {"email": unique_email, "name": unique_name}

        delete_user(unique_email, Constants.password)


    @allure.title('Создаю пользователя, который уже существует')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_create_existing_user_email_login_password_response_status_code_403(self, create_user_and_delete_after):

        login_pass = create_user_and_delete_after


        payload = {
            "email": login_pass[0],
            "password": Constants.password,
            "name": login_pass[2],
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/register", data=payload)


        assert response.status_code == 403 and response.json()['success'] == False and response.json()['message'] == Constants.error_message_user_exist

    @allure.title('Создаю пользователя с незаполненым email')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_create_user_name_password_response_status_code_403(self):

        unique_name = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}"

        payload = {
            "password": Constants.password,
            "name": unique_name
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/register", data=payload)


        assert response.status_code == 403 and response.json()['success'] == False and response.json()['message'] == Constants.error_message_required_fields


    @allure.title('Создаю пользователя с незаполненым name')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_create_user_email_password_response_status_code_403(self):

        unique_email = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}@mail.ru"

        payload = {
            "email": unique_email,
            "password": Constants.password,
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/register", data=payload)


        assert response.status_code == 403 and response.json()['success'] == False and response.json()['message'] == Constants.error_message_required_fields


    @allure.title('Создаю пользователя с незаполненым password')
    @allure.description('Отправляем POST запрос, проверяем тело и статус ответа')
    def test_create_user_email_named_response_status_code_403(self):

        unique_email = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}@mail.ru"
        unique_name = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}"

        payload = {
            "email": unique_email,
            "name": unique_name
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/register", data=payload)


        assert response.status_code == 403 and response.json()['success'] == False and response.json()['message'] == Constants.error_message_required_fields