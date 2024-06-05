import requests
import json
from .api_urls import *


def getBearerToken():
    url = auth_url
    payload = ""
    headers = {
        'Authorization': 'Basic dmI2RGNHNmRuRG92cUw3MnlNUktkNHo5OW9LblBjUUo6TkZLOTlYSHYzNXJrb0l1bA=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    res = response.json()
    return res['access_token']


def closeAllSession():
    url = nimble_close

    payload = json.dumps({
        "ourBranchID": "307",
        "operatorID": "MN1519"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()

    print(res)

def getAccessToken():
    closeAllSession()
    url = nimble_token

    payload = json.dumps({
        "userID": "MN1519",
        "password": "New@12345",
        "branchID": "307",
        "systemID": "eee"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res["accessToken"]


getAccessToken()
