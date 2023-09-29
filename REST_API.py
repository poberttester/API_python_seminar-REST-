# Написать тест с использованием pytest и requests, в котором:
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
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

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)



def get_token() -> str:
    response = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']


def get(token: str) -> str:
    response = requests.get(conf["url_posts"],
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})
    return response.json()



def create_post(url: str, token: str, body: dict) -> int:
    response = requests.post(url=url, headers={"X-Auth-Token": token}, data=body)
    return response.status_code


# Задание Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется
# его наличие на сервере по полю «описание».

# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title,
# description, content.


if __name__ == '__main__':
    #create_post(conf['url_posts'], get_token(), DATA)
    t= get_token()
    temp=get_post(conf['url_posts'], t, {'description': 'Description'})
    print(temp)
    print(t)
