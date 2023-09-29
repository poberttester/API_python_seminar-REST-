import pytest
import yaml

from REST_API import get
from REST_API import get_post
from REST_API import create_post

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)
DATA = {'title': 'Title', 'description': 'Description111', 'content': 'Сontent'}

def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert conf['id'] in lst_id

def test_step2(get_token):
    create_post(conf["url_posts"], get_token, DATA)
    result = get_post(conf['url_posts'], get_token, DATA)
    body = result['data']
    list_description = [el['description'] for el in body]
    assert DATA['description'] in list_description


if __name__ == '__main__':
    pytest.main(['-v'])
