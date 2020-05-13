from django.urls import path
from . import views
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='feed'),
    path('post/', user_post, name = 'post'), 
    path('success/', PostListView.as_view(), name = 'success'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)