from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('homepage.urls'), name='homepage'),
    path('auth/', include('users.urls'), name='users'),
    path('words/', include('words.urls'), name='words'),
    path('translator/', include('translator.urls'), name='translator'),

    path('grappelli/', include('grappelli.urls')),
]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns += [
        path(
            '__debug__/',
            include(
                debug_toolbar.urls,
            ),
        ),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
