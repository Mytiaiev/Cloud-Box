from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .forms.files import DocumentForm
from .forms.user import CloudUser
from .models import Document
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpRequest
import os
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """ plain routing to render HOME PAGE"""
    return render(request=request,
                  template_name='base.html')


def cloud_view(request: HttpRequest) -> HttpResponse:
    """ plain routing to render FILE VIEW PAGE"""
    documents = Document.objects.order_by('-id')
    return render(request,
                  template_name='cloud_view.html',
                  context={'documents': documents})


def get_file_size(files: object) -> bool:
    """Handler for check to size of object"""
    limit = 10*1048576
    if files.size < limit:
        return True


def model_form_upload_1(request: HttpRequest) -> HttpResponse:
    ''' view handling this form will receive the file data in
:attr:`request.FILES <django.http.HttpRequest.FILES>`'''
    if request.method == 'POST':
        upload = request.FILES['file']
        hash_tuple = ()
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(upload.size)
            if get_file_size(upload):
                hash = Document.get_hash(upload)
                hash_list = [x for x in Document.objects.all().values_list('hash_size')]
                hash_tuple += (hash,)
                if hash_tuple not in hash_list:
                    Document.objects.create(
                        file_path=upload.read,
                        hash_size=hash)
                else:
                    return redirect("view")
            return HttpResponseBadRequest("file bigger tha 300mb")
        else:
            return HttpResponseBadRequest("Form invalid")
    else:
        form = DocumentForm()
        return render(
            request=request,
            template_name='model_form_upload.html',
            context={'form': form})
        return render(request, 'model_form_upload.html')
    return render(request, 'model_form_upload.html')


def register_request(request: HttpRequest) -> HttpResponse:
    """ plain routing to render register page to user models"""
    if request.method == "POST":
        form = CloudUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request,
                       "Unsuccessful registration. Invalid information.")
    form = CloudUser()
    return render(
        request=request,
        template_name="register.html",
        context={"register_form": form})


def is_banned(user: object) -> bool:
    """foo will chek to is user exis to  banned group

    Args:
        user (object): UserCreateForm object

    Returns:
        bool: True or False
    """
    return user.groups.filter(name='banned').exists()


def login_request(request: HttpRequest) -> HttpResponse:
    """foo to login in session
    be able to registred users

    Args:
        request (HttpRequest):

    Raises:
        PermissionDenied: for no registred users or banned

    Returns:
        HttpResponse:
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if is_banned(user):
                raise PermissionDenied()
            else:
                if user is not None:
                    login(request, user)
                    return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
            request=request,
            template_name="login.html",
            context={"login_form": form})


def logout_user(request: HttpRequest) -> HttpResponse:
    """ plain routing to end session for user models"""
    logout(request)
    return redirect('login')


def download(request: HttpRequest, path: str) -> HttpResponse:
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(),
                                    content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise PermissionDenied()
