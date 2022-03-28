from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('photo/', views.photo, name = 'photo'),
    path('search/', views.search_results, name = 'search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)