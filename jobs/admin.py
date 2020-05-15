from django.contrib import admin

# Register your models here.
from .models import Job
#import model you want to show
admin.site.register(Job)
#register model job at the admin site
