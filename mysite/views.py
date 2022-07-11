from django.db.models import QuerySet
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from mysite import models
# Create your views here.
from django.shortcuts import HttpResponse

from mysite.models import User

messagelist = ""
currentuser = ""


def index(request):
    return render(request, 'index.html')


# function
def signup(request):
    if request.method == "POST":
        username = request.POST.get("newname", None)
        password = request.POST.get("newpassword", None)
        email = request.POST.get("newemail", None)
        userlist = models.User.objects.all()
        #
        for u in userlist:
            print(u.user, u.password,u.email)
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
