"""worker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name = 'hello'),
    url(r'^linuxtest1/', views.get_linux_test_1, name = 'linux_test_1'),
    url(r'^linuxtest1statistics/', views.get_linux_test_1_statistics, name = 'linux_test_1_statistics'),
]
