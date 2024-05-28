import requests
auth_url = "https://sandbox.analytics.metropol.co.ug/api/v3/authenticate?grant_type=client_credentials"
nimble_url = "http://10.255.201.148:93/api/v1/Token/LoginUser"
#report_url ="https://api.metropol.co.ug:5557/api/v1/reports/credit_report/pdf?report_reference_number"
report_url = "https://sandbox.analytics.metropol.co.ug/api/v3/report/pdf?reference"
#identity_path = "/Users/musembya/PycharmProjects/AutomationApps/Metropol/static/images"
#identity_path = "C:/Users/allan.musembya/PycharmProjects/AutomationApps/Metropol/static/images"
identity_path ="/home/ftb-uat/AutomationApps/Metropol/static/images"
nimble_token = "http://10.255.201.148:93/api/v1/Token/LoginUser"
nimble_close = "http://10.255.201.148:92/api/v1/Common/CloseAllSessions"
generate_rpt_url = "https://sandbox.analytics.metropol.co.ug/api/v3/report"

