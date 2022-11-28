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
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=55)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id},{self.file_name},{self.description}"

    def md5(file:object) -> str:
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
        

class DocumentHashSize(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    hash_size = models.CharField(max_length=255)
    
  
            
    
    