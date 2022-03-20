from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

import requests


def index(request):
    
    if request.method == "POST":
        word = request.POST.get('word')
        context = {}
        Token = settings.OWL_TOKEN
        url = f"https://owlbot.info/api/v4/dictionary/{word}"

        try:
            response = requests.get(url, headers={"Authorization": 'Token ' + Token})
        except requests.exceptions.Timeout:
            messages.success(request, "You have made too many failed attempts")
            return render(request, "index.html")
        except requests.exceptions.ConnectionError:
            messages.success(request, "There is an issue with your internet connection, please reconnect.")
            return render(request, "index.html")
        except requests.exceptions.RequestException:
            messages.success(request, f"Failed to get the word {word}, please try again")
            return render(request, "index.html")

        result = response.json()

        return render(request, "index.html", result)
    else:
        return render(request, "index.html")
