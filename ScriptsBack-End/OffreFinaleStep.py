import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
from DBConnexion import *
from workCGOffre import *
from workCGOffreForStep2 import *
from workCGOffreForStep3 import *
from OffresStep1 import *
from OffresStep2 import *
from OffresStep3 import *
from WorkerCompany import *
from GlobalOffre import *
from Negotiation import *
from OffresStep4 import *

import base64

def getAllInformationOfAnWorkerFromDB(idOffreSend,phoneNumberOfUser):
    selectRequette=[]
    WCGWCGO = session.query(workCGOffre,WorkerCompany).filter(and_(workCGOffre.idOffre==idOffreSend,workCGOffre.idWorker==WorkerCompany.idWorker))      
    for wcg,WC in WCGWCGO:
        selectRequette.append(workCGOffreFinalModel(wcg.idWorker,wcg.idOffre,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC,base64.b64decode(WC.profileWork.decode('ascii')),WC.fullName))
    print(selectRequette)
    return selectRequette

def getAllInformationOfAnWorkerFromDBForStep2(idOffreSend,phoneNumberOfUser):
    selectRequette=[]
    WCGWCGO = session.query(workCGOffreForStep2,WorkerCompany).filter(and_(workCGOffreForStep2.idOffre==idOffreSend,workCGOffreForStep2.idWorker==WorkerCompany.idWorker))      
    for wcg,WC in WCGWCGO:
        selectRequette.append(workCGOffreFinalModelStep2(wcg.idWorker,wcg.idOffre,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC,base64.b64decode(WC.profileWork.decode('ascii')),WC.fullName))
    print(selectRequette)
    return selectRequette

def getAllInformationOfAnWorkerFromDBForStep3(idOffreSend,phoneNumberOfUser):
    selectRequette=[]
    WCGWCGO = session.query(workCGOffreForStep3,WorkerCompany).filter(and_(workCGOffreForStep3.idOffre==idOffreSend,workCGOffreForStep3.idWorker==WorkerCompany.idWorker))      
    for wcg,WC in WCGWCGO:
        if(not WC.profileWork):
            selectRequette.append(workCGOffreFinalModelStep3(wcg.idWorker,wcg.idOffre,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC,"",WC.fullName))
        else:
            selectRequette.append(workCGOffreFinalModelStep3(wcg.idWorker,wcg.idOffre,wcg.hoursWorkCompany,wcg.hoursWorkOutCompany,wcg.FG,wcg.CostsByWorker,wcg.tPropositionByWorker,wcg.tRevientByWorker,wcg.tMargeBrute,wcg.tMargeNet,wcg.tMargeNetPC,base64.b64decode(WC.profileWork.decode('ascii')),WC.fullName))
    print(selectRequette)
    return selectRequette

def offreFinaleCalculDB(idOffreSend):
    selectRequette1 = []
    selectRequette2 = []
    selectRequette3 = []

    offreSep1 = session.query(OffresStep1).filter(OffresStep1.idOffre == idOffreSend)
    for oS1 in offreSep1:
        selectRequette1.append(oS1.totaleProposition)
        selectRequette1.append(oS1.totaleRevient)
        selectRequette1.append(oS1.CostsGlobale)
        selectRequette1.append(oS1.totaleMargeBrute)
        selectRequette1.append(oS1.totaleMargeNet)

    offreSep2 = session.query(OffresStep2).filter(OffresStep2.idOffre == idOffreSend)
    for oS2 in offreSep2:
        selectRequette2.append(oS2.totaleProposition)
        selectRequette2.append(oS2.totaleRevient)
        selectRequette2.append(oS2.CostsGlobale)
        selectRequette2.append(oS2.totaleMargeBrute)
        selectRequette2.append(oS2.totaleMargeNet)

    offreSep3 = session.query(OffresStep3).filter(OffresStep3.idOffre == idOffreSend)
    for oS3 in offreSep3:
        selectRequette3.append(oS3.totaleProposition)
        selectRequette3.append(oS3.totaleRevient)
        selectRequette3.append(oS3.CostsGlobale)
        selectRequette3.append(oS3.totaleMargeBrute)
        selectRequette3.append(oS3.totaleMargeNet)

    globalProposition = selectRequette1[0] + selectRequette2[0] + selectRequette3[0]
    globalRevient = selectRequette1[1] + selectRequette2[1] + selectRequette3[1]
    globalRevientAndFG = selectRequette1[2] + selectRequette2[2] + selectRequette3[2]
    globalMargeBrute = selectRequette1[3] + selectRequette2[3] + selectRequette3[3]
    globalMargeNete = selectRequette1[4] + selectRequette2[4] + selectRequette3[4]
        
    globalPropositionFinale = round(globalProposition,3)
    globalRevientFinale = round(globalRevient,3)
    globalRevientAndFGFinale = round(globalRevientAndFG,3)
    globalMargeBruteFinale = round(globalMargeBrute,3)
    globalMargeNeteFinale = round(globalMargeNete,3)

    if globalPropositionFinale == 0:
        globalFinaleMarge = 0
    else:
        globalFinaleMarge = round((globalMargeNeteFinale / globalPropositionFinale)*100)

    globOffre = session.query(GlobalOffre).filter(GlobalOffre.idOffre==idOffreSend).first()
    globOffre.globalProposition = globalPropositionFinale
    globOffre.globalRevient = globalRevientFinale
    globOffre.globalRevientAndFG = globalRevientAndFGFinale
    globOffre.globalMargeBrute = globalMargeBruteFinale
    globOffre.globalMargeNete = globalMargeNeteFinale
    globOffre.globalFinaleMarge = globalFinaleMarge
    session.commit()
    print("Sucess update into table GlobalOffre")
    return 1

def getInformationOffreFinale(idOffreSend):
    selectRequette = []
    globOff = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend)
    for gOF in globOff:
        selectRequette.append(GlobalOffreModel(gOF.idOffre,gOF.globalDaysOfWork,gOF.globalProposition,gOF.globalRevient,gOF.globalRevientAndFG,gOF.globalMargeBrute,gOF.globalMargeNete,gOF.globalFinaleMarge,gOF.companyId))
    
    return selectRequette

def getInformationFromOffresStep4(idOffreSend):
    selectRequette=[]

    globalOffre = session.query(GlobalOffre).filter(GlobalOffre.idOffre==idOffreSend)      
    for go in globalOffre:
        selectRequette.append(go.globalPropositionStPr)
        selectRequette.append(go.totaleFinalHT)
        selectRequette.append(go.totaleFinalTTC)
    print(selectRequette)
    return selectRequette

def addNegotiation(idOffreSend,phoneNumber,nameNegociateur):
    session.add(Negotiation(idOffre=idOffreSend,nomNegociateur=nameNegociateur,status="warning",remisePercent=0,globalPropositionStPrWR=0,globalMargeNetteStPrWR=0,description="En Négociation"))
    session.commit()

    selectRequette = []
    qry = session.query(func.sum(OffresStep4.quantity), 
        func.sum(OffresStep4.totaleHT),
        func.sum(OffresStep4.totaleTTC),
        ).filter(OffresStep4.idOffre==idOffreSend).group_by(OffresStep4.idOffre)

    for _res in qry.all():
        selectRequette.append(int(_res[0]))
        selectRequette.append(_res[1])
        selectRequette.append(_res[2])

    print(selectRequette)
    pS4 = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend)
    for i in pS4:
        valProp = i.globalProposition
        valMargeNette = i.globalMargeNete

    neg = session.query(Negotiation).filter(Negotiation.idOffre == idOffreSend).first()
    neg.globalPropositionStPrWR = valProp + selectRequette[1]
    neg.globalMargeNetteStPrWR = 0
    print(neg.globalPropositionStPrWR)
    session.commit()
    return 1
