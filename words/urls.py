from django.urls import path

from words import views

app_name = 'words'

urlpatterns = [
    path('', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
