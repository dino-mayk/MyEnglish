from django.urls import path

from users import views

app_name = 'translator'

urlpatterns = [
    path('translator/', views.translator, name='translator'),
]
