from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

from django.contrib.auth.models import User
from django.core.mail import send_mail
from random import randrange



class Otp(View):
    pw=""
    customer=""

    def get(self, request):
        return render (request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        Otp.customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (Otp.customer)

        if not error_message:
            if request.method=="POST":
                
                try:
                    
                    Otp.pw=""
                    text="123456789"
                    for i in range(4):
                        Otp.pw=Otp.pw+text[randrange(len(text))]
                    print(Otp.pw)
                    subject="Welcome to Ayurbella Clinic"
                    text="Your Otp is " + str(Otp.pw)
                    from_email="chirag.tester2002@gmail.com"
                    to_email=[str(email)]
                    send_mail(subject,text,from_email,to_email)
                    return render(request,"otp.html")
                except User.DoesNotExist:
                    return render(request,"signup.html",{"msg":"User Does Not Exist"})
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving
        

        return error_message