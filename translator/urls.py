from django.urls import path

from translator import views

app_name = 'translator'

urlpatterns = [
    path('', views.index, name='index'),
]
