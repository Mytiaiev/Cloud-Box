from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.views.static import serve

urlpatterns = [
    path('', index, name='home'),
    path('view', cloud_view, name='view'),
    path('upload', model_form_upload, name='uplaod'),
    path('login', login_request, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_request, name='register'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
