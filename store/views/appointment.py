from django.shortcuts import render
from store.models.patient import Patient
from django.http import HttpResponse
from django.core.mail import send_mail


def appointment(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        gndr = request.POST['gender']
        age = request.POST['Age']
        name = request.POST['Name_Of_the_Person_taking_Appointment']
        relation = request.POST['Relationship_with_patient']
        PDA = str(request.POST['PDA'])
        Dr = request.POST['Dr']
        Email = request.POST['Email']
        phone = int(request.POST['phone'])
        Country = request.POST['Country']

        patient = Patient(firstName=first_name, gender=gndr, Age=age, Name_Of_the_Person_taking_Appointment=name,
                            Relationship_with_patient=relation, PDA=PDA, Dr=Dr, Email=Email, phone=phone, Country=Country)
        patient.save()
        if request.method == "POST":

            try:

                subject = "Appointment at Ayurbella Clinic"
                text = "We have successfully received your request for the appointment at Ayurbella Clinic we will check the availability with the doctor as per your prefered date and time and revert you back. \n\n\n\n\n\n\n Regards,\n Ayurbella Clinic"
                from_email = "chirag.tester2002@gmail.com"
                to_email = [str(Email)]
                send_mail(subject, text, from_email, to_email)
                return render(request, "appointment.html",{"msg":"Appointment request placed Successfully.!"})
            except Exception:
                return render(request, "appointment.html", {"msg": Exception})
        return HttpResponse("Request added successfully")

    elif request.method == 'GET':
        return render(request, 'appointment.html')

    else:
        return HttpResponse("Connection error")
