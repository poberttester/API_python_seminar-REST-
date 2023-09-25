import pytest
import yaml

from REST_API import get

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)

def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert conf['id'] in lst_id


if __name__ == '__main__':
    pytest.main(['-v'])
