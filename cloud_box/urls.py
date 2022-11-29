from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('view', cloud_view, name='view'),
    path('upload', model_form_upload, name='uplaod'),
    path('login', login_request, name='login'),
    path('register', register_request, name='register'),

    
]
