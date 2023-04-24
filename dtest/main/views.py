from django.shortcuts import render
from . import models

def news(request):
    return render(request, 'news.html', {'post_list' : models.Post.objects.all()})
