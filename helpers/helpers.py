import requests
from datetime import datetime
from data.data import Constants
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class Helpers:

    def create_user():

        unique_email = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}@mail.ru"
        unique_name = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}"
        password = Constants.password

        payload = {
            "email": unique_email,
            "password": password,
            "name": unique_name,
        }
        response = requests.post(f"{Constants.url_burger}/api/auth/register", data=payload)
        
        if response.status_code == 200:
            return [response.json()['user']['email'], password, response.json()['user']['name'], response.json()['accessToken']]
        