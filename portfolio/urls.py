"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #import the settings file
from django.conf.urls.static import static #import the static media
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'), #go to jobs apps, views file to home function
    path('blogs/', include('blog.urls')),#where blog in blog.url is the name of your app and include is forwarding to urls in blog
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#simply directing where the file program will check for the details upon clicking
