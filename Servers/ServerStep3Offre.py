import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')

from ServerMain import *

#This request POST for Creation of step 3 Offre
@app.post("/company/Step3Offre")
async def Step3Offre(request: Request):
    req = await request.json()
    dataSend = req['dataSend']
    idOffre = dataSend['idOffre']
    fullName = dataSend['fullName']
    nbHWOC = dataSend['nbHWOC']
    nbHWOS = dataSend['nbHWOS']
    valueSend = req['valueSend']
    phoneNumber = req['phoneNumber']

    resutFunction1 = checkIntoGlobalOffre(idOffre,phoneNumber)

    # print(resutFunction1)
    
    if(resutFunction1 == 1):
        #Not now the next script
        resutFunction2 = insertIntoOffresStep3(idOffre)
        resutFunction3 = insertIntoworkCGOffreStep3(idOffre,fullName,nbHWOC,nbHWOS,valueSend,phoneNumber)
        resutFunction = 1
    else:
        resutFunction = 0

    return {
        "resutFunction" : resutFunction
    }

#This request POST for GET a offre for step 3 section by an ID
@app.post("/company/getOffreStep3ById")
async def getOffreStep3ById(request: Request):
    print("Hello !!")
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    print(idOffreSend,phoneNumber)
    resutFunctionGIFWCGO = getInformationFromWorkCGOffreStep3(idOffreSend,phoneNumber)

    return{
        "resutFunctionGIFWCGO" : resutFunctionGIFWCGO
    }


#This request POST for update the a offre for step 2 by an Id worker
@app.post("/company/updateInformationOfStep3")
async def updateInformationOfStep3(request: Request):
    req = await request.json()

    nbWorkOnCompanySend = req['nbWorkOnCompanySend']
    nbWorkOnSiteSend = req['nbWorkOnSiteSend']
    FGSend = req['FGSend']
    workerNameGlobaleSend = req['workerNameGlobaleSend']
    idOffreSendGlobaleSend = req['idOffreSendGlobaleSend']
    idWorkerGlobaleSend = req['idWorkerGlobaleSend']

    print(nbWorkOnCompanySend)
    print(nbWorkOnSiteSend)
    print(FGSend)
    print(workerNameGlobaleSend)
    print(idOffreSendGlobaleSend)
    print(idWorkerGlobaleSend)

    resutFunction = updateInformationOfStep3ToDB(workerNameGlobaleSend,FGSend,nbWorkOnCompanySend,nbWorkOnSiteSend,idWorkerGlobaleSend,idOffreSendGlobaleSend)

    return {
        "resutFunction" : resutFunction
    }


#This request POST for delete an worker from an an offre for step2
@app.post("/company/deleteAnWorkerFromOffreStep3")
async def deleteAnWorkerFromOffre(request: Request):
    req = await request.json()

    workerProfileSend = req['workerProfileSend']
    idOffreSendGlobaleSend = req['idOffreSendGlobaleSend']
    phoneNumber = req['phoneNumber']
    resutFunction = deleteAnWorkerFromOffreStep3UsingDB(workerProfileSend,idOffreSendGlobaleSend,phoneNumber)
    resultFunction = calculPhase3OffreFromDB(idOffreSendGlobaleSend)

    return {
        "resutFunction" : resutFunction
    }

#This request POST for calculate the step one of offre for step2
@app.post("/company/calculPhase3Offre")
async def calculPhase3Offre(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    print(idOffreSend)

    resutFunction1 = calculPhase3OffreFromDB(idOffreSend)
    resutFunction = getInformationFromOffresStep3(idOffreSend,phoneNumber)

    return {
        "resutFunction" : resutFunction
    }
