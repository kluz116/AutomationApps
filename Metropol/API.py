import requests
import json


def closeAllSession():
    url = "http://10.255.201.148:92/api/v1/Common/CloseAllSessions"

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
    url = "http://10.255.201.148:93/api/v1/Token/LoginUser"

    payload = json.dumps({
        "userID": "MN1519",
        "password": "New@1234",
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
