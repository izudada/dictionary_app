from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import requests


def index(request):
    Token = settings.OWL_TOKEN
    url = " https://owlbot.info/api/v4/dictionary/owl"
    response = requests.get(url, headers=Token)
    result = response.json()
    print(result)
    return HttpResponse("<h3> Done </h3>")