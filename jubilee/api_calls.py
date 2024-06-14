import requests
import json


def closeAllSession():
    url = "http://10.255.201.179:8092/api/v1/Common/CloseAllSessions"

    payload = json.dumps({
        "ourBranchID": "206",
        "operatorID": "DK0657"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()

    print(res)


def getAccessToken():
    closeAllSession()
    url = "http://10.255.201.179:8093/api/v1/Token/LoginUser"

    payload = json.dumps({
        "userID": "DK0657",
        "password": "New@1234",
        "branchID": "206",
        "systemID": "eee"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res["accessToken"]


def debitCustomer(payload_obj):
    url = "http://10.255.201.179:8092/api/v1/TransferTransaction/UpdateTransferTransaction"

    payload = json.dumps({
        "AccountID": payload_obj['account_id'],
        "AccountTypeID": payload_obj['account_type_id'],
        "Amount": payload_obj['amount'],
        #"ChequeDate": payload_obj['cheque_date'],
        "ChequeID": payload_obj['cheque_id'],
        "CostCenterID": payload_obj['cost_center_id'],
        "DontReturnSerial": payload_obj['dont_return_serial'],
        "ExchangeRate": payload_obj['exchange_rate'],
        "ForwardRemark": payload_obj['forward_remark'],
        "InstrumentTypeID": payload_obj['instrument_type_id'],
        "LocalAmount": payload_obj['local_amount'],
        "MainGLID": payload_obj['main_gl_id'],
        "MeanRate": payload_obj['mean_rate'],
        "ModuleID": payload_obj['module_id'],
        "OperatorID": payload_obj['operator_id'],
        "OtherDetails": payload_obj['other_details'],
        "OurBranchID": payload_obj['our_branch_id'],
        "PortfolioAccountID": payload_obj['portfolio_account_id'],
        "PortfolioBranchID": payload_obj['portfolio_branch_id'],
        "PortfolioSeries": payload_obj['portfolio_series'],
        "ProductID": payload_obj['product_id'],
        "Profit": payload_obj['profit'],
        "ReferenceNo": payload_obj['reference_no'],
        "Remarks": payload_obj['remarks'],
        "SerialID": payload_obj['serial_id'],
        "SlNo": payload_obj['sl_no'],
        "TrxAmount": payload_obj['trx_amount'],
        "TrxBranchID": payload_obj['trx_branch_id'],
        "TrxCodeID": payload_obj['trx_code_id'],
        "TrxCurrencyID": payload_obj['trx_currency_id'],
        "TrxDate": payload_obj['trx_date'],
        "TrxDescription": payload_obj['trx_description'],
        "TrxDescriptionID": payload_obj['trx_description_id'],
        "TrxFlagID": payload_obj['trx_flag_id'],
        "TrxTypeID": payload_obj['trx_type_id'],
        "ValueDate": payload_obj['value_date']
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())


def creditCustomer(payload_obj):
    url = "http://10.255.201.179:8092/api/v1/TransferTransaction/UpdateTransferTransaction"

    payload = json.dumps({
        "AccountID": payload_obj['account_id'],
        "AccountTypeID": payload_obj['account_type_id'],
        "Amount": payload_obj['amount'],
        #"ChequeDate": payload_obj['cheque_date'],
        "ChequeID": payload_obj['cheque_id'],
        "CostCenterID": payload_obj['cost_center_id'],
        "DontReturnSerial": payload_obj['dont_return_serial'],
        "ExchangeRate": payload_obj['exchange_rate'],
        "ForwardRemark": payload_obj['forward_remark'],
        "InstrumentTypeID": payload_obj['instrument_type_id'],
        "LocalAmount": payload_obj['local_amount'],
        "MainGLID": payload_obj['main_gl_id'],
        "MeanRate": payload_obj['mean_rate'],
        "ModuleID": payload_obj['module_id'],
        "OperatorID": payload_obj['operator_id'],
        "OtherDetails": payload_obj['other_details'],
        "OurBranchID": payload_obj['our_branch_id'],
        "PortfolioAccountID": payload_obj['portfolio_account_id'],
        "PortfolioBranchID": payload_obj['portfolio_branch_id'],
        "PortfolioSeries": payload_obj['portfolio_series'],
        "ProductID": payload_obj['product_id'],
        "Profit": payload_obj['profit'],
        "ReferenceNo": payload_obj['reference_no'],
        "Remarks": payload_obj['remarks'],
        "SerialID": payload_obj['serial_id'],
        "SlNo": payload_obj['sl_no'],
        "TrxAmount": payload_obj['trx_amount'],
        "TrxBranchID": payload_obj['trx_branch_id'],
        "TrxCodeID": payload_obj['trx_code_id'],
        "TrxCurrencyID": payload_obj['trx_currency_id'],
        "TrxDate": payload_obj['trx_date'],
        "TrxDescription": payload_obj['trx_description'],
        "TrxDescriptionID": payload_obj['trx_description_id'],
        "TrxFlagID": payload_obj['trx_flag_id'],
        "TrxTypeID": payload_obj['trx_type_id'],
        "ValueDate": payload_obj['value_date']
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())


def AddTransferTransaction(payload_obj):
    url = "http://10.255.201.179:8092/api/v1/TransferTransaction/AddTransferTransaction"

    payload = json.dumps({
        "ModuleID": "3020",
        "OperatorID": "DK0657",
        "SerialID": payload_obj['serial_id'],
        "TrxBranchID": payload_obj['trx_branchid']
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def AccountLookup(payload_obj):
    url = "http://10.255.201.179:8092/api/v1/AccountMaintenance/GetAccountCustomer"


    payload = json.dumps({
        "AccountID": payload_obj['account_id']
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

def getCustomer(bank_account):
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

    account_id = res["ClientDetails"][0]["AccountID"]
    ourbranch_id = res["ClientDetails"][0]["OurBranchID"]
    accountname = res["ClientDetails"][0]["ClientName"]

    return {"account_id":account_id,"ourbranch_id":ourbranch_id,"accountname":accountname}


