"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from index import views
from registration import views
from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    url('',include('index.urls')),
    url(r'^reg/',views.registration,name='registration'),
    url(r'^show/',include('show.urls')),
    url(r'^bonsai/',include('bonsai.urls')),
    url(r'^herbal/',include('herbal.urls')),
    url(r'formsubmission/',views.formsubmission,name='formsubmission'),
    url(r'adminlogin/',views.adminlogin,name='adminlogin'),
    url(r'adminsubmission/',views.adminsubmission,name='adminsubmission'),

]
