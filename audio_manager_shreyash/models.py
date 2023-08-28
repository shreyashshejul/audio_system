from django.db import models

# Create your models here.
from django.db import models

class UploadedAudio(models.Model):
    user = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    extension = models.CharField(max_length=10)
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    file_size = models.BigIntegerField()

    def __str__(self):
        return self.file.name
