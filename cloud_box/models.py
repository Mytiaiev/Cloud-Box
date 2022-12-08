from django.db import models
import hashlib
# Create your models here.


class Document(models.Model):
    """Class for uplaoded files. colect file and description
    working with analog form
    """
    id = models.AutoField(primary_key=True)
    file_path = models.CharField(max_length=255)
    hash_size = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id},{self.file_path},{self.hash_size}"

    def get_hash(file: object) -> str:
        md = hashlib.md5()
        # with open(file, "rb") as f:
        for chunk in iter(lambda: file.read(4096), b""):
            md.update(chunk)
        return md.hexdigest()
