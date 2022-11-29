from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import DocumentForm, CloudUser
from .models import Document, DocumentHashSize
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index(request):
    return render(request=request, template_name='base.html')

def cloud_view(request):
    documents = Document.objects.all()
    return render(request,
                  template_name='cloud_view.html',
                  context={'documents':documents})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        files = request.FILES['myfile']
        if files.size > 300000000:
            return HttpResponseBadRequest("file to big, try upload file less than 300MB")
        else:
            hash = Document.hash_md5(files)
            has_list = DocumentHashSize.objects.all(hash_size)
            if hash not in has_list:
               DocumentHashSize.objects.create(hash_size=has)
               form.save()
               
                
    else:
        form = DocumentForm()
    return render(request=request,
                  template_name='model_form_upload.html',
                  context={'form': form})
    
    
def register_request(request):
	if request.method == "POST":
		form = CloudUser(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CloudUser()
	return render (request=request,
                template_name="register.html",
                context={"register_form":form})
 
 
 
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request,
               template_name="login.html",
               context={"login_form":form})