from django.urls import path, re_path
from django.conf import settings
from .views import index, cloud_view, model_form_upload_1
from .views import login_request, logout_user, register_request
from django.views.static import serve


urlpatterns = [
    path('', index, name='home'),
    path('view', cloud_view, name='view'),
    path('upload', model_form_upload_1, name='uplaod'),
    path('login', login_request, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_request, name='register'),
    re_path(r'^download/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})

]