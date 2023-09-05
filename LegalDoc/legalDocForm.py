from django import forms
from django.forms import HiddenInput

from .models import Branch, Customer, SecurityType, SecurityStatus, LandTitleType, Security


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ('created_by','created_on')
        widgets = {
            'birthdate': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'date_joined': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'gender': forms.Select(attrs={'class': ''}),
            'status': forms.Select(attrs={'class': 'form-control', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),
            'bank_branch': forms.Select(
                attrs={'class': 'selectpicker form-control', 'data-size': '5', 'tickIcon': 'glyphicon-ok',
                       'data-live-search': 'true', 'data-style': 'btn-white', 'data-header': 'Select a Branch'})
        }


class SecurityTypeForm(forms.ModelForm):
    class Meta:
        model = SecurityType
        fields = "__all__"


class SecurityStatusForm(forms.ModelForm):
    class Meta:
        model = SecurityStatus
        fields = "__all__"
        widgets = {
            'security_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'})
        }


class LandTitleForm(forms.ModelForm):
    class Meta:
        model = LandTitleType
        fields = "__all__"
        widgets = {
            'security_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'})
        }


class SecurityForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['branch','client', 'client_type', 'file_sec', 'Security_owner', 'security_type', 'security_status',
                  'LandTitleType', 'Lease_Hold_Tenure', 'LeaseHoldExpiryDate', 'DateRecieved', 'ForcedSaleValue',
                  'Security_Description', 'Insurance_Details']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                               'data-live-search': 'true', 'data-style': 'btn-white'}),

            'client': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),
            'security_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),
            'security_status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                   'data-live-search': 'true', 'data-style': 'btn-white'}),
            'LandTitleType': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),
            'client_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                               'data-live-search': 'true', 'data-style': 'btn-white'}),

            'LeaseHoldExpiryDate': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'DateRecieved': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
           # 'created_by': forms.Select(
                #attrs={'type': 'text', 'class': 'form-control', 'readonly': 'true'}
            #),
            'file_sec': forms.FileInput(attrs={'class': 'form-control', 'readonly': True}),

            #'created_at': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker-autoClose'}),
        }




class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['status', 'withdrawn_on']
        widgets = {
            'withdrawn_on': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),

        }


class UploadForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['file_sec']
        widgets = {

            'file_sec': forms.FileInput(attrs={'class': 'form-control '}),

        }


class MorgagedForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['security_status','sent_for_mortgaging_by','sent_for_mortgaging_at']
        widgets = {
            'security_status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                   'data-live-search': 'true', 'data-style': 'btn-white'}),
            'sent_for_mortgaging_by': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'readonly': 'true'}
            ),
            'sent_for_mortgaging_at': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control', 'readonly': 'True'}
            ),

        }


class sentForFurtherCharge(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['security_status','sent_for_further_charge_by','sent_for_further_charge_at']
        widgets = {
            'security_status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                                   'data-live-search': 'true', 'data-style': 'btn-white'}),
            'sent_for_further_charge_by': forms.Select(
                attrs={'type': 'text', 'class': 'form-control', 'readonly': 'true'}
            ),
            'sent_for_further_charge_at': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control', 'readonly': 'True'}
            ),

        }