import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')

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
    # print(resutFunction)

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
    addressLocal = req['addressLocal']
    logoCompanySend = req['logoCompanySend']
    addressCompanySend = req['addressCompanySend']
    taxRegNumSend = req['taxRegNumSend']

    resutFunction = EditInformationOfCompanyDB(phoneNumber,nameCompanySend,telePhoneSend,cellNumberSend,webSiteSend,firstNameProfileSend,lastNameProfileSend,emailUserCompanySend,citySend,zipCodeSend,addressLocal,logoCompanySend,addressCompanySend,taxRegNumSend)

    return {
        "resutFunction" : resutFunction
    }

#This request post for get all the informations of companys user
@app.post("/company/getAllNesscaryInformation")
async def getAllNesscaryInformation(request: Request):
    req = await request.json()
    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction = getAllNesscaryInformationDB(idOffreSend,phoneNumber)

    return {
        "resutFunctionOFCompanies" : resutFunction[0],
        "resutFunctionForStep1": resutFunction[1],
        "resutFunctionForStep2": resutFunction[2],
        "resutFunctionForStep3": resutFunction[3],
        "resutFunctionForStep4": resutFunction[4],
        "resutFunctionForGlobalOffre": resutFunction[5],

    }
    