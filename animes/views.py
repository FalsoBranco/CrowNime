from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Anime

# Create your views here.


def index(request):

    animes = Anime.objects.select_related("title").all()[:21]

    return render(request, "animes/index.html", {"animes_featured": animes})
