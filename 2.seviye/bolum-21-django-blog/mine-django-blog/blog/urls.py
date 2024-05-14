"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django import urls
from django.conf.urls import handler500
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static

from article import views as a_w
from . import views

handler500 = views.handler404
handler404 = views.handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',a_w.index,name="index"),
    path('about/',a_w.about,name="about"),
    path('articles/',include("article.urls")),
    path('user/',include("user.urls")),
    path('404/',handler404,name="404")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

