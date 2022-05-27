import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
import base64
import itertools


from DBConnexion import *
from GlobalOffre import *
from Negotiation import *
from OffresStep1 import *
from OffresStep2 import *
from OffresStep3 import *
from OffresStep4 import *
def getAllOffres(phoneNumber):
    statusList = []
    selectRequette=[]
    selectRequette2=[]
    
    nego = session.query(Negotiation)
    for neg in nego:
        statusList.append(neg.status)

    for statLis in statusList:
        print(statLis)
        if(statLis== None):
            print("Yeah bro")
        else:
            print(phoneNumber)
            compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumber)
            for cp in compan:
                selectRequette.append(cp.companyId)

            gONeg = session.query(GlobalOffre,Negotiation).filter(and_(GlobalOffre.companyId==selectRequette[0],GlobalOffre.idOffre==Negotiation.idOffre,or_(Negotiation.status=="warning",Negotiation.status=="danger",Negotiation.status=="success")))      
            for go,neg in gONeg:
                selectRequette2.append(AllOffres(go.idOffre,neg.globalPropositionStPrWR,neg.globalMargeNetteStPrWR,go.totaleFinalHT,go.dateCreation,neg.nomNegociateur,neg.status,neg.remisePercent,neg.description))
            print(selectRequette2)
            return selectRequette2

def getAllOffresFromDB(phoneNumber):
    selectRequette = []
    selectRequette2 = []
    print(phoneNumber)
    compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumber)
    for cp in compan:
        selectRequette.append(cp.companyId)

    gONeg = session.query(GlobalOffre,OffresStep1,OffresStep2,OffresStep3,OffresStep4).filter(and_(GlobalOffre.companyId==selectRequette[0],GlobalOffre.idOffre==OffresStep1.idOffre,GlobalOffre.idOffre==OffresStep2.idOffre,GlobalOffre.idOffre==OffresStep3.idOffre,or_(GlobalOffre.idOffre==OffresStep4.idOffre))).group_by(GlobalOffre.idOffre)
    for go,os1,os2,os3,os4 in gONeg:
        print(go.idOffre)
        print(go.dateCreation)
        print(os1.totaleProposition)
        print(os2.totaleProposition)
        print(os3.totaleProposition)
        print(go.margeNetTotalefromStep4)
        print(go.prixRevientTotalefromStep4)
        selectRequette2.append(AllOffresFromDB(go.idOffre,go.dateCreation,os1.totaleProposition,os2.totaleProposition,os3.totaleProposition,go.margeNetTotalefromStep4,go.prixRevientTotalefromStep4))
    # print(selectRequette2)
    return selectRequette2



def getOffreFromArchivesDB(idOffreSendGlobal):
    selectRequette1 = []
    gONeg = session.query(GlobalOffre,Negotiation).filter(and_(GlobalOffre.idOffre==idOffreSendGlobal,GlobalOffre.idOffre==Negotiation.idOffre))      
    for go,neg in gONeg:
        print(neg.globalPropositionStPrWR)
        selectRequette1.append(AllOffres(go.idOffre,neg.globalPropositionStPrWR,neg.globalMargeNetteStPrWR,go.totaleFinalHT
        ,go.dateCreation,neg.nomNegociateur,neg.status,neg.remisePercent,neg.description))

    print(selectRequette1)
    return selectRequette1

def updateInformationOffreNegociationDB(idOffre,nomNegociateurSend,remiseSend,statusSend):
    selRequette = []
    selectRequette = []
    selectRequette1 = []
    selectRequette4 = []
    selectRequette5 = []
    selectRequette6 = []
    selectRequette7 = []
    priceRevient = 0
    newRemisPercent = 0
    totHT = 0
    print(remiseSend)

    gONeg = session.query(GlobalOffre,Negotiation).filter(and_(GlobalOffre.idOffre==idOffre,GlobalOffre.idOffre==Negotiation.idOffre))      
    for go,neg in gONeg:
        print(go.globalMargeNete)
        selectRequette6.append(go.prixRevientTotalefromStep4)
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        # print(selectRequette6)
        if(not selectRequette6):
            newGlobMargNette = go.globalMargeNete * (1-(remiseSend/100))
            substractionOfProposition = go.globalMargeNete - go.globalMargeNete * (1-(remiseSend/100))
            newGlobProposition = go.globalProposition - substractionOfProposition
        else:
            globOffrePRMN = session.query(GlobalOffre).filter(GlobalOffre.idOffre==idOffre)
            for goprmn in globOffrePRMN:
                selectRequette7.append(goprmn.prixRevientTotalefromStep4)
                selectRequette7.append(goprmn.margeNetTotalefromStep4)
            offresStep4 = session.query(OffresStep4).filter(OffresStep4.idOffre==idOffre)
            for ofSt4 in offresStep4:
                totHT += ofSt4.totaleHT
            
            print(totHT)
            print(selectRequette7[1])

            globaleProposition = go.globalProposition + totHT
            margeNetOfGO = go.globalMargeNete + selectRequette7[1]

            print(globaleProposition)
            print(margeNetOfGO)

            newGlobMargNette = margeNetOfGO * (1-(remiseSend/100))
            substractionOfProposition = margeNetOfGO - newGlobMargNette
            newGlobProposition = globaleProposition - substractionOfProposition

    if (statusSend == "warning"):
        descriptionSend= "En Négociation"
    elif (statusSend == "danger"):
        descriptionSend = "Rejected"
    elif (statusSend == "success"):
        descriptionSend = "Completed"

    
    nego2 = session.query(Negotiation).filter(Negotiation.idOffre==idOffre).first()
    nego2.nomNegociateur= nomNegociateurSend
    nego2.remisePercent = remiseSend
    nego2.status = statusSend
    nego2.globalPropositionStPrWR = newGlobProposition
    nego2.globalMargeNetteStPrWR = newGlobMargNette
    nego2.description = descriptionSend
    session.commit()

    return 1
