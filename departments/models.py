from django.db import models

# Create your models here.


class register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  

    def __str__(self):
        return self.username
    
class StudentDetails(models.Model):
    class Meta:
        db_table = 'details_student'
    S_no = models.AutoField(primary_key=True, default=1000)
    Session = models.CharField(max_length=100, blank=True, default="")
    Class = models.CharField(max_length=100, blank=True, default="")
    Group = models.CharField(max_length=100, blank=True, default="")
    Name = models.CharField(max_length=255, blank=True, default="")
    Father_name = models.CharField(max_length=255, blank=True, default="")
    Mother_name = models.CharField(max_length=255, blank=True, default="")
    sr_no = models.IntegerField(default="")
    Birth_date = models.DateField(max_length=255, default="")
    Category = models.CharField(max_length=100, default="")
    Gender = models.CharField(max_length=10, default="")
    Primary_parent_mobile_no = models.CharField(max_length=15, default="")
    Mother_mobile = models.CharField(max_length=15, default="")
    Address = models.TextField(blank=True, default="")

    def _str_(self):
        return self.Name
    


class stdInsert(models.Model):
    studentname=models.CharField(max_length=100)
    fathername =models.CharField(max_length=100)
    mothername=models.CharField(max_length=100)
    Class=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    class Meta:
        db_table="admission"
    
from django.db import models

class Receipt(models.Model):
    receiptno = models.CharField(max_length=50)
    studentname = models.CharField(max_length=45)
    studentclass = models.CharField(max_length=45)
    session = models.CharField(max_length=45)
    amountpaid = models.DecimalField(max_digits=10, decimal_places=2)
    totalfees = models.DecimalField(max_digits=10, decimal_places=2)
    modeofpayment = models.CharField(max_length=45)

    class Meta:
        db_table = "receipt"

class AccountDetails(models.Model):
    class Meta:
        db_table = 'account_details'
    S_no = models.AutoField(primary_key=True, default=1000)
    Session = models.CharField(max_length=100, blank=True, default="")
    Class = models.CharField(max_length=100, blank=True, default="")
    StudentName = models.CharField(max_length=100, blank=True, default="")
    AdmissionNo = models.CharField(max_length=255, blank=True, default="")
    Fee = models.CharField(max_length=255, blank=True, default="")
    Receipts = models.IntegerField(default="")
    TotalPaid = models.DateField(max_length=255, default="")
    Amount = models.CharField(max_length=100, default="")
    Status = models.CharField(max_length=10, default="")
   
    def _str_(self):
        return self.StudentName
  

from django.db import models

class CommonStudent(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    AdmissionNumber = models.CharField(max_length=20)
    AdmissionDate = models.DateField()
    Gender = models.CharField(max_length=10)
    Nationality = models.CharField(max_length=50)
    Religion = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    DateofBirth = models.DateField()
    BloodGroup = models.CharField(max_length=5)
    Address = models.TextField()
    City = models.CharField(max_length=50)
    PinCode = models.CharField(max_length=10)
    IsEmandateRequired = models.BooleanField()
    FatherName = models.CharField(max_length=255)
    FatherAddress = models.TextField()
    FatherCity = models.CharField(max_length=50)
    FatherAnnualIncome = models.DecimalField(max_digits=12, decimal_places=2)
    FatherMobile = models.CharField(max_length=15)
    FatherCommunicationOn = models.CharField(max_length=255)
    FatherPrimary = models.BooleanField()
    MotherName = models.CharField(max_length=255)
    MotherAddress = models.TextField()
    MotherCity = models.CharField(max_length=50)
    MotherAnnualIncome = models.DecimalField(max_digits=12, decimal_places=2)
    MotherMobile = models.CharField(max_length=15)
    MotherCommunicationOn = models.CharField(max_length=255)
    SessionSequenceNumber = models.IntegerField()
    ClassSequenceNumber = models.IntegerField()
    startyear= models.IntegerField()
    endyear= models.IntegerField()

    class Meta:
        abstract = True
        
        
from .models import CommonStudent

class Table1(CommonStudent):
    class Meta:
        db_table = '2021-2022'

class Table2(CommonStudent):
    class Meta:
        db_table = '2020-2021'
        
       