from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.home, name='home'),
#
# ]
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('upload', views.upload, name='upload'),
    path('upload', views.UploadView.as_view(), name='upload'),
    path('list_view', views.ListView.as_view(), name='list_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)