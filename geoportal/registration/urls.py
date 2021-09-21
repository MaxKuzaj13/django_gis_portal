from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('login', views.login, name='login'),
    #
    # path('logout', views.logout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('', include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)