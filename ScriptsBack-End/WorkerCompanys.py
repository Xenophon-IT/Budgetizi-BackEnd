import sys         
sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
from DBConnexion import *

from ClientCompany import *
from WorkerCompany import *
from Company import *
from Salary import *
from workCGOffre import *
from workCGOffreForStep2 import *
from workCGOffreForStep3 import *

import jwt
import base64
from datetime import date

def AddWorkerInDataBase(phoneNumberOfUser,fullName,professionWorker,professionCoefficient,profileWorker,departName,GrossSalary): 
    try:
        profileWorker = profileWorker.encode('ascii')
        profileWorkerBin = base64.b64encode(profileWorker)
        selectRequette=""

        comp = session.query(Company).filter(Company.phoneNumberClientCompany==phoneNumberOfUser)
        for co in comp:
            selectRequette = co.companyId

        yearCreComp = date.today().year

        session.add(WorkerCompany(fullName=fullName,profession=professionWorker,departName=departName,profCoefficient=professionCoefficient,profileWork=profileWorkerBin,companyId=selectRequette,yearCreationCompte=yearCreComp))
        session.commit()
        print("Success in adding data into WorkerCompany table")

        AddInTableSalary(fullName,professionWorker,GrossSalary)
        return 1
    except:
        print("Can't insert into dataBase !!!")
        return 0


def AddInTableSalary(fullName,professionWorker,GrossSalary):
    selectRequette=""
    try:
        workerCompany = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName == fullName, WorkerCompany.profession == professionWorker))
        for wC in workerCompany:
            selectRequette= wC.idWorker
        H_jCostsOnCompany = round((((GrossSalary*14)/300)+((GrossSalary*14*27/100)/365)),3)
        H_jCostsOnSite =round(( H_jCostsOnCompany*2),3)
        HCostsOnCompany = round((H_jCostsOnCompany/8),3)
        HCostsOnSite = round((HCostsOnCompany*2),3)

        session.add(Salary(idWorker=selectRequette,salary=GrossSalary,H_jCostsOnCompany=H_jCostsOnCompany,H_jCostsOnSite=H_jCostsOnSite,HCostsOnCompany=HCostsOnCompany,HCostsOnSite=HCostsOnSite))
        session.commit()
        print("Sucess in adding into salary table")
        return 1
    except:
        return 0
        print("There is an problem to insert into dataBase !!!")


def updateInfoWorkerCompanyInDB(userProfileImageSend,departmentNameWorkerSend,professionWorkerSend,profitCofficientWorkerSend,salaryWorkerSend,fullNameWorkerSend,idWorkerSend):
    
    profileWorker = userProfileImageSend.encode('ascii')
    profileWorkerBin = base64.b64encode(profileWorker)

    workCompa = session.query(WorkerCompany).filter(WorkerCompany.idWorker == idWorkerSend).first()
    workCompa.fullName = fullNameWorkerSend
    workCompa.profession = professionWorkerSend
    workCompa.departName = departmentNameWorkerSend
    workCompa.profCoefficient = profitCofficientWorkerSend
    workCompa.profileWork = profileWorkerBin
    session.commit()

    H_jCostsOnCompany = round((((int(salaryWorkerSend)*14)/300)+((int(salaryWorkerSend)*14*27/100)/365)),3)
    H_jCostsOnSite =round(( H_jCostsOnCompany*2),3)
    HCostsOnCompany = round((H_jCostsOnCompany/8),3)
    HCostsOnSite = round((HCostsOnCompany*2),3)

    print(type(salaryWorkerSend))
    salary = session.query(Salary).filter(Salary.idWorker == idWorkerSend).first()
    salary.salary = int(salaryWorkerSend)
    salary.H_jCostsOnCompany = H_jCostsOnCompany
    salary.H_jCostsOnSite = H_jCostsOnSite
    salary.HCostsOnCompany = HCostsOnCompany
    salary.HCostsOnSite = HCostsOnSite
    
    session.commit()
    print("Sucess update into the table salary and workercompany")

def GetAllWorkerCompanyFromDB(phoneNumberOfUser):
    selectRequette=""
    selectRequette2=[]
    print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    company = session.query(Company).filter(Company.phoneNumberClientCompany==phoneNumberOfUser)
    for com in company:
        selectRequette = com.companyId
    print(selectRequette)
    workComSal = session.query(WorkerCompany,Salary).filter(and_(WorkerCompany.companyId==selectRequette,WorkerCompany.idWorker==Salary.idWorker))
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    for WC, SA in workComSal:
        print(WC.fullName)
    for WC, SA in workComSal:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(WC.fullName)
        if(not WC.profileWork):
            selectRequette2.append(WorkerCompanyModel(WC.idWorker,WC.fullName,WC.profession,WC.departName,WC.profCoefficient,"",WC.yearCreationCompte,WC.companyId,SA.salary))
        else:
            selectRequette2.append(WorkerCompanyModel(WC.idWorker,WC.fullName,WC.profession,WC.departName,WC.profCoefficient,base64.b64decode(WC.profileWork.decode('ascii')),WC.yearCreationCompte,WC.companyId,SA.salary))

    return selectRequette2


def deleteWorkerFromDataBase(idWorker,fullNameWorker):

    salary = session.query(Salary).filter(Salary.idWorker == idWorker).first()
    session.delete(salary)
    session.commit()
    print("Sucess delete this worker from Salary table")

    workCGO = session.query(workCGOffre).filter(workCGOffre.idWorker == idWorker).first()
    if(not workCGO):
        print("workCGO is empty")
    else:
        session.delete(workCGO)
        session.commit()
        print("Sucess delete this worker from workCGOffre table")

    workCGO2 = session.query(workCGOffreForStep2).filter(workCGOffreForStep2.idWorker == idWorker).first()
    if(not workCGO2):
        print("workCGO is empty")
    else:
        session.delete(workCGO2)
        session.commit()
        print("Sucess delete this worker from workCGOffreForStep2 table")

    workCGO3 = session.query(workCGOffreForStep3).filter(workCGOffreForStep3.idWorker == idWorker).first()
    if(not workCGO3):
        print("workCGO is empty")
    else:
        session.delete(workCGO3)
        session.commit()
        print("Sucess delete this worker from workCGOffreForStep3 table")

    workerCompany = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName==fullNameWorker,WorkerCompany.idWorker==idWorker)).first()
    if(not workerCompany):
        print("workerCompany is empty")
    else:
        session.delete(workerCompany)
        session.commit()
        print("Sucess delete this worker from WorkerCompany table")        
    return 1

    # try:
    #     salary = session.query(Salary).filter(Salary.idWorker == idWorker).first()
    #     session.delete(salary)
    #     session.commit()
    #     print("Sucess delete this worker from Salary table")

    #     workCGO = session.query(workCGOffre).filter(workCGOffre.idWorker == idWorker).first()
    #     session.delete(workCGO)
    #     session.commit()
    #     print("Sucess delete this worker from workCGOffre table")


    #     workCGO2 = session.query(workCGOffreForStep2).filter(workCGOffreForStep2.idWorker == idWorker).first()
    #     session.delete(workCGO2)
    #     session.commit()
    #     print("Sucess delete this worker from workCGOffreForStep2 table")

    #     workCGO3 = session.query(workCGOffreForStep3).filter(workCGOffreForStep3.idWorker == idWorker).first()
    #     session.delete(workCGO3)
    #     session.commit()
    #     print("Sucess delete this worker from workCGOffreForStep3 table")

    #     workerCompany = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName==fullNameWorker,WorkerCompany.idWorker==idWorker)).first()
    #     session.delete(workerCompany)
    #     session.commit()
    #     print("Sucess delete this worker from WorkerCompany table")
            
    #     return 1
    # except:
    #     print("There is a problem on delete")
    #     return 0

def getAllWorkerNameFromDB(phoneNumberOfUser):
    selectRequette=""
    selectRequette2 = []

    nameWorker = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
    for nW in nameWorker:
        selectRequette = nW.companyId

    print(selectRequette)
    nameWorkerCompany = session.query(WorkerCompany).filter(WorkerCompany.companyId == selectRequette)
    for nWC in nameWorkerCompany:
        selectRequette2.append(nWC.fullName)
    return selectRequette2