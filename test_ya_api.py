import pytest, os, requests
from yandex_api import make_new_folder


def test_make_new_folder():
    result = make_new_folder(os.getenv('token'), '/test').status_code
    etalon = 201
    assert result==etalon
def test_make_new_folder_1():
    folder = requests.get(url='https://cloud-api.yandex.net/v1/disk/resources',
                          headers={
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {os.getenv("token")}'},
                          params={'path':'/test'})
    assert folder.status_code==200

def test_make_new_folder_2():
    folder = requests.get(url='https://cloud-api.yandex.net/v1/disk/resources',
                          headers={
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {os.getenv("token")}'},
                          params={'path':'/tes'})
    assert folder.status_code==200



