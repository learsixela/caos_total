import json
from collections import namedtuple

import requests
from django.shortcuts import render


def index(request):
    return render(request, 'index_cvega.html')


def show_pic(request):
    def json_to_nasa_picture(pic_dict):
        return namedtuple('X', pic_dict.keys())(*pic_dict.values())

    api_key = '3Iy7U4JE4iHJsK2zpbv3q0yZfdAMVKJEpmyk49gS'
    url = 'https://api.nasa.gov/planetary/apod?count=1&api_key={}'.format(api_key)

    response = requests.get(url)
    if response.status_code == 200:
        pic_json = response.text
        pic_json = pic_json[1:len(pic_json) - 2]
        pic = json.loads(pic_json, object_hook=json_to_nasa_picture)
        data = {
            'pic': pic,
        }
        return render(request, 'nasa_pic.html', data)

    return render(request, 'error_cvega.html')
