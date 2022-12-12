from django.urls import path
from .views import index, cloud_view, model_form_upload_1
from .views import login_request, logout_user, register_request, download_view


urlpatterns = [
    path('', index, name='home'),
    path('view', cloud_view, name='view'),
    path('upload', model_form_upload_1, name='uplaod'),
    path('login', login_request, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_request, name='register'),
    path('<int:pk>/', download_view, name='download'),

]
