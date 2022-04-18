import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Partie-BackEnd\Servers')

from ServerMain import *

#This request post for signup Client
@app.post("/company/signupCompany")
async def signupCompany(request: Request):
    req = await request.json()
    dataSend = req['dataSend']
    nameCompany = dataSend["nameCompany"]
    companAct = dataSend["companAct"]
    country = dataSend["country"]
    numberWorker = dataSend["numberWorker"]
    currency = dataSend["currency"]
    phoneNumber = dataSend["phoneUser"]
    
    resultSignUpCompany = sginUpCompany(nameCompany,companAct,country,currency,phoneNumber)

    return {
        "resultSignUpCompany": resultSignUpCompany # 0: the name of company is use it | 1: ok ok
    }


#This request post for get all the informations of companys user
@app.post("/company/getInformationFromCompanyDB")
async def getInformationFromCompanyDB(request: Request):
    req = await request.json()
    phoneNumber = req['phoneNumber']

    resutFunction = getInformationCompanyDB(phoneNumber)
    print(resutFunction)

    return {
        "resutFunction" : resutFunction
    }

#This request post for edit the informations of companys user
@app.post("/company/EditInformationOfCompany")
async def EditInformationOfCompany(request: Request):
    req = await request.json()
    phoneNumber = req['phoneNumber']
    nameCompanySend = req['nameCompanySend']
    telePhoneSend = req['telePhoneSend']
    cellNumberSend = req['cellNumberSend']
    webSiteSend = req['webSiteSend']
    firstNameProfileSend = req['firstNameProfileSend']
    lastNameProfileSend = req['lastNameProfileSend']
    emailUserCompanySend = req['emailUserCompanySend']
    citySend = req['citySend']
    zipCodeSend = req['zipCodeSend']
    logoCompanySend = req['logoCompanySend']
    addressCompanySend = req['addressCompanySend']
    taxRegNumSend = req['taxRegNumSend']

    resutFunction = EditInformationOfCompanyDB(phoneNumber,nameCompanySend,telePhoneSend,cellNumberSend,webSiteSend,firstNameProfileSend,lastNameProfileSend,emailUserCompanySend,citySend,zipCodeSend,logoCompanySend,addressCompanySend,taxRegNumSend)

    return {
        "resutFunction" : resutFunction
    }