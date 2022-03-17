from django.shortcuts import render

# Create your views here.
from django.utils import translation

if 'language' in request.GET and request.GET['language']:
    language = request.GET['language']
    if language in ['fr','en']:
        if language == 'fr': 
            translation.activate(language)
        if language == 'en': 
            translation.activate(language)

text = gettext("text")

err_msg = gettext("Oups somehting went wrong")

