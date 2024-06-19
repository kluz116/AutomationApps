from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models


# Create your models here.
class DepositFunds(models.Model):
    deposists_to = [("phone_number", "PhoneNumber (Msisdn)"), ("external_id", "External ID"), ]
    bankcode = models.CharField(max_length=30, null=False, default=37)
    accountnumber = models.CharField(max_length=15, blank=True, null=True, default='20680300000')
    amount = models.FloatField(max_length=15, null=False, blank=False)
    receiver = models.CharField(max_length=35)
    transactiontimestamp = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
    currency = models.CharField(max_length=5, blank=False, null=False, default='UGX')
    banktransactionid = models.CharField(max_length=15, null=False, blank=False)
    message = models.CharField(max_length=50, null=False, blank=False)
    receiverfirstname = models.CharField(max_length=50, null=False, blank=False)
    receiversurname = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)
    trx_batchid = models.CharField(max_length=50, null=False, blank=False)
    trx_serialid = models.CharField(max_length=50, null=False, blank=False)



class AccountHolder(models.Model):
    firstname = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    msisdn = models.CharField(max_length=50, null=False, blank=False)
    accountholderstatus = models.CharField(max_length=50, null=False, blank=False)
    profilename = models.CharField(max_length=50, null=False, blank=False)


class TransactionTimestamp(models.Model):
    timestamp = models.CharField(max_length=100)


class Amount(models.Model):
    amount = models.FloatField()
    currency = models.CharField(max_length=3)


class PaymentInstructionRequest(models.Model):
    transactiontimestamp = models.OneToOneField(TransactionTimestamp, on_delete=models.CASCADE)
    amount = models.OneToOneField(Amount, on_delete=models.CASCADE)
    paymentinstructionid = models.CharField(max_length=20)
    receiverbankcode = models.CharField(max_length=20)
    receiveraccountnumber = models.CharField(max_length=20)
    receiverfirstname = models.CharField(max_length=50)
    receiversurname = models.CharField(max_length=50)
    message = models.CharField(max_length=255)
    transmissioncounter = models.CharField(max_length=255,null=True)
    transactionid = models.CharField(max_length=255,null=True)





