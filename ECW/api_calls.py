import requests
import time
from enc import signMsg, generate_random_challenge
import  xmltodict
import json


def getsigningcertificate():
    random_challenge = generate_random_challenge()
    time_stamp = round(time.time())
    final_str = f'{random_challenge};{time_stamp}'
    values_to_beSigned = f'{random_challenge};{time_stamp};'.encode('utf-8')

    x = signMsg(values_to_beSigned)
    yy = f'{final_str};{x}'

    url = "https://212.88.125.201:8027/banks/getsigningcertificate"
    cert_path = 'E:/ftb_uat_mtls/ftb_uat_mtls.crt'
    key_path = 'E:/ftb_uat_mtls/fintrust_signing_uat.key'

    payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<ns0:getsigningcertificaterequest xmlns:ns0=\"http://www.ericsson.com/em/emm/messagesigning/v1_0\"/>"
    headers = {
        'Content-Type': 'text/xml',
        'X-Signature': yy,
        'X-Original-Signer': 'ID:FTBbank/USER',
        'Authorization': 'Basic RlRCYmFuazpBQmMxMjM0NTYh'
    }

    response = requests.request("POST", url, headers=headers, data=payload, cert=(cert_path, key_path), verify=False)
    #print(response.text)
    print(json.dumps(xmltodict.parse(response.text,process_namespaces=False), indent=4))


def getAccontHolderInfo(phone_nmber):
    random_challenge = generate_random_challenge()
    time_stamp = round(time.time())
    final_str = f'{random_challenge};{time_stamp}'
    values_to_beSigned = f'{random_challenge};{time_stamp};'.encode('utf-8')

    x = signMsg(values_to_beSigned)
    yy = f'{final_str};{x}'

    url = "https://212.88.125.201:8027/banks/getaccountholderinfo"
    cert_path = 'E:/ftb_uat_mtls/ftb_uat_mtls.crt'
    key_path = 'E:/ftb_uat_mtls/fintrust_signing_uat.key'

    payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<ns0:getaccountholderinforequest xmlns:ns0=\"http://www.ericsson.com/em/emm/provisioning/v1_2\">\r\n    <identity>ID:{phone_nmber}/MSISDN</identity>\r\n</ns0:getaccountholderinforequest>"
    headers = {
        'Content-Type': 'text/xml',
        'X-Signature': yy,
        'X-Original-Signer': 'ID:FTBbank/USER',
        'Authorization': 'Basic RlRCYmFuazpBQmMxMjM0NTYh'
    }

    response = requests.request("POST", url, headers=headers, data=payload, cert=(cert_path, key_path), verify=False)

    res = json.dumps(xmltodict.parse(response.text,process_namespaces=False), indent=4)
    print(res)

    #firstname = res["ns5:getaccountholderinforesponse"]["accountholderbasicinfo"]["firstname"]
    #print(firstname)




#getsigningcertificate()
phone_nmber ='256789999981'
getAccontHolderInfo(phone_nmber)
