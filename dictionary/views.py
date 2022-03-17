from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

import requests


def index(request):
    
    if request.method == "POST":
        word = request.POST.get('word')
        context = {}
        Token = settings.OWL_TOKEN

        #   Catching ConnectionError while connecting to owl API
        try:
            url = f"https://owlbot.info/api/v4/dictionary/{word}"
        except Exception as e:
            messages.success(request, "There is an issue with your internet connection")
            return render(request, "index.html")

        response = requests.get(url, headers={"Authorization": 'Token ' + Token})
        result = response.json()

        context['word'] = word
        context['pronunciation'] = result['pronunciation']
        context["type"] = []
        context["url"] = []
        context["definition"] = []
        context["example"] = []

        for data in result['definitions']:
            context["url"].append(data['image_url'])
            context["type"].append(data['type'])
            context["definition"].append(data['definition'])
            context["example"].append(data['example'])

        return render(request, "index.html", context)
    else:
        return render(request, "index.html")
