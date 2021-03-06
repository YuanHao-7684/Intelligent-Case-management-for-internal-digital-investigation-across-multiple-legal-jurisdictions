"""mywbsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from mysite import views
from mysite.views import index
from mysite.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('homepage/', views.homepage, name='homepage'),
    path('patternpage/',views.patternpage,name='patternpage'),
    path('cases/',views.cases,name='cases'),
    path('View/',views.View,name='View'),
    path('Report/',views.Report,name='Report'),
    path('Log/',views.Log,name='Log'),
    path('contact/',views.contact,name='contact'),
    path('buildLaw/',views.buildLaw,name='buildLaw'),
    path('lawinput/',views.lawinput,name='lawinput'),
    path('caseinput/',views.caseinput,name='caseinput'),
    path('casefileupload/',views.casefileupload,name="casefileupload"),
]
