from django.shortcuts import render
from . import models


def news(request):
    return render(request, 'news.html', {'post_list' : models.Post.objects.order_by('-date')})


def new(request, id):
    return render(request, 'new.html', {'post' : models.Post.objects.get(id=id)})
