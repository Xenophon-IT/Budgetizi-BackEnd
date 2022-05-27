import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')

from ServerMain import *

@app.post("/company/archivesOffres")
async def archivesOffres(request: Request):
    req = await request.json()
    phoneNumber = req['phoneNumber']

    print("test test",phoneNumber)

    #This function is for register of our client and you find it in the file named by BackendScript
    resutFunction = getAllOffres(phoneNumber)
    resutFunction2 = getAllOffresFromDB(phoneNumber)

    return {
        "resutFunction": resutFunction, # 0: the phone number is use it | 1: ok ok
        "resutFunction2":resutFunction2
    }

@app.post("/company/getOffreFromArchives")
async def getOffreFromArchives(request: Request):
    req = await request.json()
    idOffreSendGlobal = req['idOffreSend']

    #This function is for register of our client and you find it in the file named by BackendScript
    resutFunction = getOffreFromArchivesDB(idOffreSendGlobal)

    return {
        "resutFunction": resutFunction # 0: the phone number is use it | 1: ok ok
    }

@app.post("/company/updateInformationOffreNegociation")
async def updateInformationOffreNegociation(request: Request):
    req = await request.json()
    idOffre = req['idOffreSend']
    nomNegociateurSend = req['nomNegociateurSend']
    remiseSend = req['remiseSend']
    statusSend = req['statusSend']

    print("zzzzzzzzzzz")
    print(idOffre)
    print(statusSend)
    print(remiseSend)
    print(statusSend)
    print("22222222222222")
    #This function is for register of our client and you find it in the file named by BackendScript
    resutFunction = updateInformationOffreNegociationDB(idOffre,nomNegociateurSend,remiseSend,statusSend)

    return {
        "resutFunction": resutFunction # 0: the phone number is use it | 1: ok ok
    }