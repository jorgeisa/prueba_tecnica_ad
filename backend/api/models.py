from django.db import models

# Create your models here.
class Information(models.Model):
    question=models.CharField(max_length=3000)
    answer=models.CharField(max_length=3000)

