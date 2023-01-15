from django.shortcuts import render, redirect
from django.contrib.auth import authenticate 
from home.models import tabledb
# Create your views here.

def index(request):
    return render(request,'index.html')

def welcome(request):

    if request.method=="POST":
            
        username= request.POST.get('username')
        password= request.POST.get('password')
        print("auth rec")
        print(username)
        print(password)
        user = authenticate(username= username, password=password)
        print(user)

        if user is not None:
            # A backend authenticated the credentials
            return render(request, 'welcome.html')
        else:
            # No backend authenticated the credentials
            return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        sno=request.POST.get("sno")
        l2= request.POST.get("l2")
        task= request.POST.get("task")
        start= request.POST.get("start")
        finish= request.POST.get("finish")
        Tabledb= tabledb(sno=sno,l2id=l2,task=task, start=start,finish=finish)
        Tabledb.save()


    return render(request,'contact.html')