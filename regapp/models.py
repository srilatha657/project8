from django.db import models
class Reg(models.Model):
# Create your models here.
   firstname=models.CharField(max_length=10)
   lastname=models.CharField(max_length=10)
   username=models.CharField(max_length=10,primary_key=True)
   password=models.CharField(max_length=10)
   cpassword=models.CharField(max_length=10)
   Emailid=models.EmailField()
   Mobileno=models.IntegerField()