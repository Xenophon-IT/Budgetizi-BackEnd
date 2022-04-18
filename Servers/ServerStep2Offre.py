import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Partie-BackEnd\Servers')

from ServerMain import *

#This request POST for Creation of step 2 Offre
@app.post("/company/Step2Offre")
async def Step2Offre(request: Request):
    req = await request.json()

    dataSend = req['dataSend']
    idOffre = dataSend['idOffre']
    fullName = dataSend['fullName']
    nbHWOC = dataSend['nbHWOC']
    nbHWOS = dataSend['nbHWOS']
    valueSend = req['valueSend']
    phoneNumberOfUser = req['phoneNumber']

    print(fullName)
    resutFunction1 = checkIntoGlobalOffre(idOffre,phoneNumberOfUser)
    
    if(resutFunction1 == 1):
        #Not now the next script
        resutFunction2 = insertIntoOffresStep2(idOffre)
        resutFunction3 = insertIntoworkCGOffreStep2(idOffre,fullName,nbHWOC,nbHWOS,valueSend,phoneNumberOfUser)
        resutFunction = 1
    else:
        resutFunction = 0

    return {
        "resutFunction" : resutFunction
    }

#This request POST for GET a offre for step 2 section by an ID
@app.post("/company/getOffreStep2ById")
async def getOffreStep2ById(request: Request):
    print("Hello !!")
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    print(idOffreSend,phoneNumber)
    resutFunctionGIFWCGO = getInformationFromWorkCGOffreStep2(idOffreSend,phoneNumber)

    return{
        "resutFunctionGIFWCGO" : resutFunctionGIFWCGO
    }

#This request POST for update the a offre for step 2 by an Id worker
@app.post("/company/updateInformationOfStep2")
async def updateInformationOfStep2(request: Request):
    req = await request.json()

    nbWorkOnCompanySend = req['nbWorkOnCompanySend']
    nbWorkOnSiteSend = req['nbWorkOnSiteSend']
    FGSend = req['FGSend']
    workerNameGlobaleSend = req['workerNameGlobaleSend']
    idOffreSendGlobaleSend = req['idOffreSendGlobaleSend']
    idWorkerGlobaleSend = req['idWorkerGlobaleSend']

    resutFunction = updateInformationOfStep2ToDB(FGSend,nbWorkOnCompanySend,nbWorkOnSiteSend,idWorkerGlobaleSend,idOffreSendGlobaleSend)

    return {
        "resutFunction" : resutFunction
    }

#This request POST for delete an worker from an an offre for step2
@app.post("/company/deleteAnWorkerFromOffreStep2")
async def deleteAnWorkerFromOffre(request: Request):
    req = await request.json()

    workerProfileSend = req['workerProfileSend']
    idOffreSendGlobaleSend = req['idOffreSendGlobaleSend']
    phoneNumberOfUserSend = req['phoneNumber']
    resutFunction = deleteAnWorkerFromOffreStep2UsingDB(workerProfileSend,idOffreSendGlobaleSend,phoneNumberOfUserSend)
    resultFunction = calculPhase2OffreFromDB(idOffreSendGlobaleSend)

    return {
        "resutFunction" : resutFunction
    }

#This request POST for calculate the step one of offre for step2
@app.post("/company/calculPhase2Offre")
async def calculPhase2Offre(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']
    print("ddddddddddddddddddddddd")
    print(idOffreSend, phoneNumber)

    resutFunction1 = calculPhase2OffreFromDB(idOffreSend)
    resutFunction = getInformationFromOffresStep2(idOffreSend,phoneNumber)

    return {
        "resutFunction" : resutFunction
    }