"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from Hello.settings import STATIC_ROOT

admin.site.site_header = "CODEASSET ADMIN PAGE"
admin.site.index_title = "Welcome to CODEASSET"
admin.site.site_title = "CODEASSET"
from Home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('django',views.django,name="django"),
    path('feedback',views.feedback,name="feedback"),
    path('flask',views.flask,name="flask"),
    path('html',views.html,name="html"),
    path('php',views.php,name="php"),
    path('python',views.python,name="python"),
    path('tutorials',views.tutorials,name="tutorials"),
    path('web',views.web,name="web"),
    path('jobs',views.jobs,name="jobs"),
    path('front',views.front,name="front"),
    path('fs',views.fs,name="fs"),
    path('Ux',views.Ux,name="Ux"),
    path('technical',views.technical,name="technical"),
    path('engineering',views.engineering,name="engineering"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)