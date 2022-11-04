from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from store.views.Otp import *


def Signup(request):
    if request.method=="POST":
        o1=request.POST.get("o1")
        o2=request.POST.get("o2")
        o3=request.POST.get("o3")
        o4=request.POST.get("o4")
        otp=str(o1+o2+o3+o4)
        print("signup:-",otp)
        
        if(otp==Otp.pw):
            
            Otp.customer.password = make_password (Otp.customer.password)
            Otp.customer.register ()
            return render (request,"login.html")
        else:
            return render(request,"otp.html",{"msg":"Invalid Otp.!"})
    else:
        return render (request, 'otp.html')







    
