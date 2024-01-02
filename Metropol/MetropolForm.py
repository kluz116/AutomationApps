from Metropol.models import *
from django import forms



class CapForm(forms.ModelForm):
    class Meta:
        model = Cap
        fields = "__all__"
        # exclude = ( 'partner_bou_code', 'partner_branch_code', 'generate_report', 'currency_code')
        exclude = ('application_status', 'amount_approved', 'approved_duration', 'application_status_code',
                   'application_status_date', 'application_rejection_reason', 'application_rejection_reason_code',)
        # exclude = ('created_on')
        widgets = {
            'identity_type_code': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                      'data-live-search': 'true', 'data-style': 'btn-white'}),
            'partner_bou_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'partner_bou_code'}),
            'partner_branch_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'application_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'partner_reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Application ID'}),
            'identity_id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'National ID (NIN)'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'currency_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Currency code'}),
            'application_amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Application amount'}),

            'application_duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Duration'}),
            'product_type_code': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                      'data-live-search': 'true', 'data-style': 'btn-white'}),
            'application_type_code': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                      'data-live-search': 'true', 'data-style': 'btn-white'}),
            'generate_report': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'generate_report'}),
        }


class UpdateCapForm(forms.ModelForm):
    class Meta:
        model = Cap
        fields = ['partner_reference', 'application_status', 'amount_approved','partner_bou_code','application_status_code', 'application_status_date', 'approved_duration','application_rejection_reason', 'application_rejection_reason_code', ]

        widgets = {
            'application_status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                      'data-live-search': 'true', 'data-style': 'btn-white'}),
            'partner_bou_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'partner_bou_code'}),
            'application_status_code': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Application status code'}),
            'application_status_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'application_rejection_reason': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Application rejection reason'}),
            'application_rejection_reason_code': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Application rejection reason code'}),

            'amount_approved': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Amount Approved'}),

        }


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"

        widgets = {
            'identity_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIN Or FCS'}),
            'identity_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),

            'report_pull_reason': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                      'data-live-search': 'true', 'data-style': 'btn-white'}),
            'report_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                               'data-live-search': 'true', 'data-style': 'btn-white'}),

        }


class IdentityForm(forms.ModelForm):
    class Meta:
        model = Identity
        fields = "__all__"

        widgets = {
            'identity_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIN Or FCS'}),
            'identity_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),

        }
