import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\DB')
import base64

from DBConnexion import *
from GlobalOffre import *
from Company import *
from OffresStep2 import *
from WorkerCompany import *
from Salary import *
from workCGOffreForStep2 import *

def checkIntoGlobalOffre(idOffre,phoneNumberOfUser):
    try:
        selectRequette = []
        selectRequette2 = []

        compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
        for cp in compan:
            selectRequette.append(cp.companyId)

        globOff = session.query(GlobalOffre).filter(and_(GlobalOffre.idOffre==idOffre,GlobalOffre.companyId==selectRequette[0]))
        for gO in globOff:
            selectRequette2.append(gO.idOffre)
            
        if (not selectRequette or not selectRequette2):
            return 0
        else:
            return 1
        print("Sucess check it")
    except:
        print("There is a problem please check your data on table GlobalOffre")
        return 0

def insertIntoOffresStep2(idOffre):
    try:
        selectRequette=""
        offStp2 = session.query(OffresStep2).filter(OffresStep2.idOffre == idOffre)
        for oS2 in offStp2:
            selectRequette = oS2.idOffre

        if(not selectRequette):
            session.add(OffresStep2(idOffre=idOffre))
            session.commit()

            print("Sucess add into OffresStep2 table")
            return 1
        else:
            print("You can't add this offre into OffresStep1 because you have it")
    except:
        print("There is a problem please check your data on table OffresStep1")
        return 0

def insertIntoworkCGOffreStep2(idOffre,fullName,nbHWOC,nbHWOS,valueSend,phoneNumberOfUser):
    print(fullName)
    try:
        selectRequette=[]
        selectRequette2=[]
        selectRequette3=[]

        comp = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
        for co in comp:
            selectRequette3.append(co.companyId)

        wCompany = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName == fullName,WorkerCompany.companyId== selectRequette3[0]))
        for wC in wCompany:
            selectRequette.append(wC.idWorker)
            selectRequette.append(wC.profCoefficient)

        salary = session.query(Salary).filter(Salary.idWorker == selectRequette[0])
        for wC in salary:
            selectRequette2.append(wC.H_jCostsOnCompany)
            selectRequette2.append(wC.H_jCostsOnSite)


        priceRevByWorker = round(((selectRequette2[1]*nbHWOS) + (selectRequette2[0]*nbHWOC)),3)
        pricePropByWorker = round((((selectRequette2[1]*selectRequette[1])*nbHWOS) + ((selectRequette2[0]*selectRequette[1])*nbHWOC)),3)
        coutByWorker = round((priceRevByWorker + (priceRevByWorker * (valueSend / 100))),3)
        margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
        print(margeBrutte)
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
            
        session.add(workCGOffreForStep2(idWorker=selectRequette[0],idOffre=idOffre,hoursWorkCompany=nbHWOC,hoursWorkOutCompany=nbHWOS,FG=valueSend,CostsByWorker=coutByWorker,tPropositionByWorker=pricePropByWorker,tRevientByWorker=priceRevByWorker,tMargeNet=margeBrutte,tMargeBrute=margeNet,tMargeNetPC=margeNetPC))
    
        session.commit()

        print("Sucess add into workCGOffre table")
        return 1
    except:
        print("There is a problem in the table of workCGOffre step2")
        return 0

def getInformationFromWorkCGOffreStep2(idOffreSend,phoneNumberOfUser):
    try:
        selectRequette1 = []
        selectRequette2 = []

        comap = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
        for gO in comap:
            selectRequette1.append(gO.companyId)

        WCGWCGO = session.query(workCGOffreForStep2,WorkerCompany,GlobalOffre).filter(and_(workCGOffreForStep2.idWorker==WorkerCompany.idWorker,workCGOffreForStep2.idOffre==GlobalOffre.idOffre,workCGOffreForStep2.idOffre==idOffreSend,GlobalOffre.companyId==selectRequette1[0]))
        
        for wcg,WC,go in WCGWCGO:
            selectRequette2.append(workCGOffreForStep2Model(base64.b64decode(WC.profileWork.decode('ascii')),WC.idWorker,WC.fullName,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC))

        return selectRequette2
    except:
        print("There is a probleme please try again !!")
        return 1

def updateInformationOfStep2ToDB(FGSend,nbWorkOnCompanySend,nbWorkOnSiteSend,idWorkerNameSend,idOffreSendGlobaleSend):
    selectRequette=[]
    selectRequette2 = []

    workerCompa = session.query(WorkerCompany).filter(WorkerCompany.idWorker == idWorkerNameSend)
    for wC in workerCompa:
        selectRequette.append(wC.profCoefficient)

    salary = session.query(Salary).filter(Salary.idWorker == idWorkerNameSend)
    for sal in salary:
        selectRequette2.append(sal.H_jCostsOnCompany)
        selectRequette2.append(sal.H_jCostsOnSite)

    priceRevByWorker = round(((selectRequette2[1]*nbWorkOnSiteSend) + (selectRequette2[0]*nbWorkOnCompanySend)),3)
    pricePropByWorker = round((((selectRequette2[1]*selectRequette[0])*nbWorkOnSiteSend) + ((selectRequette2[0]*selectRequette[0])*nbWorkOnCompanySend)),3)
    coutByWorker = round((priceRevByWorker + (priceRevByWorker * (FGSend / 100))),3)
    margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    print(margeBrutte)
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

    workCGO = session.query(workCGOffreForStep2).filter(and_(workCGOffreForStep2.idWorker==idWorkerNameSend,workCGOffreForStep2.idOffre==idOffreSendGlobaleSend)).first()
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
    print("Sucess update")
    return 1

def deleteAnWorkerFromOffreStep2UsingDB(workerProfileSend,idOffreSendGlobaleSend,phoneNumberOfUserSend):
    selectRequette=[]
    selectRequette1=[]

    comap = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUserSend)
    for gO in comap:
        selectRequette1.append(gO.companyId)

    workerCompa = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName == workerProfileSend,WorkerCompany.companyId==selectRequette1[0]))
    for wC in workerCompa:
        selectRequette.append(wC.idWorker)

    workCGOSte2 = session.query(workCGOffreForStep2).filter(and_(workCGOffreForStep2.idWorker==selectRequette[0],workCGOffreForStep2.idOffre==idOffreSendGlobaleSend)).first()
    session.delete(workCGOSte2)
    session.commit()
    print("Sucess delete this worker from the offre")

    return 1

def calculPhase2OffreFromDB(idOffre):
    try:
        selectRequette = []
        rowsInClCom = session.query(workCGOffreForStep2).filter(workCGOffreForStep2.idOffre == idOffre).count()
        print(rowsInClCom)
        if rowsInClCom == 0:
            # If you will using the update method you will using this lines
            oS2 = session.query(OffresStep2).filter(OffresStep2.idOffre==idOffre).first()
            oS2.CostsGlobale = 0
            oS2.totaleProposition = 0
            oS2.totaleRevient = 0
            oS2.totaleQtyWork = 0
            oS2.totaleMargeBrute = 0
            oS2.totaleMargeNet = 0
            oS2.totaleMargeNetPC = 0
            session.commit()
            print("Sucess update")
            return 1
                    
        else:
            qry = session.query(func.sum(workCGOffreForStep2.hoursWorkCompany), 
                    func.sum(workCGOffreForStep2.hoursWorkOutCompany),
                    func.sum(workCGOffreForStep2.tPropositionByWorker),
                    func.sum(workCGOffreForStep2.tRevientByWorker),
                    func.sum(workCGOffreForStep2.CostsByWorker),
                    func.sum(workCGOffreForStep2.tMargeBrute),
                    func.sum(workCGOffreForStep2.tMargeNet),
                    ).filter(workCGOffreForStep2.idOffre==idOffre).group_by(workCGOffreForStep2.idOffre)
                    
            for _res in qry.all():
                print (_res)
                selectRequette.append(int(_res[0]))
                selectRequette.append(int(_res[1]))
                selectRequette.append(_res[2])
                selectRequette.append(_res[3])
                selectRequette.append(_res[4])
                selectRequette.append(_res[5])
                selectRequette.append(_res[6])
            print("Totale proposition")
            print(selectRequette[2])

            totaleDatOfWork = selectRequette[0]+selectRequette[1]
            totaleQtyWork = round((totaleDatOfWork),2)
            totaleProposition = round(selectRequette[2],3)
            totaleRevient = round(selectRequette[3],3)
            CostsGlobale = round(selectRequette[4],3)
            totaleMargeNet = round(selectRequette[5],3)
            totaleMargeBrute = round(selectRequette[6],3)
            totaleMargeNetPC = round((totaleMargeNet / totaleProposition)*100)

            print(totaleProposition)
            print(totaleMargeBrute)
            print(totaleMargeNetPC)

            ofS2 = session.query(OffresStep2).filter(OffresStep2.idOffre==idOffre).first()
            ofS2.totaleQtyWork = totaleQtyWork
            ofS2.totaleProposition = totaleProposition
            ofS2.totaleRevient = totaleRevient
            ofS2.CostsGlobale = CostsGlobale
            ofS2.totaleMargeBrute = totaleMargeBrute
            ofS2.totaleMargeNet = totaleMargeNet
            ofS2.totaleMargeNetPC = totaleMargeNetPC
                
            session.commit()
            print("Sucess add into workCGOffre table")
            return 1
        
    except:
        print("There is a problem please check up")
        return 0

def getInformationFromOffresStep2(idOffre,phoneNumberOfUser):
    print(phoneNumberOfUser)
    print(idOffre)

    selectRequette1 = []
    selectRequette2 = []
    compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
    for cp in compan:
        selectRequette1.append(cp.companyId)

    offreStepGlobalOffre = session.query(OffresStep2,GlobalOffre).filter(and_(OffresStep2.idOffre==GlobalOffre.idOffre,OffresStep2.idOffre==idOffre,GlobalOffre.companyId==selectRequette1[0]))

    for oS1, glOff in offreStepGlobalOffre:
        selectRequette2.append(OffresStep2Model(glOff.idOffre,oS1.CostsGlobale,oS1.totaleProposition,oS1.totaleRevient,oS1.totaleQtyWork,oS1.totaleMargeBrute,oS1.totaleMargeNet,oS1.totaleMargeNetPC))

    print(selectRequette2)
    return selectRequette2