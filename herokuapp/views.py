from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.now()
    html = "<html><body> Test deploymentu <hr> Aktualna godzina %s.</body></html>" % now
    return HttpResponse(html)
