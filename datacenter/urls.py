"""datacenter URL Configuration

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
from mysite.views import index, show, myindex

urlpatterns = [
<<<<<<< HEAD
	path('show/<int:id>/', show),
=======
    path('show/<int:id>/', show),
>>>>>>> d4ac108282bfc62c2ac84ff0bd578a94774505f1
    path('index/', index),
    path('myindex/', myindex),
    path('myindex/<str:city>/', myindex),
    path('admin/', admin.site.urls),
    path('', myindex),
]
