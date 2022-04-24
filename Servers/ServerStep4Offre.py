import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')

from ServerMain import *

#This request POST for Creation of step1 Offre
@app.post("/company/Step4Offre")
async def Step1Offre(request: Request):
    req = await request.json()

    dataSend = req['dataSend']
    idOffre = dataSend['idOffre']
    nomProduit = dataSend['nomProduit']
    pDVHT = dataSend['pDVHT']
    quantite = dataSend['quantite']
    ref = dataSend['ref']
    desc = dataSend['desc']
    valueSendMarge = req['valueSendMarge']
    valueSendRemise = req['valueSendRemise']
    phoneNumberOfUser = req['phoneNumber']

    resutFunction1 = checkIntoGlobalOffre(idOffre,phoneNumberOfUser)
    resutFunction2 = 0
    if(resutFunction1 == 1):
        resutFunction2 = insertIntoOffresStep4(idOffre,ref,nomProduit,pDVHT,quantite,valueSendMarge,valueSendRemise,desc)
        resutFunction = 1
        print("Let's get started")
    else:
        print("Not yet")
        resutFunction = 0

    return {
        "resutFunction" : resutFunction,
        "resutFunction2":resutFunction2
    }

#This request POST for GET all the informations of our product for step 4
@app.post("/company/getOffreStep4ById")
async def getOffreStep3ById(request: Request):
    print("Hello !!")
    req = await request.json()

    idOffreSend = req['idOffreSend']
    phoneNumber = req['phoneNumber']

    print(idOffreSend,phoneNumber)
    resultFunctionOffreStep4 = getInformationsOfProduct(idOffreSend,phoneNumber)

    return{
        "resultFunctionOffreStep4" : resultFunctionOffreStep4
    }

#This request POST for update the a offre for step 4
@app.post("/company/updateInformationOfStep4")
async def updateInformationOfStep4(request: Request):
    req = await request.json()

    idOffre = req['idOffre']
    referenceProduit = req['referenceProduit']
    nomProduit = req['nomProduit']
    prixUnitaire = req['prixUnitaire']
    quantity = req['quantity']
    marge = req['marge']
    remise = req['remise']


    resutFunction = updateInformationOfStep4ToDB(idOffre,referenceProduit,nomProduit,prixUnitaire,quantity,marge,remise)

    return {
        "resutFunction" : resutFunction
    }


#This request POST for delete a product from offre
@app.post("/company/deleteAnWorkerFromOffreStep4")
async def deleteAnWorkerFromOffreStep4(request: Request):
    req = await request.json()

    idOffre = req['idOffre']
    referenceProduit = req['referenceProduit']

    resutFunction = deleteAnWorkerFromOffreStep4UsingDB(idOffre,referenceProduit)

    return {
        "resutFunction" : resutFunction
    }



#This request POST for calculate the step one of offre for step4
@app.post("/company/calculPhase4Offre")
async def calculPhase4Offre(request: Request):
    req = await request.json()

    idOffreSend = req['idOffreSend']

    resutFunction = calculPhase4OffreFromDB(idOffreSend)
    # resutFunction = getInformationFromOffresStep2(idOffreSend,phoneNumber)

    return {
        "resutFunction" : resutFunction
    }