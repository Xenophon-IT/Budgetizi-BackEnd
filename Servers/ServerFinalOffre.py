import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')
from ServerMain import *

#This request POST for calculate the step one of offre for totality
@app.post("/company/getAllInformationOfAnWorker")
async def getAllInformationOfAnWorker(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction = checkIntoGlobalOffre(idOffreSend,phoneNumber)
    if(resutFunction == 1):
        print('We found it !!!!')
        resutFunction1 = getAllInformationOfAnWorkerFromDB(idOffreSend,phoneNumber)
        resutFunction2 = getInformationFromOffresStep1(idOffreSend, phoneNumber)
        resutFunction3 = getAllInformationOfAnWorkerFromDBForStep2(idOffreSend,phoneNumber)
        resutFunction4 = getInformationFromOffresStep2(idOffreSend, phoneNumber)
        resutFunction5 = getAllInformationOfAnWorkerFromDBForStep3(idOffreSend,phoneNumber)
        resutFunction6 = getInformationFromOffresStep3(idOffreSend, phoneNumber)
        resutFunction7 = offreFinaleCalculDB(idOffreSend)
        resutFunction8 = getInformationOffreFinale(idOffreSend)

        return {
            "resutFunction" : resutFunction,
            "resutFunction1" : resutFunction1,
            "resutFunction2" : resutFunction2,
            "resutFunction3" : resutFunction3,
            "resutFunction4" : resutFunction4,
            "resutFunction5" : resutFunction5,
            "resutFunction6" : resutFunction6,
            "resutFunction8" : resutFunction8
        }
    else:
        print("Not yet")
        resutFunction = 0

    return {
        "resutFunction" : resutFunction,
    }


#This request POST for calculate the step one of offre for totality
@app.post("/company/getAllInformationForStep1")
async def getAllInformationForStep1(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction1 = getAllInformationOfAnWorkerFromDB(idOffreSend,phoneNumber)
    resutFunction2 = getInformationFromOffresStep1(idOffreSend, phoneNumber)

    return {
        "resutFunction1" : resutFunction1,
        "resutFunction2" : resutFunction2
    }


#This request POST for calculate the step one of offre for totality
@app.post("/company/getAllInformationForStep2")
async def getAllInformationForStep2(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction3 = getAllInformationOfAnWorkerFromDBForStep2(idOffreSend,phoneNumber)
    resutFunction4 = getInformationFromOffresStep2(idOffreSend, phoneNumber)

    return {
        "resutFunction3" : resutFunction3,
        "resutFunction4" : resutFunction4,
    }


#This request POST for calculate the step one of offre for totality
@app.post("/company/getAllInformationForStep3")
async def getAllInformationForStep3(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction5 = getAllInformationOfAnWorkerFromDBForStep3(idOffreSend,phoneNumber)
    resutFunction6 = getInformationFromOffresStep3(idOffreSend, phoneNumber)

    return {
        "resutFunction5" : resutFunction5,
        "resutFunction6" : resutFunction6
    }


#This request POST for calculate the step one of offre for totality
@app.post("/company/getAllInformationForStep4")
async def getAllInformationForStep4(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    resutFunction7 = getInformationsOfProduct(idOffreSend, phoneNumber)
    resutFunction8 = getInformationFromOffresStep4(idOffreSend)
    print("Let's get started")
    return {
        "resutFunction7" : resutFunction7,
        "resutFunction8" : resutFunction8
    }

#This request POST for calculate the step one of offre for totality
@app.post("/company/addNegociateur")
async def addNegociateur(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']
    nameNegociateur = req['nameNegociateur']

    resutFunction = addNegotiation(idOffreSend,phoneNumber,nameNegociateur)

    # print(resutFunction)

    return {
        "resutFunction" : resutFunction,
    }