import requests
auth_url = "https://api.metropol.co.ug:5557/api/v1/authenticate?grant_type=client_credentials"
nimble_url = "http://10.255.201.148:93/api/v1/Token/LoginUser"
report_url ="https://api.metropol.co.ug:5557/api/v1/reports/credit_report/pdf?report_reference_number"
#identity_path = "/Users/musembya/PycharmProjects/AutomationApps/Metropol/static/images"
identity_path = "C:/Users/allan.musembya/PycharmProjects/AutomationApps/Metropol/static/images"
JWT = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik1OMTUxOSIsIkJyYW5jaElEIjoiMzA3IiwiU3lzdGVtIjoiZWVlIiwiVG9rZW5UeXBlIjoiQVQiLCJuYmYiOjE3MDU0OTA1NDIsImV4cCI6MTcwNjAzMDU0MiwiaWF0IjoxNzA1NDkwNTQyLCJpc3MiOiJodHRwOi8vMTAuMjU1LjIwMS4xNDg6OTMvIiwiYXVkIjoiaHR0cHM6Ly9uaW1ibGUuZmluYW5jZXRydXN0LmNvLnVnOjkxLyJ9.ZmMSsVD75E2V0X-WWAZZ4EJS2fcGbuN3eS2FlCGHmLsoLGEXF7dt8PLVqbp99mzi7fjZKbruzk1PUBYykaqgyQ"