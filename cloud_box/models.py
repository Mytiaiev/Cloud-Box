from django.db import models
import hashlib
# Create your models here.


class Document(models.Model):
    """Class for uplaoded files. colect file and description
    working with analog form
    """
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=55)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id},{self.file_name},{self.description}"

    def get_hash(file: object) -> str:
        md = hashlib.md5()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md.update(chunk)
        return md.hexdigest()


class DocumentHashSize(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    hash_size = models.CharField(max_length=255)