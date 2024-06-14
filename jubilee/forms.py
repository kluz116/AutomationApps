from .models import *
from django import forms


class AccountFormForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = "__all__"
        exclude = ( 'ourbranch_id', 'accountname', 'created_at', 'created_by')

        widgets = {
            'account_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),


        }
