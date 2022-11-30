import requests
import os


def make_new_folder(token, path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'OAuth {token}'
    }
    params = {
        'path' : path
    }
    params_for_del = {
    'path' : path,
    'permanently':'true'
    }
    deletion = requests.delete(url = url, headers=headers, params=params_for_del)
    response = requests.put(url = url, headers=headers, params=params)
    return response
