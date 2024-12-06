import data
import configuration
import requests


# Функция для создания нового набора пользователя
def post_new_client_kit (kit_body, auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KITS,
                         headers=auth_token,
                         json=kit_body
                         )
# В переменную response сохраняется результат
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)  # а здесь заголовки


response = post_new_user(data.user_body);
print(response.status_code)


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_ids,
                             headers=data.headers)
response = post_new_client_kit(data.kit_body, data.auth_token)
print(response.status_code)

