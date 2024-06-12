from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .EcwForms import *
from .api_calls import *

# Create your views here.

# Create your views here.
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
                return redirect("getDeposits")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name='ecw/login.html', context={"login_form": form})


def logout_request_metropol(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect('/ecw/')


@login_required(login_url='/ecw/')
def getIndex(request):
    return render(request, 'ecw/index.html', {})


def addDeposit(request):
    form = DepositForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            bankcode = form['bankcode'].value()
            accountnumber = form['accountnumber'].value()
            amount = form['amount'].value()
            receiver = form['receiver'].value()
            transactiontimestamp = form['transactiontimestamp'].value()
            currency = form['currency'].value()
            #banktransactionid = form['banktransactionid'].value()
            message = form['message'].value()

            banktransactionid = generate_random_trx_id()

            res = depositFunds(bankcode, accountnumber, amount, transactiontimestamp, currency, receiver,
                               banktransactionid, message)

            first_name = res["receiverfirstname"]
            sur_name = res["receiversurname"]
            status =  res["status"]

            deposit_obj_data = {
                "bankcode": bankcode,
                "accountnumber": accountnumber,
                "amount": amount,
                "receiver": receiver,
                "transactiontimestamp": transactiontimestamp,
                "currency": currency,
                "banktransactionid": banktransactionid,
                "message": message,
                "receiverfirstname": first_name,
                "receiversurname": sur_name,
                "status": status }

            obj = DepositFunds.objects.create(**deposit_obj_data)
            obj.save()
            messages.success(request, f'Successful deposit of {amount} UGX to {receiver} with status :{status}')
            return HttpResponseRedirect('/ecw/getDeposits')
        else:
            print(form.errors)
    return render(request, 'ecw/create_deposit.html', {'form': form})


def getDeposits(request):
    dep = DepositFunds.objects.all().order_by('-id')
    return render(request, 'ecw/deposits.html', {'dep': dep})


def addAccountHolder(request):
    form = AccountHolderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            phone_nmber = form['msisdn'].value()

            res = getAccontHolderInfo(phone_nmber)

            firstname = res['firstname']
            surname = res['surname']
            accountholderstatus = res['accountholderstatus']
            profilename = res['profilename']
            msisdn = res['msisdn']
            msg = res['msg']

            account_holder_obj_data = {
                "firstname": firstname,
                "surname": surname,
                "msisdn": msisdn,
                "accountholderstatus": accountholderstatus,
                "profilename": profilename}

            obj = AccountHolder.objects.create(**account_holder_obj_data)
            obj.save()
            #form.save()
            messages.success(request, f'{msg}')
            return HttpResponseRedirect('/ecw/getAccountHolders')
    return render(request, 'ecw/add_account_holder.html', {'form': form})

def getAccountHolders(request):
    dep = AccountHolder.objects.all().order_by('-id')
    return render(request, 'ecw/account_holders.html', {'dep': dep})

