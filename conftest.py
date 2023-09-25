import pytest
import yaml
import requests

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)


@pytest.fixture()
def get_token():
    response = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']
