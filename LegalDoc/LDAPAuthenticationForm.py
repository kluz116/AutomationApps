from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django_python3_ldap.auth import LDAPBackend


class LDAPAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            ldap_backend = LDAPBackend()
            print(username)
            print(password)
            user = ldap_backend.authenticate(self.request, username=username, password=password)
            print(user)
                 #Tri<><><>******Kluz@6028********
            if not user:
                raise forms.ValidationError("Invalid LDAP credentials.")

        return self.cleaned_data

    def login_request(request):
        if request.method == 'POST':
            form = LDAPAuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                user = form.get_user()
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect("getCustomers")
        else:
            form = LDAPAuthenticationForm()
        return render(request, 'login.html', {'login_form': form})

