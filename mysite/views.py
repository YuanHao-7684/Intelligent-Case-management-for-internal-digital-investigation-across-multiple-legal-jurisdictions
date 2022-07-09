from django.shortcuts import render
from mysite import models
# Create your views here.
from django.shortcuts import HttpResponse

messagelist = []
currentuser = ""


def index(request):
    return render(request, 'index.html')


def signup(request):
    messagelist.clear()
    if request.method == "POST":
        username = request.POST.get("newname", None)
        password = request.POST.get("newpassword", None)
        email = request.POST.get("newemail", None)
        flag = models.User.objects.get_or_create(user=username, email=email, password=password)
    if (flag == True):
        truemessage = {"message": "you have create a new account"}
        messagelist.append(truemessage)
        return render(request, 'index.html')
    else:
        failmessage = {"message": "you already have a account,log in now"}
        messagelist.append(failmessage)
        return render(request, 'index.html')


def homepage(request):
    currentuser = "Hao Yuan"
    return render(request, 'homepage.html', {'user': currentuser})


def patternpage(request):
    currentuser = "Hao Yuan"
    return render(request, 'list pages.html', {'user': currentuser})





# case management
def cases(request):
    currentuser = "Hao Yuan"
    return render(request, 'casepage.html', {'user': currentuser})


def View(request):
    currentuser = "Hao Yuan"
    return render(request, 'caseView.html', {'user': currentuser})


def Log(request):
    currentuser = "Hao Yuan"
    return render(request, 'caseLog.html', {'user': currentuser})


def Report(request):
    currentuser = "Hao Yuan"
    return render(request, 'caseReport.html', {'user': currentuser})


#contact
def contact(request):
    currentuser="Hao Yuan"
    return render(request,'contact.html',{'user': currentuser})