from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=20)
    branch_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Deposits(models.Model):
    name = models.CharField(max_length=300)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(default=0)
    accountBalance = models.BigIntegerField(default=0)
    mobile_number = models.CharField(default=0,max_length=9)

    def __str__(self):
        return self.name
