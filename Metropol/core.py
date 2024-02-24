import db
'''import requests
import json
from views import getAccessToken, getBearerToken, getNin
from models import Cap'''


def getPendingCRB():

    cursor = db.conn.cursor()
    cursor.execute('select  top 1 OurBranchID,ApplicationID from t_CRBEnquiry where status =?', 'VALIDATING')
    for row in cursor:
        application_dic = {
            "OurBranchID": row[0],
            "ApplicationID": row[1]
        }
        return application_dic


print(getPendingCRB())

'''def addNimble():
    url = "http://10.255.201.148:92/api/v1/LoanApplication/GetLoanApplication"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getAccessToken()}'
    }

    url_cap = "https://api.metropol.co.ug:5557/api/v1/cap"
    headers_cap = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getBearerToken()}'
    }

    payload = json.dumps({
        "OurBranchID": OurBranchID,
        "ApplicationID": getPendingCRB,
        "ModuleID": "7035",
        "ApiOperatorID": "MN1519"
    }, indent=4)
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()

    application_date = res["LoanApplication"][0]["ApplicationDate"]
    partner_reference = res["LoanApplication"][0]["ApplicationID"]
    phone = res["ClientDetail"][0]["Mobile"]
    currency_code = res["LoanApplication"][0]["CurrencyID"]
    application_amount = res["LoanApplication"][0]["LoanAmount"]
    application_duration = res["LoanApplication"][0]["LoanTerm"]

    borrower_list = [{"identity_id_number": getNin(res["LoanApplication"][0]["ClientID"]),
                      "identity_type_code": "IDT10",
                      "country_code": "UG"}]

    payload_cap = json.dumps({
        "partner_bou_code": "UG001",
        "partner_branch_code": "001",
        "application_date": application_date,
        "partner_reference": partner_reference,
        "borrowers": borrower_list,
        "phone": phone,
        "currency_code": currency_code,
        "application_amount": application_amount,
        "application_duration": application_duration,
        "product_type_code": "7",
        "application_type_code": "I",
        "generate_report": "true"
    }, indent=4)

    response = requests.request("POST", url_cap, headers=headers_cap, data=payload_cap)

    result = response.json()
    res_message = result['api_code_description']

    data = {

        "partner_bou_code": "UG001",
        "partner_branch_code": "001",
        # "application_date": datetime.now().date(),
        "application_date": application_date,
        "partner_reference": partner_reference,
        "identity_id_number": getNin(res["LoanApplication"][0]["ClientID"]),
        "identity_type_code": "IDT04",
        "phone": phone,
        "currency_code": currency_code,
        "application_amount": application_amount,
        "application_duration": application_duration,
        "product_type_code": "7",
        "application_type_code": "I",
        "generate_report": "true"
    }
    obj = Cap.objects.create(**data)
    obj.save() '''''
