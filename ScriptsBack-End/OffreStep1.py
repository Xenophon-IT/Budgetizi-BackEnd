import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\DB')
import base64

from DBConnexion import *
from GlobalOffre import *
from Company import *
from OffresStep1 import *
from WorkerCompany import *
from Salary import *
from workCGOffre import *

def insertIntoGlobalOffre(idOffre,phoneNumberOfUser):
    try:
        selectRequette0=""

        globalOffre = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffre)
        for gO in globalOffre:
            selectRequette0 = gO.idOffre

        if(not selectRequette0):
            selectRequette = ""
            comp = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
            for co in comp:
                selectRequette = co.companyId

            session.add(GlobalOffre(idOffre=idOffre,companyId=selectRequette,globalDaysOfWork=0,globalProposition=0,globalRevient=0,globalRevientAndFG=0,globalMargeBrute=0,globalMargeNete=0,globalFinaleMarge=0))
            session.commit()
            print("Sucess add into GlobalOffre table")
            return 1
        else:
            print("You can't add this offre into GlobalOffre because you have it")
    except:
        print("There is a problem please check your data on table GlobalOffre")
        return 0

def insertIntoOffresStep1(idOffre):
    try:
        selectRequette=""

        offresStep1 = session.query(OffresStep1).filter(OffresStep1.idOffre == idOffre)
        for oS1 in offresStep1:
            selectRequette = oS1.idOffre

        if(not selectRequette):

            session.add(OffresStep1(idOffre=idOffre))
            session.commit()

            print("Sucess add into OffresStep1 table")
            return 1
        else:
            print("You can't add this offre into OffresStep1 because you have it")
    except:
        print("There is a problem please check your data on table OffresStep1")
        return 0

def insertIntoworkCGOffre(idOffre,fullName,nbHWOC,nbHWOS,valueSend,phoneNumberOfUser):
    selectRequette=[]
    selectRequette2=[]
    selectRequette3=[]

    comp = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
    for co in comp:
        selectRequette3.append(co.companyId)

    print(selectRequette3[0])
    wCompany = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName == fullName,WorkerCompany.companyId== selectRequette3[0]))
    for wC in wCompany:
        selectRequette.append(wC.idWorker)
        selectRequette.append(wC.profCoefficient)

    print(selectRequette[0])
    print(selectRequette[1])

    salary = session.query(Salary).filter(Salary.idWorker == selectRequette[0])
    for wC in salary:
        selectRequette2.append(wC.HCostsOnCompany)
        selectRequette2.append(wC.HCostsOnSite)

    print(selectRequette2[0])
    print(selectRequette2[1])

    priceRevByWorker = round(((selectRequette2[1]*nbHWOS) + (selectRequette2[0]*nbHWOC)),3)
    pricePropByWorker = round((((selectRequette2[1]*selectRequette[1])*nbHWOS) + ((selectRequette2[0]*selectRequette[1])*nbHWOC)),3)
    coutByWorker = round((priceRevByWorker + (priceRevByWorker * (valueSend / 100))),3)
    margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    margeNet = round((pricePropByWorker - coutByWorker))
    if margeNet ==0.0:
        margeNetPC = 0.0
    else:
        if(pricePropByWorker == 0 ):
            margeNetPC = 0
        else:
            margeNetPC = round((margeNet / pricePropByWorker) * 100)

    print("Price Revient: ",priceRevByWorker)
    print("Price Proposition: ",pricePropByWorker)
    print("Cout: ",coutByWorker)
    print("Marge Brute: ",margeBrutte)
    print("Marge Net: ",margeNet)
    print("Marge Net: ",margeNetPC,"%")
            
    session.add(workCGOffre(idWorker=selectRequette[0],idOffre=idOffre,hoursWorkCompany=nbHWOC,hoursWorkOutCompany=nbHWOS,FG=valueSend,CostsByWorker=coutByWorker,tPropositionByWorker=pricePropByWorker,tRevientByWorker=priceRevByWorker,tMargeNet=margeBrutte,tMargeBrute=margeNet,tMargeNetPC=margeNetPC))
    session.commit()

    print("Sucess add into workCGOffre table")
    return 1
    
    # try:
    #     selectRequette=[]
    #     selectRequette2=[]

    #     wCompany = session.query(WorkerCompany).filter(WorkerCompany.fullName == fullName)
    #     for wC in wCompany:
    #         selectRequette.append(wC.idWorker)
    #         selectRequette.append(wC.profCoefficient)

    #     salary = session.query(Salary).filter(Salary.idWorker == selectRequette[0])
    #     for wC in salary:
    #         selectRequette2.append(wC.HCostsOnCompany)
    #         selectRequette2.append(wC.HCostsOnSite)


    #     priceRevByWorker = round(((selectRequette2[1]*nbHWOS) + (selectRequette2[0]*nbHWOC)),3)
    #     pricePropByWorker = round((((selectRequette2[1]*selectRequette[1])*nbHWOS) + ((selectRequette2[0]*selectRequette[1])*nbHWOC)),3)
    #     coutByWorker = round((priceRevByWorker + (priceRevByWorker * (valueSend / 100))),3)
    #     margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    #     margeNet = round((pricePropByWorker - coutByWorker))
    #     if margeNet ==0.0:
    #         margeNetPC = 0.0
    #     else:
    #         if(pricePropByWorker == 0 ):
    #             margeNetPC = 0
    #         else:
    #             margeNetPC = round((margeNet / pricePropByWorker) * 100)

    #     print("Price Revient: ",priceRevByWorker)
    #     print("Price Proposition: ",pricePropByWorker)
    #     print("Cout: ",coutByWorker)
    #     print("Marge Brute: ",margeBrutte)
    #     print("Marge Net: ",margeNet)
    #     print("Marge Net: ",margeNetPC,"%")
            
    #     session.add(workCGOffre(idWorker=selectRequette[0],idOffre=idOffre,hoursWorkCompany=nbHWOC,hoursWorkOutCompany=nbHWOS,FG=valueSend,CostsByWorker=coutByWorker,tPropositionByWorker=pricePropByWorker,tRevientByWorker=priceRevByWorker,tMargeNet=margeBrutte,tMargeBrute=margeNet,tMargeNetPC=margeNetPC))
    #     session.commit()

    #     print("Sucess add into workCGOffre table")
    #     return 1
    # except:
    #     print("There is a problem in the table of workCGOffre step1")
    #     return 0

def getInformationFromWorkCGOffre(idOffreSend,phoneNumberOfUser):
    # try:
        
    # except:
    #     print("There is a probleme please try again !!")
    #     return 1

    selectRequette1 = []
    selectRequette2 = []
    print(idOffreSend,phoneNumberOfUser)
    comap = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
    for gO in comap:
        selectRequette1.append(gO.companyId)

    WCGWCGO = session.query(workCGOffre,WorkerCompany,GlobalOffre).filter(and_(workCGOffre.idWorker==WorkerCompany.idWorker,workCGOffre.idOffre==GlobalOffre.idOffre,workCGOffre.idOffre==idOffreSend,GlobalOffre.companyId==selectRequette1[0]))
    
    for wcg,WC,go in WCGWCGO:
        print(WC.idWorker)
        selectRequette2.append(workCGOffreModel(base64.b64decode(WC.profileWork.decode('ascii')),WC.idWorker,WC.fullName,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC))
    
    return selectRequette2


def updateInformationOfStep1ToDB(FGSend,nbWorkOnCompanySend,nbWorkOnSiteSend,idWorkerNameSend,idOffreSendGlobaleSend):
    selectRequette=[]
    selectRequette2 = []

    workerCompa = session.query(WorkerCompany).filter(WorkerCompany.idWorker == idWorkerNameSend)
    for wC in workerCompa:
        selectRequette.append(wC.profCoefficient)

    salary = session.query(Salary).filter(Salary.idWorker == idWorkerNameSend)
    for sal in salary:
        selectRequette2.append(sal.HCostsOnCompany)
        selectRequette2.append(sal.HCostsOnSite)

    priceRevByWorker = round(((selectRequette2[1]*nbWorkOnSiteSend) + (selectRequette2[0]*nbWorkOnCompanySend)),3)
    pricePropByWorker = round((((selectRequette2[1]*selectRequette[0])*nbWorkOnSiteSend) + ((selectRequette2[0]*selectRequette[0])*nbWorkOnCompanySend)),3)
    coutByWorker = round((priceRevByWorker + (priceRevByWorker * (FGSend / 100))),3)
    margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    margeNet = round((pricePropByWorker - coutByWorker))
    if margeNet ==0.0:
        margeNetPC = 0.0
    else:
        if(pricePropByWorker == 0):
            margeNetPC = 0
        else:
            margeNetPC = round((margeNet / pricePropByWorker) * 100)

    print(nbWorkOnCompanySend)
    print(nbWorkOnSiteSend)

    workCGO = session.query(workCGOffre).filter(and_(workCGOffre.idWorker==idWorkerNameSend,workCGOffre.idOffre==idOffreSendGlobaleSend)).first()
    workCGO.hoursWorkCompany = nbWorkOnCompanySend
    workCGO.hoursWorkOutCompany = nbWorkOnSiteSend
    workCGO.FG = FGSend
    workCGO.CostsByWorker = coutByWorker
    workCGO.tPropositionByWorker = pricePropByWorker
    workCGO.tRevientByWorker = priceRevByWorker
    workCGO.tMargeBrute = margeBrutte
    workCGO.tMargeNet = margeNet
    workCGO.tMargeNetPC = margeNetPC
    session.commit()

    return 1

def deleteAnWorkerFromOffreUsingDB(workerProfileSend,idOffreSendGlobaleSend,phoneNumberOfUserSend):
    selectRequette=[]
    selectRequette1=[]

    comap = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUserSend)
    for gO in comap:
        selectRequette1.append(gO.companyId)

    workerCompa = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName == workerProfileSend,WorkerCompany.companyId==selectRequette1[0]))
    for wC in workerCompa:
        selectRequette.append(wC.idWorker)
    print(selectRequette[0])
    workCGO = session.query(workCGOffre).filter(and_(workCGOffre.idWorker==selectRequette[0],workCGOffre.idOffre==idOffreSendGlobaleSend)).first()
    
    session.delete(workCGO)
    session.commit()
    print("Sucess delete this worker from the offre")

    return 1

def calculPhase1OffreFromDB(idOffre):
    try:
        selectRequette = []
        rowsInClCom = session.query(workCGOffre).filter(workCGOffre.idOffre == idOffre).count()
        print(rowsInClCom)
        if rowsInClCom == 0:
            # If you will using the update method you will using this lines
            oS1 = session.query(OffresStep1).filter(OffresStep1.idOffre==idOffre).first()
            oS1.CostsGlobale = 0
            oS1.totaleProposition = 0
            oS1.totaleRevient = 0
            oS1.totaleQtyWork = 0
            oS1.totaleMargeBrute = 0
            oS1.totaleMargeNet = 0
            oS1.totaleMargeNetPC = 0
            session.commit()
            print("Sucess update")
            return 1
                    
        else:
            qry = session.query(func.sum(workCGOffre.hoursWorkCompany), 
                    func.sum(workCGOffre.hoursWorkOutCompany),
                    func.sum(workCGOffre.tPropositionByWorker),
                    func.sum(workCGOffre.tRevientByWorker),
                    func.sum(workCGOffre.CostsByWorker),
                    func.sum(workCGOffre.tMargeBrute),
                    func.sum(workCGOffre.tMargeNet),
                    ).filter(workCGOffre.idOffre==idOffre).group_by(workCGOffre.idOffre)
                    
            for _res in qry.all():
                print (_res)
                selectRequette.append(int(_res[0]))
                selectRequette.append(int(_res[1]))
                selectRequette.append(_res[2])
                selectRequette.append(_res[3])
                selectRequette.append(_res[4])
                selectRequette.append(_res[5])
                selectRequette.append(_res[6])
                    
            totaleDatOfWork = selectRequette[0]+selectRequette[1]
            totaleQtyWork = round((totaleDatOfWork / 8.66),2)
            totaleProposition = round(selectRequette[2],3)
            totaleRevient = round(selectRequette[3],3)
            CostsGlobale = round(selectRequette[4],3)
            totaleMargeNet = round(selectRequette[5],3)
            totaleMargeBrute = round(selectRequette[6],3)
            totaleMargeNetPC = round((totaleMargeNet / totaleProposition)*100)

            print(totaleProposition)
            print(totaleMargeBrute)
            print(totaleMargeNetPC)

            ofS1 = session.query(OffresStep1).filter(OffresStep1.idOffre==idOffre).first()
            ofS1.totaleQtyWork = totaleQtyWork
            ofS1.totaleProposition = totaleProposition
            ofS1.totaleRevient = totaleRevient
            ofS1.CostsGlobale = CostsGlobale
            ofS1.totaleMargeBrute = totaleMargeBrute
            ofS1.totaleMargeNet = totaleMargeNet
            ofS1.totaleMargeNetPC = totaleMargeNetPC
                
            session.commit()
            print("Sucess add into workCGOffre table")
            return 1
        
    except:
        print("There is a problem please check up")
        return 0

def getInformationFromOffresStep1(idOffre,phoneNumberOfUser):
    print(phoneNumberOfUser)
    print(idOffre)

    selectRequette1 = []
    selectRequette2 = []
    compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
    for cp in compan:
        selectRequette1.append(cp.companyId)

    offreStepGlobalOffre = session.query(OffresStep1,GlobalOffre).filter(and_(OffresStep1.idOffre==GlobalOffre.idOffre,OffresStep1.idOffre==idOffre,GlobalOffre.companyId==selectRequette1[0]))

    for oS1, glOff in offreStepGlobalOffre:
        selectRequette2.append(OffresStep1Model(glOff.idOffre,oS1.CostsGlobale,oS1.totaleProposition,oS1.totaleRevient,oS1.totaleQtyWork,oS1.totaleMargeBrute,oS1.totaleMargeNet,oS1.totaleMargeNetPC))

    print(selectRequette2)
    return selectRequette2

# getInformationFromOffresStep1('JustGroup-01','+21653786397')