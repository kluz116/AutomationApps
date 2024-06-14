from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .api_calls import debitCustomer, creditCustomer, AddTransferTransaction, AccountLookup, getCustomer
from .forms import AccountFormForm
from .models import Transaction, Accounts
from .serializers import TransactionSerializer, AddTransactionSerializer, CustomerSerializer


def getTransactions(request):
    dep = Transaction.objects.all().order_by('-id')
    return render(request, 'ecw/paymentinstructions.html', {'dep': dep})


@api_view(['POST'])
def postTransactionsDebit(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        transaction = debitCustomer(request.data)
        return Response(transaction)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def postTransactionsCredit(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        transaction = creditCustomer(request.data)
        return Response(transaction)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addTransactions(request):
    serializer = AddTransactionSerializer(data=request.data)
    if serializer.is_valid():
        transaction = AddTransferTransaction(request.data)
        return Response(transaction)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def GetAccountCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        transaction = AccountLookup(request.data)
        return Response(transaction)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def addCustomerNimble(request):
    form = AccountFormForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            bank_account = form['account_id'].value()

            clientDetails = getCustomer(bank_account)
            obj = Accounts.objects.create(**clientDetails)
            obj.save()

            messages.success(request, f'Successfully created customer')
            return HttpResponseRedirect('/LegalDoc/getCustomers')

    return render(request, 'addCustomer.html', {'form': form})
