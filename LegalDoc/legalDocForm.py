from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,password_validation
from django.forms import HiddenInput


from .models import Branch, Customer, SecurityType, SecurityStatus, LandTitleType, Security, Contracts,CustomUser, CustomGroup


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

    class Meta:
        model = CustomUser
        fields = ('firstname','lastname','branch','email','is_staff','group','password1','password2',)
        widgets = {
            'firstname':  forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            #'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'branch': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),
            'group': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),
        }
        
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomGroupForm(forms.ModelForm):
    
    class Meta:
        model = CustomGroup
        fields = "__all__"

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
        widgets = {
            'branch_code':  forms.TextInput(attrs={'class':'form-control','placeholder':'Branch Code'}),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Branch Name'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ('created_by', 'created_on','status')
        widgets = {

            'gender': forms.Select(attrs={'class': 'form-control','placeholder': 'Gender'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'National ID (NIN)'}),
            'bank_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AccountID'}),
            'bank_tin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TIN'}),
            'bank_branch': forms.Select(
                attrs={'class': 'selectpicker form-control', 'data-size': '5', 'tickIcon': 'glyphicon-ok',
                       'data-live-search': 'true', 'data-style': 'btn-white', 'data-header': 'Select a Branch'})
        }


class SecurityTypeForm(forms.ModelForm):
    class Meta:
        model = SecurityType
        fields = "__all__"

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        }


class SecurityStatusForm(forms.ModelForm):
    class Meta:
        model = SecurityStatus
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
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
        fields = ['branch', 'client', 'client_type', 'security_file', 'Security_owner', 'security_type', 'security_status',
                  'LandTitleType', 'LeaseHoldStartDate','Lease_Hold_Tenure', 'Security_Description']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),

            'client': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),
            'security_type': forms.Select(attrs={'class': 'form-control  selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),
            'security_status': forms.Select(attrs={'class': 'form-control ', 'data-size': '5',
                                                   'data-live-search': 'true', 'data-style': 'btn-white'}),
            'LandTitleType': forms.Select(attrs={'class': 'form-control ', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),
            'client_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                               'data-live-search': 'true', 'data-style': 'btn-white','label':'Please select a string'}),

            'LeaseHoldStartDate': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'Security_Description':forms.TextInput(attrs={'class':'form-control','placeholder':'Security Description'}),
            'Security_owner': forms.TextInput(attrs={'class':'form-control','placeholder':'Security Owner'}),
            'Lease_Hold_Tenure':  forms.TextInput(attrs={'class':'form-control','placeholder':'Lease Hold Tenure'}),
            'security_file': forms.FileInput(attrs={'class': 'form-control','placeholder':'Security File'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['security_status'].queryset = SecurityStatus.objects.none()
        self.fields['LandTitleType'].queryset = LandTitleType.objects.none()
        self.fields['client'].queryset = Customer.objects.filter(status='No')
        if 'security_type' in self.data:
            try:
                security_type_id = int(self.data.get('security_type'))
                self.fields['security_status'].queryset = SecurityStatus.objects.filter(security_type_id=security_type_id).order_by('name')
                self.fields['LandTitleType'].queryset = LandTitleType.objects.filter(security_type_id=security_type_id)
            except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
        #elif self.instance.pk:
            #self.fields['security_status'].queryset = self.instance.security_type.name.order_by('name')

class SecurityEditForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['branch', 'client', 'client_type', 'security_file', 'Security_owner', 'security_type', 'security_status',
                  'LandTitleType', 'LeaseHoldStartDate','Lease_Hold_Tenure', 'Security_Description']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),

            'client': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),
            'security_type': forms.Select(attrs={'class': 'form-control  selectpicker', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),
            'security_status': forms.Select(attrs={'class': 'form-control ', 'data-size': '5',
                                                   'data-live-search': 'true', 'data-style': 'btn-white'}),
            'LandTitleType': forms.Select(attrs={'class': 'form-control ', 'data-size': '5',
                                                 'data-live-search': 'true', 'data-style': 'btn-white'}),
            'client_type': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                               'data-live-search': 'true', 'data-style': 'btn-white','label':'Please select a string'}),

            'LeaseHoldStartDate': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'Security_Description':forms.TextInput(attrs={'class':'form-control','placeholder':'Security Description'}),
            'Security_owner': forms.TextInput(attrs={'class':'form-control','placeholder':'Security Owner'}),
            'Lease_Hold_Tenure':  forms.TextInput(attrs={'class':'form-control','placeholder':'Lease Hold Tenure'}),
            'security_file': forms.FileInput(attrs={'class': 'form-control','placeholder':'Security File'}),
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
        fields = ['security_file']
        widgets = {

            'security_file': forms.FileInput(attrs={'class': 'form-control '}),

        }


class MorgagedForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['security_status', 'sent_for_mortgaging_by', 'sent_for_mortgaging_at']
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
        fields = ['security_status', 'sent_for_further_charge_by', 'sent_for_further_charge_at']
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


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts
        fields = ['Party_Name', 'branch', 'Contract_value', 'DateSigned', 'Duration', 'contract_file', 'status',
                  'Expiry_Date', 'Description', 'Compulsory_Terms', 'InsuranceTerms']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-control selectpicker', 'data-size': '5',
                                          'data-live-search': 'true', 'data-style': 'btn-white'}),

            'DateSigned': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'Expiry_Date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd', 'class': 'form-control'}
            ),
            'Party_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Party Name'}),
            'Compulsory_Terms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Compulsory Terms'}),
            'InsuranceTerms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insurance Terms'}),
            'Description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'Duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Duration'}),
            'Contract_value': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract Value'}),
            'contract_file': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contract File'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}),

        }
