from django.shortcuts import render
from mysite import models
# Create your views here.
from django.shortcuts import HttpResponse
messagelist=[]

def index(request):
    return render(request, 'index.html')
def signup(request):
    messagelist.clear()
    if request.method == "POST":
        username = request.POST.get("newname", None)
        password = request.POST.get("newpassword", None)
        email = request.POST.get("newemail", None)
        flag=models.User.objects.get_or_create(user=username, email=email, password=password)
    if(flag==True):
        truemessage={"message":"you have create a new account"}
        messagelist.append(truemessage)
        return render(request, 'index.html')
    else:
        failmessage={"message":"you already have a account,log in now"}
        messagelist.append(failmessage)
        return render(request, 'index.html')
def homepage(request):
    return render(request,'homepage.html')