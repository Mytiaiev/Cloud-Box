from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import DocumentForm
from .models import Document, DocumentHashSize
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.
def index(request):
    template_name = 'base.html'
    return render(request, template_name)

def cloud_view(request):
    documents = Document.objects.all()
    template_name = 'cloud_view.html'
    return render(request, template_name, {'documents':documents})

def model_form_upload(request):
    template_name = 'model_form_upload.html'
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
    return render(request, template_name, {
        'form': form
    })