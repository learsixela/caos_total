import json
from collections import namedtuple

import requests
from django.shortcuts import render


def index(request):
    return render(request, 'index_cvega.html')


def show_pic(request):
    def json_to_nasa_picture(pic_dict):
        return namedtuple('json_to_nasa_picture', pic_dict.keys())(*pic_dict.values())

    api_key = open('api-key.txt', "r").read()
    url = 'https://api.nasa.gov/planetary/apod?count=1&api_key={}'.format(api_key)

    response = requests.get(url)
    if response.status_code == 200:
        pic_json = response.json()
        pic = json.loads(pic_json, object_hook=json_to_nasa_picture)
        data = {
            'pic': pic,
        }
        return render(request, 'nasa_pic.html', data)

    return render(request, 'error_cvega.html')
