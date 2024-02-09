import datetime
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .legalDocForm import *
from django.contrib import messages
from django.contrib.auth.models import User
from .APIToken import getAccessToken
from django.contrib.auth.decorators import login_required
import requests
import smtplib
from email.message import EmailMessage
from .decorators import group_required

null = None


def handle_uploaded_file(f):
    with open("/home/ftb-uat/AutomationApps/uploads/+f.name", "wb+") as destination:
    # with open("D:/uploads/+f.name", "wb+") as destination:

        for chunk in f.chunks():
            destination.write(chunk)


def sendMail(subject, content, to):
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = subject
    msg['From'] = "cclog@financetrust.co.ug"
    msg['To'] = to

    # Send the message via our own SMTP server.
    server = smtplib.SMTP('mail.financetrust.co.ug', 587)
    server.starttls()
    server.login("cclog@financetrust.co.ug", "")
    server.send_message(msg)
    server.quit()


def index(request):
    return render(request, 'index.html', {})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')


            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("getCustomers")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={"login_form": form})


@login_required(login_url='/LegalDoc/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password1']

            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return redirect('getCustomers')
            else:
                form.add_error('old_password', 'Incorrect old password.')
    else:
        form = PasswordChangeForm()
    return render(request, 'change_password.html', {'form': form})

def logout_request_legal(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect('/LegalDoc/')


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin','Branch'])
def getCustomers(request):
    customer = Customer.objects.all().order_by('-id')
    return render(request, 'customers.html', {'customer': customer})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def getBranchesLegal(request):
    branch = Branch.objects.all().order_by('-id')
    return render(request, 'branches.html', {'branch': branch})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def addUsers(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/LegalDoc/addUsers')
        else:
            form = CustomUserCreationForm()

    context = {"form": form}
    return render(request, "addUsers.html", context)


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def addBranchLegal(request):
    form = BranchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully added a branch.")
            return HttpResponseRedirect('/LegalDoc/addBranch')
    return render(request, 'addBranch.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def addGroup(request):
    form = CustomGroupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully added a group.")
            return HttpResponseRedirect('/LegalDoc/addGroup')
    return render(request, 'addGroup.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin'])
def addCustomer(request):
    form = CustomerForm(request.POST or None)
    current_datetime = datetime.datetime.now()
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.created_by = request.user
            m.created_on = current_datetime
            m.save()
            # form.save()
            messages.success(request, "You have successfully added customer.")
            return HttpResponseRedirect('/LegalDoc/addCustomer')
    return render(request, 'addCustomer.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def getSecurityType(request):
    securitytype = SecurityType.objects.all().order_by('-id')
    return render(request, 'securitytype.html', {'securitytype': securitytype})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def addSecurityType(request):
    form = SecurityTypeForm(request.POST or None, )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully security type.")
            return HttpResponseRedirect('/LegalDoc/addSecurityType')
    return render(request, 'addSecurityType.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def addSecurityStatus(request):
    form = SecurityStatusForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully security status.")
            return HttpResponseRedirect('/LegalDoc/addSecurityStatus')
    return render(request, 'addSecurityStatus.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def getSecurityStatus(request):
    securitystatus = SecurityStatus.objects.all()
    return render(request, 'securitystatus.html', {'securitystatus': securitystatus})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def addLandTitleType(request):
    form = LandTitleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully land title.")
            return HttpResponseRedirect('/LegalDoc/addLandTitleType')
    return render(request, 'addLandTitle.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def getLandTitleType(request):
    landtitletype = LandTitleType.objects.all()
    return render(request, 'LandTitle.html', {'landtitletype': landtitletype})


def security_status(request):
    data = json.loads(request.body)
    securitystatus = SecurityStatus.objects.filter(security_type__id=data['user_id'])
    return JsonResponse(list(securitystatus.values("id", "name")), safe=False)


def landtitle(request):
    data = json.loads(request.body)
    landtitle = LandTitleType.objects.filter(security_type__id=data['user_id'])
    return JsonResponse(list(landtitle.values("id", "name")), safe=False)


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin','Branch'])
def addSecurity(request):
    form = SecurityForm(request.POST, request.FILES)
    current_datetime = datetime.datetime.now()
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.created_by = request.user
            m.created_at = current_datetime
            m.save()
            # form.save()

            content = f'New Security for Customer {m.client}  security type {m.security_type}, security status {m.security_status} Land Title Type {m.LandTitleType} Security Description {m.Security_Description} has been successfuly created by {request.user}'
            sendMail(f'New Security for {m.client} has been maintained on LegalDoc', content,
                     'allan.musembya@financetrust.co.ug')
            handle_uploaded_file(request.FILES["security_file"])
            messages.success(request, "You have successfully security.")
            return HttpResponseRedirect('/LegalDoc/addSecurity')
    return render(request, 'addSecurity.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin','Branch'])
def getSecurity(request):

    user_branch = request.user.branch
    user_group = request.user.group

    if str(user_group) == 'Branch':
        security = Security.objects.filter(branch=user_branch).order_by('-id')
        return render(request, 'security.html', {'security': security})
    else:
        security = Security.objects.all().order_by('-id')
        return render(request, 'security.html', {'security': security})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin'])
def updateSecurity(request, id):
    sec = Security.objects.get(id=id)

    if request.method == 'POST':
        form = SecurityEditForm(request.POST, instance=sec)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/LegalDoc/getSecurity')
    else:
        form = SecurityEditForm(instance=sec)
    return render(request, 'update_security.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin'])
def updateCustomer(request, id):
    sec = Customer.objects.get(id=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=sec)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/LegalDoc/getCustomers')
    else:
        form = CustomerForm(instance=sec)
    return render(request, 'update_customer.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def withdrawSecurity(request, id):
    sec = Security.objects.get(id=id)

    if request.method == 'POST':
        form = WithdrawForm(request.POST, instance=sec)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/LegalDoc/getSecurity')
    else:
        form = WithdrawForm(instance=sec)
    return render(request, 'withdraw_security.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin'])
def security_detail(request, id):
    security = get_object_or_404(Security, pk=id)

    return render(request, "security_detail.html", {"security": security})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def uploadSecurity(request, id):
    sec = Security.objects.get(id=id)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES, instance=sec)
        if form.is_valid():
            form.save()
            handle_uploaded_file(request.FILES["security_file"])
            return HttpResponseRedirect('/LegalDoc/getSecurity')
    else:
        form = UploadForm(instance=sec)
    return render(request, 'upload_security.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def download_file(request, file_id):
    uploaded_file = Security.objects.get(pk=file_id)
    if uploaded_file.security_file:
        response = HttpResponse(uploaded_file.security_file, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.security_file.name}"'
        return response
    else:
        return HttpResponseRedirect('/LegalDoc/getSecurity')


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def download_contract_file(request, file_id):
    uploaded_file = Contracts.objects.get(pk=file_id)
    if uploaded_file.contract_file:
        response = HttpResponse(uploaded_file.contract_file, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.contract_file.name}"'
        return response
    else:
        return HttpResponseRedirect('/LegalDoc/getContracts')


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def sendForMortgage(request, id):
    sec = Security.objects.get(id=id)

    if request.method == 'POST':
        form = MorgagedForm(request.POST, instance=sec)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/LegalDoc/getSecurity')
    else:
        form = MorgagedForm(instance=sec)
    return render(request, 'sendForMortgage.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def sentForFurtherCharges(request, id):
    sec = Security.objects.get(id=id)

    if request.method == 'POST':
        form = sentForFurtherCharge(request.POST, instance=sec)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/LegalDoc/getSecurity')
    else:
        form = sentForFurtherCharge(instance=sec)
    return render(request, 'sentForFurtherCharge.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager', 'Legal Admin'])
def addContract(request):
    form = ContractForm(request.POST, request.FILES)
    current_datetim = datetime.datetime.now()
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.created_by = request.user
            m.created_at = current_datetim
            m.save()

            handle_uploaded_file(request.FILES["contract_file"])
            messages.success(request, "You have successfully add contract.")
            return HttpResponseRedirect('/LegalDoc/addContract')
    return render(request, 'addContract.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def getContracts(request):
    contract = Contracts.objects.all().order_by('-id')
    return render(request, 'contracts.html', {'contract': contract})


@login_required(login_url='/LegalDoc/')
@group_required(['admin', 'Legal Manager'])
def updateContract(request, id):
    sec = Contracts.objects.get(id=id)

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=sec)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/LegalDoc/getContracts')
    else:
        form = ContractForm(instance=sec)
    return render(request, 'update_contracts.html', {'form': form})


@login_required(login_url='/LegalDoc/')
@group_required(['admin'])
def getUsers(request):
    user = CustomUser.objects.all().order_by('-id')
    return render(request, 'users.html', {'user': user})


def getClient(clientID):
    url = "http://10.255.201.179:8092/api/v1/ClientIdentity/GetClient"

    payload = json.dumps({
        "clientID": clientID,
        "direction": 0
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    firstname = res["clientQuery"][0]["firstName"]
    lastName = res["clientQuery"][0]["lastName"]
    middleName = res["clientQuery"][0]["middleName"]
    genderID = res["clientQuery"][0]["genderID"]
    nin = res["clientQuery"][0]["passportNo"]

    data_res = {
        "firstname": firstname,
        "middlename": middleName,
        "lastname": lastName,
        "gender": genderID,
        "national_id": nin
    }

    return data_res


@group_required(['admin', 'Legal Manager', 'Legal Admin','Branch'])
def addCustomerNimble(request):
    form = CustomerAddNimble(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            bank_account = form['bank_account'].value()

            url = "http://10.255.201.179:8092/api/v1/AccountMaintenance/GetAccountCustomer"

            payload = json.dumps({
                "AccountID": bank_account
            })
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {getAccessToken()}'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            res = response.json()
            client_id = res["ClientDetails"][0]["ClientID"]
            AccountID = res["ClientDetails"][0]["AccountID"]
            clientDetails = getClient(client_id)
            clientDetails['bank_account'] = AccountID
            clientDetails['created_by'] = request.user
            firstname = clientDetails['firstname']
            lastname = clientDetails['lastname']

            obj = Customer.objects.create(**clientDetails)
            obj.save()

            content = f'New Customer {firstname} {lastname} with Account {AccountID} has been successfuly created by {request.user}'
            sendMail(f'New Customer {AccountID} has been created on LegalDoc', content,
                     'allan.musembya@financetrust.co.ug')
            messages.success(request, f'Successfully created customer {AccountID}')
            return HttpResponseRedirect('/LegalDoc/getCustomers')

    return render(request, 'addCustomer.html', {'form': form})
