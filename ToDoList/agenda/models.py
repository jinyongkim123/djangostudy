from django.db import models

# Create your models here.
class ToDos(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    

