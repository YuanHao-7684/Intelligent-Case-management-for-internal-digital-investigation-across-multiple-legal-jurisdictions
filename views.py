import os

from django.db.models import QuerySet
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from mysite import models
import docx
from docx import Document
from chardet import detect
# Create your views here.
from django.shortcuts import HttpResponse
from mysite.forms import UploadFileForm
from mysite.models import User

messagelist = ""
currentuser = ""

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
            return render(request, 'index.html',{'message':messagelist})
        request.session["username"]=userName
        currentuser=request.session.get("username")
        return render(request, 'homepage.html', {'user': currentuser})

def caseinput(request):
    if request.method == "POST":
        casetext=request.POST.get("casecontent",None)
        userName=request.session.get("username")
        currentuser = userName
        flag = models.Cases.objects.get_or_create(caseUser=userName,caseContent=casetext)
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
                 models.Cases.objects.create(caseUser=userName, caseContent=totaltext)
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


def View(request):
    currentuser = request.session.get("username")
    return render(request, 'caseView.html', {'user': currentuser})


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
