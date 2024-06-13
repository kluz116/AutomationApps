from ecw.models import *
from django import forms


class DepositForm(forms.ModelForm):
    class Meta:
        model = DepositFunds
        fields = "__all__"
        exclude = ( 'receiversurname', 'receiverfirstname','status','banktransactionid')

        widgets = {
            'bankcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Code'}),
            'accountnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'receiver': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Receiver Phone Number'}),
            'transactiontimestamp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'transactiontimestamp'}),
            'currency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'currency'}),
            #'banktransactionid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'banktransactionid'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'message'}),

        }

class DepositFormExternal(forms.ModelForm):
    class Meta:
        model = DepositFunds
        fields = "__all__"
        exclude = ( 'receiversurname', 'receiverfirstname','status','banktransactionid')

        widgets = {
            'bankcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Code'}),
            'accountnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'receiver': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put External ID '}),
            'transactiontimestamp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'transactiontimestamp'}),
            'currency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'currency'}),
            #'banktransactionid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'banktransactionid'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'message'}),

        }

class AccountHolderForm(forms.ModelForm):
    class Meta:
        model = AccountHolder
        fields = "__all__"
        exclude = ('firstname', 'surname','accountholderstatus','profilename')


        widgets = {
            'msisdn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),


        }
