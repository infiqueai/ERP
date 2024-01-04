from django.db import models

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
    S_No = models.AutoField(primary_key=True, default=1000)
    Session = models.CharField(max_length=100, blank=True, default="")
    Class = models.CharField(max_length=100, blank=True, default="")
    Group = models.CharField(max_length=100, blank=True, default="")
    Name = models.CharField(max_length=255, blank=True, default="")
    SR_No = models.IntegerField(default="")
    FatherName = models.CharField(max_length=255, blank=True, default="")
    MotherName = models.CharField(max_length=255, blank=True, default="")
    BirthDate = models.DateField(max_length=255, default="")
    Category = models.CharField(max_length=100, default="")
    Gender = models.CharField(max_length=10, default="")
    FatherMobile= models.CharField(max_length=15, default="")
    MotherMobile = models.CharField(max_length=15, default="")
    Address = models.TextField(blank=True, default="")

    def _str_(self):
        return self.Name
    
class stdInsert(models.Model):
    session=models.CharField(max_length=100)
    Class =models.CharField(max_length=100)
    group=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    sr_no=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    mothername=models.CharField(max_length=100)
    birthdate =models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    fathermobile=models.CharField(max_length=100)
    mothermobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    class Meta:
        db_table="admission"
    
from django.db import models

class Receipt(models.Model):
    receiptno = models.CharField(max_length=255)
    referenceno = models.CharField(max_length=255)
    student = models.CharField(max_length=255)
    paymentmodedetails = models.CharField(max_length=255)
    admissionno = models.CharField(max_length=255)
    session = models.CharField(max_length=255)
    Class = models.CharField(max_length=255)
    date = models.DateField()
    paymentmode = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "receipt"

class AccountDetails(models.Model):
    class Meta:
        db_table = 'account_details'
    S_No = models.AutoField(primary_key=True, default=1000)
    ReceiptNo = models.CharField(max_length=100, blank=True, default="")
    ReferenceNumber= models.CharField(max_length=100, blank=True, default="")
    Student= models.CharField(max_length=100, blank=True, default="")
    PaymentModeDetail= models.CharField(max_length=255, blank=True, default="")
    AdmissionNo = models.CharField(max_length=255, blank=True, default="")
    Session= models.IntegerField(default="")
    Class = models.DateField(max_length=255, default="")
    Date = models.CharField(max_length=100, default="")
    PaymentMode = models.CharField(max_length=10, default="")
    Amount = models.CharField(max_length=10, default="")
   
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
        
       