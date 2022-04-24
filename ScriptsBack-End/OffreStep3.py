import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
import base64

from DBConnexion import *
from GlobalOffre import *
from Company import *
from OffresStep3 import *
from WorkerCompany import *
from Salary import *
from workCGOffreForStep3 import *

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

def insertIntoOffresStep3(idOffre):
    try:
        selectRequette=""
        offStp3 = session.query(OffresStep3).filter(OffresStep3.idOffre == idOffre)
        for oS3 in offStp3:
            selectRequette = oS3.idOffre

        if(not selectRequette):
            session.add(OffresStep3(idOffre=idOffre))
            session.commit()

            print("Sucess add into OffresStep3 table")
            return 1
        else:
            print("You can't add this offre into OffresStep1 because you have it")
    except:
        print("There is a problem please check your data on table OffresStep1")
        return 0

def insertIntoworkCGOffreStep3(idOffre,fullName,nbWorkOnCompanySend,nbWorkOnSiteSend,valueSend,phoneNumberOfUser):
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
        selectRequette2.append(wC.H_jCostsOnCompany)
        selectRequette2.append(wC.H_jCostsOnSite)

    print(selectRequette2[0])
    print(selectRequette2[1])

    priceRevByWorker = round(((selectRequette2[1]*nbWorkOnSiteSend) + (selectRequette2[0]*nbWorkOnCompanySend)),3)
    pricePropByWorker = round((((selectRequette2[1]*selectRequette[1])*nbWorkOnSiteSend) + ((selectRequette2[0]*selectRequette[1])*nbWorkOnCompanySend)),3)
    coutByWorker = round((priceRevByWorker + (priceRevByWorker * (valueSend / 100))),3)
    # margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    # margeNet = round((pricePropByWorker - coutByWorker))
    margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    print(margeBrutte)
    margeNet = round((pricePropByWorker - coutByWorker))
    print(margeNet)
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

    session.add(workCGOffreForStep3(idWorker=selectRequette[0],idOffre=idOffre,hoursWorkCompany=nbWorkOnCompanySend,hoursWorkOutCompany=nbWorkOnSiteSend,FG=valueSend,CostsByWorker=coutByWorker,tPropositionByWorker=pricePropByWorker,tRevientByWorker=priceRevByWorker,tMargeNet=margeBrutte,tMargeBrute=margeNet,tMargeNetPC=margeNetPC))
    session.commit()
    print("Sucess add into workCGOffre table")
    
    return 1

def getInformationFromWorkCGOffreStep3(idOffreSend,phoneNumberOfUser):
    try:
        selectRequette1 = []
        selectRequette2 = []

        comap = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
        for gO in comap:
            selectRequette1.append(gO.companyId)

        WCGWCGO = session.query(workCGOffreForStep3,WorkerCompany,GlobalOffre).filter(and_(workCGOffreForStep3.idWorker==WorkerCompany.idWorker,workCGOffreForStep3.idOffre==GlobalOffre.idOffre,workCGOffreForStep3.idOffre==idOffreSend,GlobalOffre.companyId==selectRequette1[0]))
            
        for wcg,WC,go in WCGWCGO:
            if(not WC.profileWork):
                selectRequette2.append(workCGOffreForStep3Model("",WC.idWorker,WC.fullName,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC))
            else:
                selectRequette2.append(workCGOffreForStep3Model(base64.b64decode(WC.profileWork.decode('ascii')),WC.idWorker,WC.fullName,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC))

        return selectRequette2
    except:
        print("There is a probleme please try again !!")
        return 1

def updateInformationOfStep3ToDB(workerNameGlobaleSend,FGSend,nbWorkOnCompanySend,nbWorkOnSiteSend,idWorkerNameSend,idOffreSendGlobaleSend):
    selectRequette=[]
    selectRequette2 = []

    workerCompa = session.query(WorkerCompany).filter(WorkerCompany.idWorker == idWorkerNameSend)
    for wC in workerCompa:
        selectRequette.append(wC.profCoefficient)
    print(selectRequette)
    salary = session.query(Salary).filter(Salary.idWorker == idWorkerNameSend)
    for wC in salary:
        selectRequette2.append(wC.H_jCostsOnCompany)
        selectRequette2.append(wC.H_jCostsOnSite)

    print(selectRequette2[0])
    print(selectRequette2[1])

    priceRevByWorker = round(((selectRequette2[1]*nbWorkOnSiteSend) + (selectRequette2[0]*nbWorkOnCompanySend)),3)
    pricePropByWorker = round((((selectRequette2[1]*selectRequette[0])*nbWorkOnSiteSend) + ((selectRequette2[0]*selectRequette[0])*nbWorkOnCompanySend)),3)
    coutByWorker = round((priceRevByWorker + (priceRevByWorker * (FGSend / 100))),3)
    # margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    # margeNet = round((pricePropByWorker - coutByWorker))
    margeBrutte = round((pricePropByWorker - priceRevByWorker),3)
    print(margeBrutte)
    margeNet = round((pricePropByWorker - coutByWorker))
    print(margeNet)
    if margeNet ==0.0:
        margeNetPC = 0.0
    else:
        if(pricePropByWorker == 0 ):
            margeNetPC = 0
        else:
            margeNetPC = round((margeNet / pricePropByWorker) * 100)


    # print("Price Revient: ",priceRevByWorker)
    # print("Price Proposition: ",pricePropByWorker)
    # print("Cout: ",coutByWorker)
    # print("Marge Brute: ",margeBrutte)
    # print("Marge Net: ",margeNet)
    # print("Marge Net: ",margeNetPC,"%")

    workCGO3 = session.query(workCGOffreForStep3).filter(and_(workCGOffreForStep3.idWorker==idWorkerNameSend,workCGOffreForStep3.idOffre==idOffreSendGlobaleSend)).first()
    workCGO3.hoursWorkCompany = nbWorkOnCompanySend
    workCGO3.hoursWorkOutCompany = nbWorkOnSiteSend
    workCGO3.FG = FGSend
    workCGO3.CostsByWorker = coutByWorker
    workCGO3.tPropositionByWorker = pricePropByWorker
    workCGO3.tRevientByWorker = priceRevByWorker
    workCGO3.tMargeBrute = margeBrutte
    workCGO3.tMargeNet = margeNet
    workCGO3.tMargeNetPC = margeNetPC
    session.commit()

    return 1

def deleteAnWorkerFromOffreStep3UsingDB(workerProfileSend,idOffreSendGlobaleSend,phoneNumberOfUserSend):
    selectRequette=[]
    selectRequette1=[]

    comap = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUserSend)
    for gO in comap:
        selectRequette1.append(gO.companyId)

    workerCompa = session.query(WorkerCompany).filter(and_(WorkerCompany.fullName == workerProfileSend,WorkerCompany.companyId==selectRequette1[0]))
    for wC in workerCompa:
        selectRequette.append(wC.idWorker)

    workCGOSte3 = session.query(workCGOffreForStep3).filter(and_(workCGOffreForStep3.idWorker==selectRequette[0],workCGOffreForStep3.idOffre==idOffreSendGlobaleSend)).first()
    if(not workCGOSte3):
        print("You can do anything is empty")
    else:
        session.delete(workCGOSte3)
        session.commit()
        print("Sucess delete this worker from the offre")

    return 1

def calculPhase3OffreFromDB(idOffre):
    try:
        print(idOffre)
        selectRequette = []
        rowsInClCom = session.query(workCGOffreForStep3).filter(workCGOffreForStep3.idOffre == idOffre).count()
        # print(rowsInClCom)
        if rowsInClCom == 0:
            # If you will using the update method you will using this lines
            oS2 = session.query(OffresStep3).filter(OffresStep3.idOffre==idOffre).first()
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
            qry = session.query(func.sum(workCGOffreForStep3.hoursWorkCompany), 
                    func.sum(workCGOffreForStep3.hoursWorkOutCompany),
                    func.sum(workCGOffreForStep3.tPropositionByWorker),
                    func.sum(workCGOffreForStep3.tRevientByWorker),
                    func.sum(workCGOffreForStep3.CostsByWorker),
                    func.sum(workCGOffreForStep3.tMargeBrute),
                    func.sum(workCGOffreForStep3.tMargeNet),
                    ).filter(workCGOffreForStep3.idOffre==idOffre).group_by(workCGOffreForStep3.idOffre)
                    
            for _res in qry.all():
                print (_res)
                selectRequette.append(int(_res[0]))
                selectRequette.append(int(_res[1]))
                selectRequette.append(_res[2])
                selectRequette.append(_res[3])
                selectRequette.append(_res[4])
                selectRequette.append(_res[5])
                selectRequette.append(_res[6])

            print(selectRequette[0])
            print(selectRequette[1])
            
            totaleDatOfWork = selectRequette[0] + selectRequette[1]
            totaleQtyWork = round((totaleDatOfWork),2)
            totaleProposition = round(selectRequette[2],3)
            totaleRevient = round(selectRequette[3],3)
            CostsGlobale = round(selectRequette[4],3)
            totaleMargeNet = round(selectRequette[5],3)
            totaleMargeBrute = round(selectRequette[6],3)
            totaleMargeNetPC = round((totaleMargeNet / totaleProposition)*100)
            
            print('Totle Work',selectRequette[0] + selectRequette[1])
            print('Totale Proposition', selectRequette[2])
            print('Totale Revient',selectRequette[3])
            print('Costs Globale',selectRequette[4])
            print('Marge Brute',selectRequette[5])
            print('Marge Net',selectRequette[6])

            ofS3 = session.query(OffresStep3).filter(OffresStep3.idOffre==idOffre).first()
            ofS3.totaleQtyWork = totaleQtyWork
            ofS3.totaleProposition = totaleProposition
            ofS3.totaleRevient = totaleRevient
            ofS3.CostsGlobale = CostsGlobale
            ofS3.totaleMargeBrute = totaleMargeBrute
            ofS3.totaleMargeNet = totaleMargeNet
            ofS3.totaleMargeNetPC = totaleMargeNetPC
                
            session.commit()
            print("Sucess add into workCGOffre table")
            return 1
        
    except:
        print("There is a problem please check up")
        return 0

def getInformationFromOffresStep3(idOffre,phoneNumberOfUser):
    print(phoneNumberOfUser)
    print(idOffre)

    selectRequette1 = []
    selectRequette2 = []
    compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
    for cp in compan:
        selectRequette1.append(cp.companyId)

    offreStepGlobalOffre = session.query(OffresStep3,GlobalOffre).filter(and_(OffresStep3.idOffre==GlobalOffre.idOffre,OffresStep3.idOffre==idOffre,GlobalOffre.companyId==selectRequette1[0]))

    for oS1, glOff in offreStepGlobalOffre:
        selectRequette2.append(OffresStep3Model(glOff.idOffre,oS1.CostsGlobale,oS1.totaleProposition,oS1.totaleRevient,oS1.totaleQtyWork,oS1.totaleMargeBrute,oS1.totaleMargeNet,oS1.totaleMargeNetPC))

    print(selectRequette2)
    return selectRequette2