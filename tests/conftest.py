import pytest
import requests
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from helpers.helpers import Helpers
from data.data import Constants



@pytest.fixture
def create_user_and_delete_after():

    login_pass_name = Helpers.create_user()
    yield login_pass_name

    if login_pass_name:  
        payload = {
            "email": login_pass_name[0],
            "password": login_pass_name[1],
            "name": login_pass_name[2]
        }
        
        response = requests.post(f"{Constants.url_burger}/api/auth/login", data=payload)
        if response.status_code == 200:
            user_token = response.json()["accessToken"]
            requests.delete(f"{Constants.url_burger}/api/auth/user", headers={'Authorization': user_token})

@pytest.fixture
def delete_user():
    couriers_to_delete = []  
    
    def _register_user(email, password):
        couriers_to_delete.append((email, password))
    
    yield _register_user
    
    for email, password in couriers_to_delete:
        payload = {"email": email, "password": password}
        response = requests.post(f"{Constants.url_burger}/api/auth/login", data=payload)
        if response.status_code == 200:
            user_token = response.json()["accessToken"]
            requests.delete(f"{Constants.url_burger}/api/auth/user", headers={'Authorization': user_token})


@pytest.fixture
def create_user_order():

    login_pass_name = Helpers.create_user()
    if login_pass_name:  
        payload_order = {
            "ingredients": Constants.ingredients_hash
        }
        requests.post(f"{Constants.url_burger}/api/orders", data=payload_order, headers={'Authorization': login_pass_name[3]})

    yield login_pass_name

    requests.delete(f"{Constants.url_burger}/api/auth/user", headers={'Authorization': login_pass_name[3]})
