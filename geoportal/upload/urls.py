from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Main.as_view(), name='home'),
    # path('upload', views.upload, name='upload'),
    path('upload', views.UploadView.as_view(), name='upload'),
    path('list_view', views.ListView.as_view(), name='list_view'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),
         name="login"),
    path('detail_view/<slug:pk>/', views.DetailView.as_view(), name='detail_view'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)