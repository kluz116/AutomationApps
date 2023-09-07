from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import *
from django_currentuser.db.models import CurrentUserField


class Branch(models.Model):
    name = models.CharField(max_length=20)
    branch_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class SecurityType(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class SecurityStatus(models.Model):
    name = models.CharField(max_length=100)
    security_type = models.ForeignKey(SecurityType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LandTitleType(models.Model):
    name = models.CharField(max_length=25)
    security_type = models.ForeignKey(SecurityType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Customer(models.Model):
    gender_list = [("M", "Male"), ("F", "Female"), ]
    firstname = models.CharField(max_length=60)
    middlename = models.CharField(max_length=60, blank=True)
    lastname = models.CharField(max_length=60)
    gender = models.CharField(max_length=1, choices=gender_list)
    #birthdate = models.DateField(db_comment="Birth Date")
    #address = models.CharField(max_length=60)
    #email = models.CharField(max_length=60, blank=True)
    #tel = models.CharField(max_length=60)
    national_id = models.CharField(max_length=12)
    #occupation = models.CharField(max_length=25, blank=True)
    #date_joined = models.DateField(db_comment="Birth Date", )
    #status = models.CharField(max_length=10, choices=[("live", "Live"), ("deceased", "Deceased")])
    #kin_name = models.CharField(max_length=60)
    #kin_relationship = models.CharField(max_length=60)
    #kin_tel = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=20, blank=True)
    #bank_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    bank_tin = models.CharField(max_length=20)
    created_on = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        ordering = ('-id',)


class Security(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    client_type = models.CharField(max_length=50,choices=[("borrower", "Borrower"), ("Powers_of_the_Attorney", "Powers of the Attorney")])
    status = models.CharField(max_length=50, choices=[("InCustody", "In Custody"),("Withdrawn", "Withdrawn"),("Expired", "Expired"),("Recieved", "Recieved")],default='InCustody')
    file_sec = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    Security_owner = models.CharField(max_length=20)
    security_type = models.ForeignKey(SecurityType, on_delete=models.CASCADE)
    security_status = models.ForeignKey(SecurityStatus, on_delete=models.CASCADE)
    LandTitleType = models.ForeignKey(LandTitleType, on_delete=models.CASCADE)
    Lease_Hold_Tenure= models.CharField(max_length=50,blank=True)
    LeaseHoldExpiryDate = models.DateField()
    #DateRecieved = models.DateField()
    #ForcedSaleValue = models.CharField(max_length=100)
    Security_Description = models.CharField(max_length=100)
    #Insurance_Details = models.CharField(max_length=100,blank=True)
    withdrawn_on = models.DateField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    #created_by = CurrentUserField()
    sent_for_mortgaging_by = CurrentUserField(related_name='sent_for_mortgaging_by')
    sent_for_mortgaging_at = models.DateField(default=datetime.now)
    sent_for_further_charge_by = CurrentUserField(related_name='sent_for_further_charge_by')
    sent_for_further_charge_at = models.DateField(default=datetime.now)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    #created_by = models.ForeignKey('auth.User', related_name='created_by_user',on_delete=models.CASCADE)


class Contracts(models.Model):
    Party_Name = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    Contract_value =models.FloatField(max_length=20)
    DateSigned = models.DateField(default=datetime.now)
    Duration = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=[("on", "On"),("Expired", "Expired"),("Expired", "Expired"),("Terminated", "Terminated")],default='on')
    Expiry_Date=models.DateField(default=datetime.now)
    Description = models.CharField(max_length=200)
    Compulsory_Terms = models.CharField(max_length=200)
    InsuranceTerms = models.CharField(max_length=200)
    contract_file = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now)
    
    