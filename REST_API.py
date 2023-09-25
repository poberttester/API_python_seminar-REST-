# Написать тест с использованием pytest и requests, в котором:#
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml#
# conftest.py содержит фикстуру авторизации по адресу
# https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password" и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя,
# для этого выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером,
# содержащим токен авторизации в параметре "X-Auth-Token".
# Для отображения постов другого пользователя передается "owner": "notMe".

from getpass import getpass

import requests as requests
import yaml

with open('config.yaml', 'r')as f:
    conf = yaml.safe_load(f)


def get_token():
    response = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']

def get(token: str):
    response = requests.get(conf["url_posts"],
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})
    return response.json()


if __name__ == '__main__':
    temp = get_token()
    print(get(temp))
