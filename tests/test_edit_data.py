import requests
import allure
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from data.data import Constants

class TestEditUser:

    @allure.title('Изменение email авторизованного пользователя')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_edit_user_email_response_status_code_200(self, create_user_and_delete_after):

        login_pass_name_token = create_user_and_delete_after
        unique_email = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}@mail.ru"
        payload = {
            "email": unique_email
        }
        response = requests.patch(f"{Constants.url_burger}/api/auth/user", data=payload, headers={'Authorization': login_pass_name_token[3]})


        assert response.status_code == 200 and response.json()['success'] == True and response.json()['user'] == {"email": unique_email, "name": login_pass_name_token[2]}
    
    @allure.title('Изменение имени авторизованного пользователя')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_edit_user_name_response_status_code_200(self, create_user_and_delete_after):

        login_pass_name_token = create_user_and_delete_after

        payload = {
            "name": Constants.new_name
        }
        response = requests.patch(f"{Constants.url_burger}/api/auth/user", data=payload, headers={'Authorization': login_pass_name_token[3]})


        assert response.status_code == 200 and response.json()['success'] == True and response.json()['user'] == {"email": login_pass_name_token[0], "name": Constants.new_name}
    
    @allure.title('Изменение пароля авторизованного пользователя')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_edit_user_password_response_status_code_200(self, create_user_and_delete_after):

        login_pass_name_token = create_user_and_delete_after

        payload = {
            "email": login_pass_name_token[0],
            "password": Constants.new_password
        }
        response = requests.patch(f"{Constants.url_burger}/api/auth/user", data=payload, headers={'Authorization': login_pass_name_token[3]})
        response_login = requests.post(f"{Constants.url_burger}/api/auth/login", data=payload)

        assert response.status_code == 200 and response_login.json()['success'] == True


    @allure.title('Изменение данных не авторизованного пользователя')
    @allure.description('Отправляем PATCH запрос, проверяем тело и статус ответа')
    def test_edit_unauthorized_user_data_response_status_code_401(self, create_user_and_delete_after):

        login_name_pass = create_user_and_delete_after

        payload = {
            "email": login_name_pass[0],
            "password": Constants.password,
            "name": login_name_pass[2],
        }
        response = requests.patch(f"{Constants.url_burger}/api/auth/user", data=payload)

        assert response.status_code == 401 and response.json()['message'] == Constants.error_message_not_authorised