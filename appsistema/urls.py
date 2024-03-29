"""appsistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import reverse

from django.urls import include, path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.consumer.urls')),
    path('lesson/', include('apps.lesson.urls')),
    path('teacherbot/', include('apps.teacherbot.urls')),
    path('evaluation/', include('apps.evaluation.urls')),

    #Urls password reset     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
