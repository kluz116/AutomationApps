from datetime import datetime
from django.db import models
from AutomationApps import settings


# Create your models here.
class Cap(models.Model):
    identity_codes = [("IDT04", "Financial Card Number"), ("IDT10", "Country National ID Number"), ]
    app_status = [("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected"), ]

    partner_bou_code = models.CharField(max_length=7, default='UG001')
    partner_branch_code = models.CharField(max_length=3, default='001')
    application_date = models.DateField()
    partner_reference = models.CharField(max_length=15)
    identity_id_number = models.CharField(max_length=20)
    identity_type_code = models.CharField(max_length=50, choices=identity_codes, default='IDT04')
    phone = models.CharField(max_length=15)
    currency_code = models.CharField(max_length=15, default="UGX")
    application_amount = models.CharField(max_length=15)
    application_duration = models.CharField(max_length=15)
    product_type_code = models.CharField(max_length=15)
    application_type_code = models.CharField(max_length=15)
    generate_report = models.CharField(max_length=5, default="true")
    application_status_date = models.DateField(blank=True, null=True)
    application_status_code = models.CharField(max_length=15, blank=True, null=True)
    amount_approved = models.CharField(max_length=15, blank=True, null=True)
    application_rejection_reason = models.CharField(max_length=15, blank=True, null=True)
    application_rejection_reason_code = models.CharField(max_length=15, blank=True, null=True)
    application_status = models.CharField(max_length=15, choices=app_status, default='Pending')
    approved_duration = models.CharField(max_length=15, blank=True, null=True)

    # created_on = models.DateTimeField(default=datetime.now)
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.identity_id_number} '


class Report(models.Model):
    identity_codes = [("4", "Financial Card Number"), ("10", "Country National ID Number"), ]
    pull_reason = [("1", "New Credit Application"), ("2", "Review Of Existing Credit"),
                   ("3", "Customer Report Request"), ("4", "Review Existing Credit"),
                   ("5", "Stakeholder/Guarantor Report"), ]
    report_type = [("4", "Compact Report"), ("2", "Standard Report"), ("3", "Enhanced Report"), ("4", "Score Report"), ]
    identity_number = models.CharField(max_length=15)
    identity_type = models.CharField(max_length=15, choices=identity_codes)
    report_pull_reason = models.CharField(max_length=15, choices=pull_reason)
    report_type = models.CharField(max_length=15, choices=report_type)

    def __str__(self):
        return f'{self.identity_number} '


class Identity(models.Model):
    identity_codes = [("4", "Financial Card Number"), ("10", "Country National ID Number"), ]
    identity_number = models.CharField(max_length=15)
    identity_type = models.CharField(max_length=15, choices=identity_codes)

    def __str__(self):
        return f'{self.identity_number} '


class IdentityDetail(models.Model):
    identity_number = models.CharField(max_length=15)
    fcs = models.CharField(max_length=15)
    surname = models.CharField(max_length=150,blank=True, null=True)
    forename1 = models.CharField(max_length=150,blank=True, null=True)
    forename2 = models.CharField(max_length=150,blank=True, null=True)
    forename3 = models.CharField(max_length=150,blank=True, null=True)
    date_of_birth = models.CharField(max_length=50)
    gender = models.CharField(max_length=150)


    def __str__(self):
        return f'{self.identity_number} '
