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


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/',views.signout, name='/signout/'),
    path('homepage/', views.homepage, name='homepage'),
    path('patternpage/',views.patternpage,name='patternpage'),
    path('cases/',views.cases,name='cases'),
    path('View/',views.View,name='View'),
    path('source/',views.source,name='source'),
    path('Evidence/',views.evidence,name='Evidence'),
    path('contact/',views.contact,name='contact'),
    path('buildLaw/',views.buildLaw,name='buildLaw'),
    path('lawinput/',views.lawinput,name='lawinput'),
    path('caseinput/',views.caseinput,name='caseinput'),
    path('casefileupload/',views.casefileupload,name="casefileupload"),
    path('Setupnewcase/',views.Setupnewcase,name="/Setupnewcase/"),
    path('NewcaseSubmit/',views.NewcaseSubmit,name="/NewcaseSubmit/"),
    path('ShowCaseEvidence/',views.ShowCaseEvidence,name="/ShowCaseEvidence/"),
    path('SetupnewEvidence/',views.SetupnewEvidence,name="/SetupnewEvidence/"),
    path('NewEvidenceSubmit/',views.NewEvidenceSubmit,name="/NewEvidenceSubmit/"),
    path('SerchCase/',views.SerchCase,name="/SerchCase/"),
    path('sCaseName/',views.sCaseName,name="/sCaseName/"),
    path('SerchEvidence/',views.SerchEvidence,name="/SerchEvidence/"),
    path('sEvidenceName/',views.sEvidenceName,name="/sEvidenceName/"),
    path('ShowEvidenceSource/',views.ShowEvidenceSource,name='/ShowEvidenceSource/'),
    path('SetupnewSource/',views.SetupnewSource,name='/SetupnewSource/'),
    path('NewSourceSubmit/',views.NewSourceSubmit,name='/NewSourceSubmit/'),

    path('addEvidenceToOtherCase/',views.addEvidenceToOtherCase,name='/addEvidenceToOtherCase/'),
    path('addsourceToOtherEvidence/',views.addsourceToOtherEvidence,name='/addsourceToOtherEvidence/'),
    path('veifiyKey/',views.veifiyKey,name='/veifiyKey/'),
    path('veifiyKeyE/',views.veifiyKeyE,name='veifiyKeyE'),
    path('colNewSourceSubmit/',views.colNewSourceSubmit,name='/colNewSourceSubmit/'),
    path('colNewEvidenceSubmit/',views.colNewEvidenceSubmit,name='/colNewEvidenceSubmit/'),

    path('DeleteCase/',views.DeleteCase,name='/DeleteCase/'),
    path('DeleteEvidence/',views.DeleteEvidence,name='/DeleteEvidence/'),
    path('DeleteSource/',views.DeleteSource,name='/DeleteSource/'),
    path('AnalyzeMode/',views.AnalyzeMode,name='/AnalyzeMode/'),

    path('UpdateCase/',views.UpdateCase,name='/UpdateCase/'),
    path('UpdateCaseSubmit/',views.UpdateCaseSubmit,name='/UpdateCaseSubmit/'),
    path('UpdateEvidence/',views.UpdateEvidence,name='/UpdateEvidence/'),
    path('UpdateEvidenceSubmit/',views.UpdateEvidenceSubmit,name='/UpdateEvidenceSubmit/'),
    path('UpdateSource/',views.UpdateSource,name='/UpdateSource/'),
    path('UpdateSourceSubmit/',views.UpdateSourceSubmit,name='/UpdateSourceSubmit/'),

    path('Authorizationsumbit/',views.Authorizationsumbit,name='/Authorizationsumbit/'),
    path('authorsummit/',views.authorsummit,name='/authorsummit/'),
    path('warrantsumbit/',views.warrantsumbit,name='/warrantsumbit/'),
    path('wsummit/',views.wsummit,name='/wsummit/'),
    path('justificationsumbit/',views.justificationsumbit,name='/justificationsumbit/'),
    path('jsummit/',views.jsummit,name='/jsummit/'),

    path('download/',views.download,name='/download/'),
    path('downloadw/',views.downloadw,name='/downloadw/'),
    path('downloadj/',views.downloadj,name='/downloadj/'),
    path('downloada/',views.downloada,name='/downloada/'),
    path('clearW/',views.clearW,name='/clearW/'),
    path('clearAu/',views.clearAu,name='/clearAu/'),
    path('clearJ/',views.clearJ,name='/clearJ/'),
]
