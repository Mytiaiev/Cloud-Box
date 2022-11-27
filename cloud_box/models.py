from django.db import models
import hashlib
import os
# Create your models here.


class User(models.Model):
    class Role(models.TextChoices):
        GUEST = 'GUEST', 'Guest'
        MODERATOR = 'MODERATOR', 'Moderator'
    
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    
    
    
class Document(models.Model): 
    # def hash_file(document, block_size=65536):
    #     hasher = hashlib.md5()
    #     for buf in iter(partial(document.read, block_size), b''):
    #         hasher.update(buf)
    #     return hasher.hexdigest()

    # def hash_upload(instance, filename):
    #     instance.document.open()
    #     contents = instance.document.read()
    #     fname, ext = os.path.splitext(filename)
    #     return "{0}_{1}{2}".format(fname, hash_file(document), ext)
        
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=55)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id},{self.file_name},{self.description}"


    