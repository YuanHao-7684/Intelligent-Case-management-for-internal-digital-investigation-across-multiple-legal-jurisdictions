import os

from django.db.models import QuerySet
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from mysite import models
import docx
import re
from docx import Document
from chardet import detect
# Create your views here.
from django.shortcuts import HttpResponse
from mysite.forms import UploadFileForm
from mysite.models import User
import numpy as np
messagelist = ""
currentuser = ""

open_country=['EEA', 'United Kingdom', 'UK', 'Kingdom', 'India', 'Hong Kong', 'Hong','Kong','United States', 'US', 'States']
neutral_country=['Russian', 'Colombia', 'Japan', 'Ukraine', 'South Korea', 'Korea', 'Nigeria', 'Argentina']
strict_country=['China', 'Turkey', 'Brazil', 'Peru', 'Philippines', 'Thailand', 'Malaysia', 'Singapore', 'Egypt', 'South Africa', 'Africa', 'Morocco', 'Canada', 'Mexico']
#index page
def index(request):
    initialization=""
    return render(request, 'index.html',{'user':initialization})

#self-builde function
def buildLaw(request):
    if request.method == "POST":
        national = request.POST.get("national", None)
        nameoflaw = request.POST.get("nameoflaw", None)
        KeyPoints = request.POST.get("KeyPoints", None)
        mode = request.POST.get("mode",None)
        relCountry= request.POST.get("rCountry",None)
        #models.LawIno.objects.filter(country="Mexico").delete()
        models.LawIno.objects.create(country=national,LawName=nameoflaw,KeyPoint=KeyPoints,restrictedMode=mode,AgreementCountry=relCountry)
        lawlist = models.LawIno.objects.all()
        i=1
        for l in lawlist:
            print(str(i)+"---"+l.country+"---"+"\n","<<"+l.LawName+">>"+"\n",l.KeyPoint+"\n",l.restrictedMode+"\n",l.AgreementCountry)
            i += 1
    return render(request,"lawinput.html")
def lawinput(request):
    return render(request,"lawinput.html")




# function
def signup(request):
    if request.method == "POST":
        username = request.POST.get("newname", None)
        password = request.POST.get("newpassword", None)
        email = request.POST.get("newemail", None)
        userlist = models.User.objects.all()
        #
        for u in userlist:
            print(u.user,u.password,u.email)
        flag = models.User.objects.get_or_create(user=username, email=email, password=password)
        if flag[1] == False :
            messagelist="user already exist,please login"
            return render(request, 'index.html', {'message': messagelist})
        else:
            messagelist = "Account created successfully"
            Nuser=username
            Npassword=password
            return render(request, 'index.html', {'message': messagelist,'user':Nuser,'password':Npassword})


def signin(request):
    if request.method == "POST":
        userName = request.POST.get("username", None)
        passWord = request.POST.get("password", None)
        #print(userName,passWord)
        try:
          nameflag = models.User.objects.get(user=userName)
        except ObjectDoesNotExist:
            messagelist="user dose not exist"
            return render(request, 'index.html',{'message':messagelist})
        if nameflag.password != passWord:
            messagelist="wrong password"
            initialization = ""
            return render(request, 'index.html',{'message':messagelist,'user':initialization})
        request.session["username"]=userName
        currentuser=request.session.get("username")
        return render(request, 'homepage.html', {'user': currentuser})

def caseinput(request):
    if request.method == "POST":
        casetext=request.POST.get("casecontent",None)
        userName=request.session.get("username")
        currentuser = userName
        title="InputCase-"+casetext[0:5]
        print(title)
        flag = models.Cases.objects.get_or_create(caseUser=userName,caseContent=casetext,casetitle=title)
        if flag[1] == True:
            return render(request, 'casepage.html', {'user': currentuser})
    return render(request, 'homepage.html', {'user': currentuser})


def casefileupload(request):
    if request.method == "POST":
           uploadfile_list=request.FILES.getlist('files')
           for file in uploadfile_list:
              filetype=os.path.splitext(file.name)[-1][1:]
              #docx file
              if filetype == "docx":
                 totaltext=""
                 docfile=docx.Document(file)
                 for paragraph in docfile.paragraphs:
                     totaltext+=paragraph.text+" "
                 userName = request.session.get("username")
                 currentuser = userName
                 models.Cases.objects.create(caseUser=userName, caseContent=totaltext,casetitle=file.name)
    return render(request, 'casepage.html', {'user': currentuser})


def homepage(request):
    currentuser = request.session.get("username")
    return render(request, 'homepage.html', {'user': currentuser})


def patternpage(request):
    currentuser = request.session.get("username")
    return render(request, 'list pages.html', {'user': currentuser})


# case management
def cases(request):
    currentuser = request.session.get("username")
    return render(request, 'casepage.html', {'user': currentuser})
def Setupnewcase(request):
    currentuser = request.session.get("username")
    return render(request, 'newcase.html', {'user': currentuser})


def NewcaseSubmit(request):
    if request.method == "POST":
        caseName = request.POST.get("Name", None)
        userinputID = request.POST.get("ID", None)
        caseScope = request.POST.getlist("area")
        InvName = request.POST.get("InvName", None)
        InvEmail = request.POST.get("InvEmail", None)
        caseSynopsis = request.POST.get("synopsis", None)
        caseType = request.POST.getlist("Type")
        currentuser = request.session.get("username")
        models.SetUpCases.objects.create(UserInputId=userinputID,
                                         caseName=caseName,
                                         caseScope=caseScope,
                                         caseInv=InvName,
                                         caseInvEmail=InvEmail,
                                         caseType=caseType,
                                         casesynopsis=caseSynopsis,
                                         caseUserName=currentuser)
    # case process
    currentuser = request.session.get("username")
    userCase_list = models.SetUpCases.objects.filter(caseUserName=currentuser)
    return render(request, 'caseView.html',{'user': currentuser, 'caselist': userCase_list, 'listlen': len(userCase_list)})


#case preview
def View(request):
    #country process
    #country_list=models.LawIno.objects.all()
    #for c in range(len(country_list)):
    #    if country_list[c].restrictedMode == "open":
    #        open_country.append(country_list[c].country)
    #    if country_list[c].restrictedMode == "neutral":
    #       neutral_country.append(country_list[c].country)
    #    if country_list[c].restrictedMode == "strict":
    #        strict_country.append(country_list[c].country)
    #case process
    currentuser = request.session.get("username")
    userCase_list = models.SetUpCases.objects.filter(caseUserName=currentuser)
    return render(request, 'caseView.html',
                  {'user': currentuser, 'caselist': userCase_list, 'listlen': len(userCase_list)})
def Log(request):
    currentuser = request.session.get("username")
    return render(request, 'caseLog.html', {'user': currentuser})


def Report(request):
    currentuser = request.session.get("username")
    return render(request, 'caseReport.html', {'user': currentuser})


# contact
def contact(request):
    currentuser =request.session.get("username")
    return render(request, 'contact.html', {'user': currentuser})
