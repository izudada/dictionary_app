from django.shortcuts import render
from django.conf import settings
from django.contrib import messages

import requests


def index(request):
    
    if request.method == "POST":
        word = request.POST.get('word')

        #   Chec if word is valid
        if len(word) < 1:
            messages.error(request, "Please input a valid word")
            return render(request, "index.html")

        context = {}
        Token = settings.OWL_TOKEN
        url = f"https://owlbot.info/api/v4/dictionary/{word}"

        #   Handling request errors
        try:
            response = requests.get(url, headers={"Authorization": 'Token ' + Token})
        except requests.exceptions.Timeout:
            messages.error(request, "You have made too many failed attempts")
            return render(request, "index.html")
        except requests.exceptions.ConnectionError:
            messages.error(request, "There is an issue with your internet connection, please reconnect.")
            return render(request, "index.html")
        except requests.exceptions.RequestException:
            messages.error(request, f"Failed to get the word {word}, please try again")
            return render(request, "index.html")

        result = response.json()
        
        #   Check if a valid response was returned
        if type(result) == list:
            messages.error(request, f"The word \"{word}\" wasn't found")
            return render(request, "index.html")

        return render(request, "index.html", result)
    else:
        return render(request, "index.html")
