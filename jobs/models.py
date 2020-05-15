from django.db import models

# Create your models/class here.
class Job(models.Model):
#allows creation of new class, gives background stuf that allows this object to be saved in the database
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
