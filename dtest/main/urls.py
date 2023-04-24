from django.urls import path
from . import views


urlpatterns = [
    path('', views.news),
    path('<int:id>', views.new, name='new')
]