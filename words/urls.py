from django.urls import path

from words import views

app_name = 'words'

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
