import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')

from ServerMain import *

#This request POST for Creation of step1 Offre
@app.post("/company/Step1Offre")
async def Step1Offre(request: Request):
    req = await request.json()

    dataSend = req['dataSend']
    idOffre = dataSend['idOffre']
    lfN = dataSend['lfN']
    nbHWOC = dataSend['nbHWOC']
    nbHWOS = dataSend['nbHWOS']
    valueSend = req['valueSend']
    phoneNumberOfUser = req['phoneNumber']

    resutFunction1 = insertIntoGlobalOffre(idOffre,phoneNumberOfUser)
    resutFunction2 = insertIntoOffresStep1(idOffre)
    resutFunction3 = insertIntoworkCGOffre(idOffre,lfN,nbHWOC,nbHWOS,valueSend,phoneNumberOfUser)

    resutFunction = 1

    return {
        "resutFunction" : resutFunction
    }

#This request POST for GET a offre for step1 section by an ID
@app.post("/company/getOffreById")
async def getOffreById(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunctionGIFWCGO = getInformationFromWorkCGOffre(idOffreSend,phoneNumber)

    return{
        "resutFunctionGIFWCGO" : resutFunctionGIFWCGO
    }

#This request POST for update the a offre for step 1 by an Id worker
@app.post("/company/updateInformationOfStep1")
async def updateInformationOfStep1(request: Request):
    req = await request.json()

    workerNameGlobaleSend = req['workerNameGlobaleSend']
    FGSend = req['FGSend']
    nbWorkOnCompanySend = req['nbWorkOnCompanySend']
    nbWorkOnSiteSend = req['nbWorkOnSiteSend']
    idWorkerNameSend = req['idWorkerNameSend']
    idOffreSendGlobaleSend = req['idOffreSendGlobaleSend']

    resutFunction = updateInformationOfStep1ToDB(FGSend,nbWorkOnCompanySend,nbWorkOnSiteSend,idWorkerNameSend,idOffreSendGlobaleSend)

    return {
        "resutFunction" : resutFunction
    }
    
#This request POST for delete an worker from an an offre for step1
@app.post("/company/deleteAnWorkerFromOffre")
async def deleteAnWorkerFromOffre(request: Request):
    req = await request.json()

    workerProfileSend = req['workerProfileSend']
    idOffreSendGlobaleSend = req['idOffreSendGlobaleSend']
    phoneNumber = req['phoneNumber']
    resutFunction = deleteAnWorkerFromOffreUsingDB(workerProfileSend,idOffreSendGlobaleSend,phoneNumber)
    resultFunction = calculPhase1OffreFromDB(idOffreSendGlobaleSend)

    return {
        "resutFunction" : resutFunction
    }

#This request POST for calculate the step one of offre for step 1
@app.post("/company/calculPhase1Offre")
async def calculPhase1Offre(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction1 = calculPhase1OffreFromDB(idOffreSend)
    resutFunction = getInformationFromOffresStep1(idOffreSend,phoneNumber)

    return {
        "resutFunction" : resutFunction
    }