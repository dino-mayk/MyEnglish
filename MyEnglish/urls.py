from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls'), name='homepage'),
    path('auth/', include('users.urls'), name='users'),
    path('words/', include('words.urls'), name='words'),
]
