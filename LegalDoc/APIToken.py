import requests
import json
from .api_urls import *


def closeAllSession():
    url = nimble_close

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
    url = nimble_token

    payload = json.dumps({
        "userID": "DK0657",
        "password": "Pass@word24",
        "branchID": "206",
        "systemID": "eee"
    })


    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res["accessToken"]



