from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Document)
admin.site.register(DocumentHashSize)

# Register your models here.
