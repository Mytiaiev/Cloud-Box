from django.contrib import admin
from .models import Document, DocumentHashSize


admin.site.register(Document)
admin.site.register(DocumentHashSize)

# Register your models here.
