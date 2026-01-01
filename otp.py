import re
import time
import names
import requests


MAIL_API = "https://api.mail.tm"


def generate_email(domain:str) -> str:
    name = names.get_full_name()
    name = ''.join(name.split()).lower()

    curr_time = time.perf_counter_ns()

    return f'{name}{curr_time}@{domain}'


def create_account() -> dict:
    domain = requests.get(f"{MAIL_API}/domains").json()
    domain = domain["hydra:member"][0]['domain']

    new_email = generate_email(domain)

    credential = {
            "address": new_email,
            "password": "P@ssword123"
    }

    account = requests.post(f"{MAIL_API}/accounts", json=credential).json()
    token = requests.post(f"{MAIL_API}/token", json=credential).json()

    return {
        "email": new_email,
        "token": token['token']
    }


def get_otp(token:str) -> None | str:
    headers = {"Authorization": f"Bearer {token}"}

    for _ in range(10):
        messages = requests.get(f"{MAIL_API}/messages", headers=headers).json()

        if messages["hydra:member"]:
            recent_message = messages["hydra:member"][0]
            message = recent_message['intro']

            return  re.search(r"\d+", message).group()