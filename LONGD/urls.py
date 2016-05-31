"""LONGD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from blog.views import *
urlpatterns = [
    url(r'^$',blog),
    url(r'^api_list.html',api_list),
    url(r'^delapi/(\d+)/',delete_api),
    url(r'^delcase/(\d+)/',delete_case),
    url(r'^addapi.html',addapi),
    url(r'^addcase.html',addcase),
    url(r'^api_case.html',api_case),
    url(r'^project.html',addproject),
    url(r'^project_list.html',project_list),
    url(r'^result/(\d+)/',goproject),
    url(r'^result.html',result),

    #url(r'^api/',api),
    url(r'^admin/', admin.site.urls),
]
