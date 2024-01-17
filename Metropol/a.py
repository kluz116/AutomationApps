import json
null = None
true = "True"
false = "False"
res = {
    "Status": "000",
    "Message": "Successful",
    "SystemMessage": null,
    "MessageID": null,
    "LoanWorkflowStages": [
        {
            "WFAdvStageID": "10APPL",
            "StageOrder": 1,
            "IsSystem": true,
            "WorkflowURL": "",
            "Description": "Application",
            "StageDuration": "2023-07-01T10:27:00",
            "EstimatedCompletionDate": "2023-07-01T10:27:00",
            "CompletionStatus": "ONTRACK",
            "WorkflowDays": 0
        },
        {
            "WFAdvStageID": "16CRB",
            "StageOrder": 2,
            "IsSystem": true,
            "WorkflowURL": "/CRBEnquiry/Index",
            "Description": "CRB Enquiry",
            "StageDuration": "2023-07-01T10:27:00",
            "EstimatedCompletionDate": "2023-07-01T10:27:00",
            "CompletionStatus": "ONTRACK",
            "WorkflowDays": 0
        },
        {
            "WFAdvStageID": "30SANC",
            "StageOrder": 3,
            "IsSystem": true,
            "WorkflowURL": "/LoanSanction/index",
            "Description": "Sanction",
            "StageDuration": "2023-07-01T10:27:00",
            "EstimatedCompletionDate": "2023-07-01T10:27:00",
            "CompletionStatus": "ONTRACK",
            "WorkflowDays": 0
        },
        {
            "WFAdvStageID": "60DISB",
            "StageOrder": 4,
            "IsSystem": true,
            "WorkflowURL": "/LoanDisbursement/index",
            "Description": "Disbursement ",
            "StageDuration": null,
            "EstimatedCompletionDate": "2023-07-01T10:27:00",
            "CompletionStatus": "ONTRACK",
            "WorkflowDays": 0
        }
    ],
    "CustomerRestriction": [
        {
            "CustomerRestrictionID": "G"
        },
        {
            "CustomerRestrictionID": "I"
        }
    ],
    "LoanWorkflowStagesChecklist": null,
    "AdvanceRateMenuDetail": [
        {
            "AmountSlabFrom": 50000.0,
            "AmountSlabTo": 1000000.0,
            "TermFrom": 1,
            "TermTo": 3,
            "EffectiveRate": 60.0,
            "ProductEffectiveRate": 60.0,
            "MarkingRate": 0.0,
            "Sign": "+"
        }
    ],
    "ClientDetail": [
        {
            "ClientBranchID": "",
            "ClientTypeID": "I",
            "ClientName": "IVAN CHEMONGES",
            "Address1": "MUTUNGO",
            "Address2": "NAKAWA",
            "City": "Kampala",
            "Country": "UGANDA",
            "Phone1": "0773138828,0701421351",
            "Mobile": "0773138828",
            "Email": "",
            "Gender": "MALE",
            "IsDOBGiven": true,
            "DateOfBirth": "1998-06-15T00:00:00",
            "Age": 0,
            "AgeAsOn": "1900-01-01T00:00:00"
        }
    ],
    "LoanApplication": [
        {
            "OurBranchID": "211",
            "BranchName": "Kitintale Branch",
            "WFAdvTypeID": "WF28",
            "IsGracePeriod": false,
            "GracePeriod": null,
            "WFAdvType": "Loan Ku Simu",
            "ClientID": "00000295167",
            "IsExistingClient": true,
            "ClientBranchID": "211",
            "ClientBranchName": "Kitintale Branch",
            "TempClientID": null,
            "ApplicationID": "211012131",
            "ApplicationDate": "2023-06-30T00:00:00",
            "ProductID": "505",
            "ProductName": "Trust Mobile Loans",
            "RepaymentAccountID": "211200006824",
            "RepaymentAccountName": "IVAN CHEMONGES",
            "PurposeCodeID": "014",
            "BusinessLineID": "901",
            "CreditOfficerID": "614",
            "SalesOfficerID": "",
            "SalesOfficerName": "",
            "IsSystemWorkflow": true,
            "DeviationID": "",
            "IsDeviationSystem": false,
            "DonorID": "",
            "DonorName": "",
            "CreditOfficerName": "LOAN ON PHONE",
            "LoanAmount": 450000.0,
            "LoanTerm": 3,
            "LoanPeriodID": "M",
            "LoanPeriod": "Month(s)",
            "DisbursementDate": "2023-06-30T00:00:00",
            "AccountClassID": "CL505",
            "AccountClassName": "Loan Ku Simu Class",
            "FileNumber": null,
            "WFAdvStageID": "60DISB",
            "WFAppStatusID": "DIS",
            "Penalty": 0.0,
            "WFAppStatus": "Disbursed",
            "AllowEdit": false,
            "DataEditable": false,
            "CurrencyID": "UGX",
            "MinLoanAmount": 100000.0,
            "MaxLoanAmount": 1000000.0,
            "MinLoanTerm": 1,
            "MaxLoanTerm": 3,
            "GuarantorTypeID": "",
            "LoanTypeID": "N",
            "LoanType": "Normal",
            "IsLoanSanctioned": true,
            "IsLoanAppraised": false,
            "CreatedBy": "LOP001",
            "CreatedOn": "2023-07-01T10:27:00",
            "ModifiedBy": null,
            "ModifiedOn": null,
            "InterestRate": 60.0,
            "VerifiedBy": "",
            "UpdateCount": 2,
            "CommissionRate": 0.0,
            "TaxRate": 0.0,
            "EffectiveRate": 60.0,
            "GroupID": "",
            "GroupName": "",
            "SubGroupID": "",
            "SpecialLoanScheme": "MFI505",
            "MainProductID": "505",
            "MainProductDescription": "Trust Mobile Loans",
            "LoanAgreementConfirmation": null,
            "LoanAccountID": "211505000341",
            "AppraisalDate": "2023-06-30T00:00:00",
            "SanctionDate": "1900-01-01T00:00:00",
            "BranchID": "211",
            "SubSectorID": "",
            "SubSubSectorID": "",
            "SubSubSubSectorID": "",
            "PartialAmountPending": 0.0,
            "RepaymentFrequencyID": null,
            "InterestGracePeriod": null,
            "ScheduleFeeGracePeriod": null,
            "MobilisedBy": "",
            "MobilisedByName": ""
        }
    ]
}

ClientID= res["LoanApplication"][0]["ClientID"]
application_date = res["LoanApplication"][0]["ApplicationDate"]
partner_reference = res["LoanApplication"][0]["ApplicationID"]
phone = res["ClientDetail"][0]["Mobile"]
currency_code =res["LoanApplication"][0]["CurrencyID"]
application_amount = res["LoanApplication"][0]["LoanAmount"]
application_duration = res["LoanApplication"][0]["LoanTerm"]




okay = {
    "status": [
        {
            "operatorID": "",
            "eventID": 0,
            "newData": "",
            "createdOn": "",
            "updateCount": 0
        }
    ],
    "client": [
        {
            "clientID": "00000121006",
            "name": "ALLAN MUSEMBYA",
            "clientTypeID": "E",
            "addressTypeID": "R",
            "address1": "KAMWOKYA",
            "address2": "",
            "cityID": "03",
            "city": "Kampala",
            "countryID": "UG",
            "countryName": "UGANDA",
            "zipcode": "256",
            "phone1": "0771602851",
            "phone2": "0755947634",
            "mobile": "0771602851",
            "fax": "1.30 :Low Risk",
            "email": "",
            "photoID": 1226520,
            "signID": 1226523,
            "bioID": 1228841,
            "bioID1": 1228841,
            "iD1": "",
            "iD2": "WKC",
            "canSendGreetings": true,
            "canSendOurSpecialOffers": true,
            "canSendAssociateSpecialOffer": true,
            "eStatementRequired": false,
            "mobileAlertRequired": true,
            "noOfEmployee": 0,
            "businessLineID": "1002",
            "businessOwnershipID": null,
            "businessStartedYear": null,
            "openedBy": "SK0559",
            "openedByName": null,
            "openedDate": "2008-04-22T00:00:00",
            "closeDate": null,
            "clientStatusID": "A",
            "clientStatus": "Active",
            "comments": null,
            "isExpired": false,
            "createdBy": "SK0559",
            "createdOn": "2018-07-09T16:22:00",
            "modifiedBy": "YO1739",
            "modifiedOn": "2023-03-28T08:40:00",
            "supervisedBy": "EL1013",
            "supervisedOn": "2018-07-09T00:00:00",
            "updateCount": 2,
            "clientClassID": "E",
            "totalLimits": 0.0000,
            "base": null,
            "relationshipManagerID": "052001061RM",
            "introducerClientID": ""
        }
    ],
    "clientQuery": [
        {
            "titleID": "MR",
            "firstName": "ALLAN",
            "lastName": "MUSEMBYA",
            "middleName": null,
            "genderID": "M",
            "nationalityID": "UG",
            "isDOBGiven": true,
            "dateOfBirth": "1990-01-22T00:00:00",
            "age": null,
            "ageAsOn": null,
            "bloodGroupID": "B -",
            "canDonateBlood": false,
            "residentID": "R",
            "literacyLevelID": "01",
            "passportNo": "CM90007100FKWA",
            "passportIssuedCityID": "Govt.",
            "passportExpiryDate": "2026-02-02T00:00:00",
            "maritalStatusID": "0",
            "spouseID": null,
            "nextOfKinID": null,
            "numberOfHouseMembers": 0,
            "numberOfChildren": 0,
            "numberOfDependents": 0,
            "isSalaried": true,
            "occupationID": "14",
            "designationID": "50",
            "companyTypeID": "0",
            "employerName": "FTB",
            "employerCode": null,
            "workingSince": "2018-07-07T00:00:00",
            "salary": 3500000.0000,
            "familyIncome": 0.0000,
            "otherIncome": 0.0000,
            "rentExpense": 0.0000,
            "otherExpenses": 1000000.0000,
            "workPermitNo": null,
            "identificationTypeID": "ID",
            "introducerClientID": null
        }
    ],
    "roleDetails": [
        {
            "clientRoleID": "A",
            "roleExist": 1
        }
    ]
}

print(okay["clientQuery"][0]["passportNo"])