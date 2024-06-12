from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models


# Create your models here.
class DepositFunds(models.Model):
    bankcode = models.CharField(max_length=30, null=False, default=37)
    accountnumber = models.CharField(max_length=15, blank=True, null=True, default='20680300000')
    amount = models.FloatField(max_length=15, null=False, blank=False)
    receiver = models.CharField(max_length=20)
    transactiontimestamp = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
    currency = models.CharField(max_length=5, blank=False, null=False, default='UGX')
    banktransactionid = models.CharField(max_length=15, null=False, blank=False)
    message = models.CharField(max_length=50, null=False, blank=False)
    receiverfirstname = models.CharField(max_length=50, null=False, blank=False)
    receiversurname = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)


class AccountHolder(models.Model):
    firstname = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    msisdn = models.CharField(max_length=50, null=False, blank=False)
    accountholderstatus = models.CharField(max_length=50, null=False, blank=False)
    profilename = models.CharField(max_length=50, null=False, blank=False)



