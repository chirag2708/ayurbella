from django.db import models



class Patient(models.Model):
    firstName=models.CharField(max_length=50,null=False)
    gender=models.CharField(max_length=50)
    Age=models.IntegerField()
    Name_Of_the_Person_taking_Appointment=models.CharField(max_length=50)
    Relationship_with_patient=models.CharField(max_length=50)
    PDA=models.CharField(max_length=50)
    Dr=models.CharField(max_length=50)
    Email=models.EmailField()
    phone=models.IntegerField(default=0)
    Country=models.CharField(max_length=50)


    def _str_(self):
       return  "%s" %(self.firstName)
