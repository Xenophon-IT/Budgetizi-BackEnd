import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
import base64

from DBConnexion import *
from GlobalOffre import *
from Negotiation import *

def getAllOffres(phoneNumber):
    print(phoneNumber)
    selectRequette=[]
    selectRequette2=[]
    compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumber)
    for cp in compan:
        selectRequette.append(cp.companyId)

    gONeg = session.query(GlobalOffre,Negotiation).filter(and_(GlobalOffre.companyId==selectRequette[0],GlobalOffre.idOffre==Negotiation.idOffre))      
    for go,neg in gONeg:
        selectRequette2.append(AllOffres(go.idOffre,neg.globalPropositionStPrWR,neg.globalMargeNetteStPrWR,go.totaleFinalHT,go.dateCreation,neg.nomNegociateur,neg.status,neg.remisePercent,neg.description))
    print(selectRequette2)
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
    # print(idOffre)
    # print(nomNegociateurSend)
    # print(remiseSend)
    # print(statusSend)
    print("eeeeeeeeeeeeee")
    selectRequette1 = []
    gONeg = session.query(GlobalOffre,Negotiation).filter(and_(GlobalOffre.idOffre==idOffre,GlobalOffre.idOffre==Negotiation.idOffre))      
    for go,neg in gONeg:
        newGlobMargNette = go.globalMargeNete * (1-(remiseSend/100))
        substractionOfProposition = go.globalMargeNete - newGlobMargNette
        print(go.globalPropositionStPr)
        newGlobProposition = go.globalPropositionStPr - substractionOfProposition

    print(newGlobMargNette)
    print(substractionOfProposition)
    print(newGlobProposition)

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
