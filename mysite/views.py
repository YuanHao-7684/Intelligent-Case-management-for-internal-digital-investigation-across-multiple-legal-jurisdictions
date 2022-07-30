import os

from django.db.models import QuerySet
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from mysite import models
import docx
import random
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
        key=""
        for i in range(6):
            num =random.randint(0,9)
            letter = chr(random.randint(97,122))
            Letter = chr(random.randint(65,90))
            s = str(random.choice([num,letter,Letter]))
            key+=s
        for u in userlist:
            print(u.user,u.password,u.email)
        flag = models.User.objects.get_or_create(user=username, email=email, password=password,userKey=key)
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
        InvEmail = request.POST.get("InvEmail", None)
        caseSynopsis = request.POST.get("synopsis", None)
        caseType = request.POST.getlist("Type")
        currentuser = request.session.get("username")
        models.SetUpCases.objects.create(UserInputId=userinputID,
                                         caseName=caseName,
                                         caseScope=caseScope,
                                         caseInv=currentuser,
                                         caseInvEmail=InvEmail,
                                         caseType=caseType,
                                         casesynopsis=caseSynopsis,
                                         caseUserName=currentuser)
    # case process
    currentuser = request.session.get("username")
    userCase_list = models.SetUpCases.objects.filter(caseUserName=currentuser)
    return render(request, 'caseView.html',{'user': currentuser, 'caselist': userCase_list, 'listlen': len(userCase_list)})


#Evidence
def ShowCaseEvidence(request):

    cId=request.GET.get("caseid")
    caseN=models.SetUpCases.objects.filter(caseId=cId)
    currentCaseName=caseN[0].caseName
    Evidence_list = models.Evidence.objects.filter(ComCaseId=cId)
    currentuser = request.session.get("username")
    listlen=len(Evidence_list)
    return render(request, 'caseEviShowpage.html', {'user': currentuser,'caseName':currentCaseName,'caseId':cId,'evidences':Evidence_list,'lenevidence':listlen,})


def SetupnewEvidence(request):

    cId=request.GET.get("caseId")
    caseType = models.SetUpCases.objects.filter(caseId=cId)
    caseN = models.SetUpCases.objects.filter(caseId=cId)
    currentCaseType = caseType[0].caseScope
    a=currentCaseType.replace('[',"")
    b=a.replace(']',"")
    c=b.replace('\'',"")
    typelist=c.split(",")
    print(typelist)
    currentCaseName = caseN[0].caseName
    currentuser = request.session.get("username")
    request.session["currentCaseId"] = cId
    return render(request, 'NewEvidencePage.html', {'user': currentuser, 'caseName': currentCaseName, 'caseId': cId,'evidencescope':typelist})


#add evidence to own case
def NewEvidenceSubmit(request):
    if request.method == "POST":
        eName=request.POST.get("EviName")
        eviType=request.POST.get("type")
        principal=request.session.get("username")
        evidenceSummary=request.POST.get("summary")
        loc=request.POST.get("loc")
        cId=request.session.get("currentCaseId")
        loctaion=loc.strip()
        caseN = models.SetUpCases.objects.filter(caseId=cId)
        currentCaseName = caseN[0].caseName

        models.Evidence.objects.create(EvidenceName=eName,
                                       ComCaseId=cId,
                                       EvidenceType=eviType,
                                       EvidenceSummary=evidenceSummary,
                                       Principal=principal,
                                       EvidenceLoc=loctaion,
                                       ComCaseName=currentCaseName)
        del request.session["currentCaseId"]
        Evidence_list = models.Evidence.objects.filter(ComCaseId=cId)
        currentuser = request.session.get("username")
        listlen = len(Evidence_list)
        return render(request, 'caseEviShowpage.html',
                      {'user': currentuser, 'caseName': currentCaseName, 'caseId': cId, 'evidences': Evidence_list,
                       'lenevidence': listlen, })


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
    query=models.User.objects.filter(user=currentuser)
    userkey=query[0].userKey
    userCase_list = models.SetUpCases.objects.filter(caseInv=currentuser)
    return render(request, 'caseView.html',
                  {'user': currentuser, 'caselist': userCase_list, 'listlen': len(userCase_list),'userkey': userkey})
def Evidence(request):
    currentuser = request.session.get("username")
    Evidence_list = models.Evidence.objects.filter(Principal=currentuser)
    return render(request, 'Evidence.html', {'user': currentuser,"elist":Evidence_list,'lenevidence':len(Evidence_list)})

#Source mananget page
def source(request):
    currentuser = request.session.get("username")
    resultlist= models.Source.objects.filter(Principal=currentuser)
    return render(request, 'source.html', {'user': currentuser,'slist':resultlist,'lens':len(resultlist),})


#evidence Search pattern
def SerchEvidence(request):
    currentuser = request.session.get("username")
    return render(request, 'searchEvidence.html', {'user': currentuser})
def sEvidenceName(request):
    sforEvidenceName = request.POST.get("sEviname")

    result_list = models.Evidence.objects.filter(EvidenceName__icontains=sforEvidenceName)
    print(result_list)
    currentuser = request.session.get("username")
    return render(request, 'searchEvidence.html', {'user': currentuser, 'elist': result_list, 'listlen': len(result_list)})


# contact
def contact(request):
    currentuser =request.session.get("username")
    return render(request, 'contact.html', {'user': currentuser})


#case Search pattern & add evidence to other case
def SerchCase(request):
    currentuser = request.session.get("username")
    return render(request, 'searchCase.html', {'user': currentuser})
def sCaseName(request):
    sforCaseName=request.POST.get("sCasename")

    result_list=models.SetUpCases.objects.filter(caseName__icontains=sforCaseName)
    currentuser = request.session.get("username")
    return render(request, 'searchCase.html', {'user': currentuser,'caselist':result_list,'listlen':len(result_list)})

def addEvidenceToOtherCase(request):
    caseId = request.GET.get("caseid")
    result=models.SetUpCases.objects.filter(caseId=caseId)
    userofcase=result[0].caseInv
    caseName=result[0].caseName
    request.session["addcaseId"] = caseId
    return render(request, 'keyinputCase.html', {'user': currentuser, 'userofcase': userofcase,'cName':caseName})

def veifiyKey(request):
    currentuser = request.session.get("username")
    caseId = request.session.get("addcaseId")
    query=models.SetUpCases.objects.filter(caseId=caseId)
    caseName=query[0].caseName
    currentCaseType = query[0].caseScope
    a = currentCaseType.replace('[', "")
    b = a.replace(']', "")
    c = b.replace('\'', "")
    typelist = c.split(",")
    print(typelist)
    caseUser = request.GET.get("caseUser")
    result=models.User.objects.filter(user=caseUser)
    Key = result[0].userKey
    inputkey=request.POST.get("userkey")
    if Key == inputkey:
        return render(request, 'colNewevidence.html',
                      {'user': currentuser, 'caseName': caseName, 'caseId': caseId, 'evidencescope': typelist})
    else:
        messagelist = "Incorrect key, please confirm with this user"
        return render(request, 'keyinputCase.html', {'message': messagelist,'user': currentuser, 'userofcase': caseUser,'cName':caseName})
def colNewEvidenceSubmit(request):
    if request.method == "POST":
        eName = request.POST.get("EviName")
        eviType = request.POST.get("type")
        principal = request.session.get("username")
        evidenceSummary = request.POST.get("summary")
        loc = request.POST.get("loc")
        cId = request.session.get("addcaseId")
        loctaion = loc.strip()
        caseN = models.SetUpCases.objects.filter(caseId=cId)
        currentCaseName = caseN[0].caseName

        models.Evidence.objects.create(EvidenceName=eName,
                                       ComCaseId=cId,
                                       EvidenceType=eviType,
                                       EvidenceSummary=evidenceSummary,
                                       Principal=principal,
                                       EvidenceLoc=loctaion,
                                       ComCaseName=currentCaseName)
        del request.session["addcaseId"]
        currentuser = request.session.get("username")
        return render(request, 'searchCase.html', {'user': currentuser})






#ShowEvidenceSource
def ShowEvidenceSource(request):
    currentuser = request.session.get("username")
    eId = request.GET.get("evidenceid")
    result=models.Evidence.objects.filter(EvidenceId=eId)
    evidenceName=result[0].EvidenceName
    caseid=result[0].ComCaseId
    SourceList=models.Source.objects.filter(ComEvidenceId=eId)
    return render(request, 'EviSourceShowpage.html', {'user': currentuser,'eName':evidenceName,'eid':eId,'cid':caseid,'SourceList':SourceList,'listLen':len(SourceList)})

def SetupnewSource(request):
    currentuser = request.session.get("username")
    eId = request.GET.get("evidenceId")
    result = models.Evidence.objects.filter(EvidenceId=eId)
    evidenceName = result[0].EvidenceName
    return render(request, 'NewSourcePage.html', {'user': currentuser,'eName':evidenceName,'eid':eId})

def NewSourceSubmit(request):
    if request.method == "POST":
        currentuser = request.session.get("username")
        eId = request.GET.get("evidenceId")
        print(eId)
        result = models.Evidence.objects.filter(EvidenceId=eId)
        evidenceName = result[0].EvidenceName
        caseName = result[0].ComCaseName
        caseId = result[0].ComCaseId
        sName = request.POST.get("SName")
        sType = request.POST.get("type")
        sMan = request.POST.get("Manufacturer")
        sModel = request.POST.get("Model")
        sSystem = request.POST.get("System")
        Private = request.POST.get("pri")
        Principal = request.session.get("username")
        SerialNumber = request.POST.get("SerialNumber")
        Ssta = request.POST.get("status")
        AcquTool = request.POST.get("AcquTool")

        models.Source.objects.create(SourceName=sName,
                                     ComEvidenceId=eId,
                                     ComEvidenceName=evidenceName,
                                     ComCaseId=caseId,
                                     ComCaseName=caseName,
                                     SourceType=sType,
                                     Manufacturer=sMan,
                                     Model=sModel,
                                     System=sSystem,
                                     Private=Private,
                                     Principal=Principal,
                                     SerialNumber=SerialNumber,
                                     AcquTool=AcquTool,
                                     Encryptionstatus=Ssta)


        SourceList = models.Source.objects.filter(ComEvidenceId=eId)
        return render(request, 'EviSourceShowpage.html',
                      {'user': currentuser, 'eName': evidenceName, 'eid': eId, 'cid': caseId, 'SourceList': SourceList,
                       'listLen': len(SourceList)})
