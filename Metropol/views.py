import json

import requests
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import base64
import os.path
from django.core.files.base import ContentFile

from .MetropolForm import *
from .api_urls import nimble_url, auth_url, report_url, identity_path

requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)
auth_url = auth_url


def getCoreApp(request):
    return render(request, 'metropol/core_applications.html', {})


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
                return redirect("getCap")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name='metropol/login.html', context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return HttpResponseRedirect('/Metropol/')


def getNimbleToken():
    url = nimble_url
    
    payload = json.dumps({
        "userID": "DK0657",
        "password": "New@1234",
        "branchID": "206",
        "systemID": ""
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    res = response.json()


def getBearerToken():
    url = auth_url
    payload = ""
    headers = {
        'Authorization': 'Basic VFBsZWNQN1ZkYmxmNHl4cnJPelYxcVZvbWNPTUhzTGc6VFBXTkFKRTN2b3Q5QXgzMw=='
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    res = response.json()
    return res['access_token']


@login_required(login_url='/Metropol/')
def addCap(request):
    url = "https://api.metropol.co.ug:5557/api/v1/cap"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getBearerToken()}'
    }
    
    form = CapForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            partner_bou_code = form['partner_bou_code'].value()
            partner_branch_code = form['partner_branch_code'].value()
            application_date = form['application_date'].value()
            partner_reference = form['partner_reference'].value()
            phone = form['phone'].value()
            currency_code = form['currency_code'].value()
            application_amount = form['application_amount'].value()
            application_duration = form['application_duration'].value()
            product_type_code = form['product_type_code'].value()
            application_type_code = form['application_type_code'].value()
            generate_report = form['generate_report'].value()
            identity_id_number = form['identity_id_number'].value()
            identity_type_code = form['identity_type_code'].value()
            
            borrower_list = [{"identity_id_number": identity_id_number,
                              "identity_type_code": identity_type_code,
                              "country_code": "UG"}]
            
            payload = json.dumps({
                "partner_bou_code": partner_bou_code,
                "partner_branch_code": partner_branch_code,
                "application_date": application_date,
                "partner_reference": partner_reference,
                "borrowers": borrower_list,
                "phone": phone,
                "currency_code": currency_code,
                "application_amount": application_amount,
                "application_duration": application_duration,
                "product_type_code": product_type_code,
                "application_type_code": application_type_code,
                "generate_report": generate_report
            }, indent=4)
            response = requests.request("POST", url, headers=headers, data=payload)
            # print(response.text)
            res = response.json()
            res_message = res['api_code_description']
            form.save()
            messages.success(request, f'{res_message}')
            return HttpResponseRedirect('/Metropol/addCap')
    return render(request, 'metropol/create_cap.html', {'form': form})


@login_required(login_url='/Metropol/')
def getCap(request):
    cap = Cap.objects.all().order_by('-id')
    return render(request, 'metropol/cap.html', {'cap': cap})


@login_required(login_url='/Metropol/')
def getIdentityDetails(request):
    obj = IdentityDetail.objects.all().order_by('-id')
    return render(request, 'metropol/identity_detail.html', {'obj': obj})


@login_required(login_url='/Metropol/')
def updateCap(request, id):
    sec = Cap.objects.get(id=id)
    url = "https://api.metropol.co.ug:5557/api/v1/cap"
    
    if request.method == 'POST':
        form = UpdateCapForm(request.POST, instance=sec)
        if form.is_valid():
            partner_reference = form['partner_reference'].value()
            partner_bou_code = form['partner_bou_code'].value()
            application_status_date = form['application_status_date'].value()
            application_status_code = form['application_status_code'].value()
            approved_duration = form['application_status_code'].value()
            amount_approved = form['application_status_code'].value()
            application_rejection_reason = form['application_status_code'].value()
            application_rejection_reason_code = form['application_status_code'].value()
            application_status = form['application_status'].value()
            
            payload = json.dumps({
                "amount_approved": amount_approved,
                "application_rejection_reason": application_rejection_reason,
                "application_rejection_reason_code": application_rejection_reason_code,
                "application_status": application_status,
                "application_status_code": application_status_code,
                "application_status_date": application_status_date,
                "approved_duration": approved_duration,
                "partner_bou_code": partner_bou_code,
                "partner_reference": partner_reference
            }, indent=4)
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {getBearerToken()}'
            }
            
            response = requests.request("PUT", url, headers=headers, data=payload)
            res = response.json()
            res_message = res['api_code_description']
            form.save()
            messages.success(request, f'{res_message}')
            return HttpResponseRedirect('/Metropol/getCap')
    else:
        form = UpdateCapForm(instance=sec)
    return render(request, 'metropol/update_cap.html', {'form': form})


def pdfReport(report_reference_number):
    url = f"{report_url}={report_reference_number}"
    payload = {}
    headers = {
        'Content-Type': 'application/pdf',
        'Authorization': f'Bearer {getBearerToken()}'
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    return response


@login_required(login_url='/Metropol/')
def generateReport(request):
    url = "https://api.metropol.co.ug:5557/api/v1/reports/generate_report"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {getBearerToken()}'
    }
    form = ReportForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            identity_id_number = form['identity_number'].value()
            identity_type_id = form['identity_type'].value()
            report_pull_reason_id = form['report_pull_reason'].value()
            report_type_id = form['report_type'].value()
            
            payload = json.dumps({
                "identity_id_number": identity_id_number,
                "identity_type_id": identity_type_id,
                "report_pull_reason_id": report_pull_reason_id,
                "report_type_id": report_type_id
            }, indent=4)
            
            response = requests.request("POST", url, headers=headers, data=payload)
            res = response.json()
            report_reference_number = res['data']['report_reference_number']
            res = pdfReport(report_reference_number)
            generated_rpt = HttpResponse(res.content, content_type='application/pdf')
            return generated_rpt
    
    return render(request, 'metropol/generate_report.html', {'form': form})


def getId(id):
    if id is None:
        return 'NA'
    else:
        return id


@login_required(login_url='/Metropol/')
def Identity(request):
    form = IdentityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            identity_id_number = form['identity_number'].value()
            identity_type_id = form['identity_type'].value()
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {getBearerToken()}'
            }
            url = f"https://api.metropol.co.ug:5557/api/v1/identity/verify?identity_number={identity_id_number}&identity_type_id={identity_type_id}"
            
            payload = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            res = response.json()
            
            # image = base64.b64decode(res['data']['identity_info']['image'], validate=True)
            
            img = res['data']['identity_info']['image']
            save_path = identity_path
            name_of_file = res['data']['identity_number']
            file_name = name_of_file + ".jpg"
            completeName = os.path.join(save_path, file_name)
            
            imgdata = base64.b64decode(img)
            image = open(completeName, "wb")
            image.write(imgdata)
            image.close()
            
            
            getIds = getId(res["data"]["other_identities"][0]["number"])
            
            if identity_type_id == '10':
                passed_data = {
                    "identity_number": res['data']['identity_number'],
                    "fcs": getIds,
                    "surname": res['data']['identity_info']['surname'],
                    "forename1": res['data']['identity_info']['forename1'],
                    "forename2": res['data']['identity_info']['forename2'],
                    "forename3": res['data']['identity_info']['forename3'],
                    "date_of_birth": res['data']['identity_info']['date_of_birth'],
                    "gender": res['data']['identity_info']['gender'],
                    "image": file_name
                }
                
                res_message = res['api_code_description']
                messages.success(request, f'{res_message}')
                obj = IdentityDetail.objects.create(**passed_data)
                obj.save()
                
                return HttpResponseRedirect('/Metropol/getIdentityDetails')
            else:
                passed_info = {
                    "identity_number": getIds,
                    "fcs": res['data']['identity_number'],
                    "surname": res['data']['identity_info']['surname'],
                    "forename1": res['data']['identity_info']['forename1'],
                    "forename2": res['data']['identity_info']['forename2'],
                    "forename3": res['data']['identity_info']['forename3'],
                    "date_of_birth": res['data']['identity_info']['date_of_birth'],
                    "gender": res['data']['identity_info']['gender'],
                    "image": file_name
                }
                print('hmmmmmmm4')
                
                res_message = res['api_code_description']
                messages.success(request, f'{res_message}')
                obj = IdentityDetail.objects.create(**passed_info)
                obj.save()
                
                return HttpResponseRedirect('/Metropol/getIdentityDetails')
    
    return render(request, 'metropol/generate_identity.html', {'form': form})


@login_required(login_url='/Metropol/')
def addBranch(request):
    form = BranchCodeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully added a branch.")
            return HttpResponseRedirect('/Metropol/addBranch')
    return render(request, 'metropol/addBranch.html', {'form': form})


@login_required(login_url='/Metropol/')
def addBoucode(request):
    form = BouCodeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully added code.")
            return HttpResponseRedirect('/Metropol/addBoucode')
    return render(request, 'metropol/addBouCode.html', {'form': form})


@login_required(login_url='/Metropol/')
def getBranches(request):
    branch = BranchCode.objects.all()
    return render(request, 'metropol/branches.html', {'branch': branch})
