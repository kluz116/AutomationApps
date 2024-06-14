from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Transaction(models.Model):
    account_id = models.CharField(max_length=20)
    account_type_id = models.CharField(max_length=1)
    amount = models.FloatField()
    cheque_id = models.CharField(max_length=10,null=True)
    cost_center_id = models.CharField(max_length=10)
    dont_return_serial = models.BooleanField()
    exchange_rate = models.FloatField()
    forward_remark = models.TextField(blank=True, null=True)
    instrument_type_id = models.CharField(max_length=1)
    local_amount = models.FloatField()
    main_gl_id = models.CharField(max_length=10)
    mean_rate = models.FloatField()
    module_id = models.CharField(max_length=10)
    operator_id = models.CharField(max_length=10)
    other_details = models.CharField(max_length=30, blank=True, null=True)
    our_branch_id = models.CharField(max_length=10)
    portfolio_account_id = models.CharField(max_length=10, blank=True, null=True)
    portfolio_branch_id = models.CharField(max_length=10, blank=True, null=True)
    portfolio_series = models.CharField(max_length=10)
    product_id = models.CharField(max_length=10)
    profit = models.FloatField()
    reference_no = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=255)
    serial_id = models.CharField(max_length=10)
    sl_no = models.CharField(max_length=10)
    trx_amount = models.FloatField()
    trx_branch_id = models.CharField(max_length=10)
    trx_code_id = models.CharField(max_length=10)
    trx_currency_id = models.CharField(max_length=10)
    trx_date = models.DateTimeField()
    trx_description = models.CharField(max_length=255)
    trx_description_id = models.CharField(max_length=10)
    trx_flag_id = models.CharField(max_length=10, blank=True, null=True)
    trx_type_id = models.CharField(max_length=10)
    value_date = models.DateTimeField()


class Accounts(models.Model):
    account_id = models.CharField(max_length=20)
    ourbranch_id = models.CharField(max_length=10)
    accountname =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='yourmodel_created_by')
