import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')

from ServerMain import *

#This request post for adding the worker in the database 
@app.post("/company/AddWorkerInDB")
async def AddWorkerInDB(request: Request):
    req = await request.json()

    phoneNumber = req['phoneNumber']
    profileWorker = req['imageProfileForUserSend']
    dataSend = req['dataSend']
    fullName = dataSend['fullName']
    professionWorker = dataSend['professionWorker']
    professionCoefficient = dataSend['professionCoefficient']
    departName = dataSend['departName']
    GrossSalary = dataSend['GrossSalary']

    resutFunction = AddWorkerInDataBase(phoneNumber,fullName,professionWorker,professionCoefficient,profileWorker,departName,GrossSalary)

    return {
        "resutFunction" : resutFunction
    }

#This request post for updating the informations of the worker company in the database 
@app.post("/company/updateInfoWorkerCompany")
async def updateInfoWorkerCompany(request: Request):
    req = await request.json()
    
    userProfileImageSend = req['userProfileImageSend']
    departmentNameWorkerSend = req['departmentNameWorkerSend']
    professionWorkerSend = req['professionWorkerSend']
    profitCofficientWorkerSend = req['profitCofficientWorkerSend']
    salaryWorkerSend = req['salaryWorkerSend']
    fullNameWorkerSend = req['fullNameWorkerSend']
    idWorkerSend = req['idWorkerSend']

    resutFunction = updateInfoWorkerCompanyInDB(userProfileImageSend,departmentNameWorkerSend,professionWorkerSend,profitCofficientWorkerSend,salaryWorkerSend,fullNameWorkerSend,idWorkerSend)

    return {
        "resutFunction" : resutFunction
    }

#This request post for updating the informations of the worker company in the database 
@app.post("/company/addInTableSalary")
async def addInTableSalary(request: Request):
    req = await request.json()

    dataSend = req['dataSend']
    fullName = dataSend['fullName']
    professionWorker = dataSend['professionWorker']
    GrossSalary = dataSend['GrossSalary']

    resutFunction = AddInTableSalary(fullName,professionWorker,GrossSalary)

    return {
        "resutFunction" : resutFunction
    }

#This request post for get all the informations of the worker company from the database 
@app.post("/company/GetAllWorkerCompany")
async def GetAllWorkerCompany(request: Request):
    req = await request.json()

    phoneNumber = req['phoneNumber']
    resutFunction = GetAllWorkerCompanyFromDB(phoneNumber)

    return{
        "resutFunction" : resutFunction
    }


#This request POST for delete an worker from the databases
@app.post("/company/deleteWorkerFromDB")
async def deleteWorkerFromDB(request: Request):
    req = await request.json()

    idWorker = req['idWorker']
    fullNameWorker = req['fullNameWorker']

    resutFunction = deleteWorkerFromDataBase(idWorker,fullNameWorker)

    return {
        "resutFunction" : resutFunction
    }

#This request POST for GET all the name ofworker from the databases
@app.post("/company/getAllWorkerName")
async def deleteWorkerFromDB(request: Request):
    req = await request.json()

    phoneNumber = req['phoneNumber']

    resutFunction = getAllWorkerNameFromDB(phoneNumber)

    return {
        "resutFunction" : resutFunction
    }