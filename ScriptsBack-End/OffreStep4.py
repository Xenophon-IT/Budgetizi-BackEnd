import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
import base64
import itertools

from DBConnexion import *
from GlobalOffre import *
from Company import *
from OffresStep4 import *
from Negotiation import *

# def checkIntoGlobalOffre(idOffre,phoneNumberOfUser):
#     try:
#         selectRequette = []
#         selectRequette2 = []

#         compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
#         for cp in compan:
#             selectRequette.append(cp.companyId)

#         globOff = session.query(GlobalOffre).filter(and_(GlobalOffre.idOffre==idOffre,GlobalOffre.companyId==selectRequette[0]))
#         for gO in globOff:
#             selectRequette2.append(gO.idOffre)
            
#         if (not selectRequette or not selectRequette2):
#             return 0
#         else:
#             return 1
#         print("Sucess check it")
#     except:
#         print("There is a problem please check your data on table GlobalOffre")
#         return 0

def insertIntoOffresStep4(idOffre,ref,nomProduit,pDVHT,quantite,valueSendMarge,valueSendRemise,desc):
    try:
        tMarge = quantite * pDVHT * (valueSendMarge / 100)
        tRemsise = quantite * pDVHT * (valueSendRemise / 100)
        totaleHTProduct = quantite * pDVHT + tMarge - tRemsise
        totaleTTCProduct = totaleHTProduct * 1.19



        session.add(OffresStep4(idOffre=idOffre,referenceProduit=ref,nomProduit=nomProduit,prixUnitaire=pDVHT,quantity=quantite,marge=valueSendMarge,remise=valueSendRemise,totaleApresMarge=tMarge,totaleApresRemise=tRemsise,totaleHT=totaleHTProduct,totaleTTC=totaleTTCProduct,description=desc))
        session.commit()

        print("Sucess add into OffresStep4 table")
        return 1
        
    except:
        print("There is a problem please check your data on table OffresStep4")
        return 0

def getInformationsOfProduct(idOffreSend,phoneNumberOfUser):
    # try:
    selectRequette = []
    selectRequette1 = []
    selectRequette2 = []
    totlaleRevient = 0
    margeNetTot = 0

    comap = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumberOfUser)
    for gO in comap:
        selectRequette1.append(gO.companyId)

    qry = session.query(func.sum(OffresStep4.quantity), 
    func.sum(OffresStep4.totaleHT),
    func.sum(OffresStep4.totaleTTC),
    ).filter(OffresStep4.idOffre==idOffreSend).group_by(OffresStep4.idOffre)


    if(selectRequette1[0]):
        productStep4 = session.query(OffresStep4).filter(OffresStep4.idOffre == idOffreSend)

        for pS4 in productStep4:
            margeNetTot += pS4.totaleHT
            totlaleRevient += pS4.prixUnitaire * pS4.quantity
        margeNetTotale = margeNetTot - totlaleRevient

        # print("Totale Revient: ")
        # print(totlaleRevient)
        # print("Totale Marge: ")
        # print(margeNetTotale)

        # globOffre = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend).first()
        # globOffre.globalMargeNete = globOffre.globalMargeNete + margeNetTotale
        # globOffre.prixRevientTotalefromStep4 = totlaleRevient
        # globOffre.margeNetTotalefromStep4 = margeNetTotale
        # session.commit()

        produStep4 = session.query(OffresStep4).filter(OffresStep4.idOffre == idOffreSend)
        for prodSte4 in produStep4:
            selectRequette2.append(OffresStep4Model(prodSte4.idOffre, prodSte4.referenceProduit, prodSte4.nomProduit, prodSte4.prixUnitaire, prodSte4.quantity, prodSte4.marge, prodSte4.remise, prodSte4.totaleApresMarge, prodSte4.totaleApresRemise, prodSte4.totaleHT, prodSte4.totaleTTC))
        return selectRequette2
    else:
            print("You can acces to the offre step4")
    # except:
    #     print("There is a probleme please try again !!")
        # return 1

def updateInformationOfStep4ToDB(idOffre,referenceProduit,nomProduit,prixUnitaire,quantity,marge,remise):

    print(quantity)
    print(prixUnitaire)
    print(marge)
    print(remise)

    tMarge = (int(quantity) * float(prixUnitaire)) * (int(marge) / 100)
    tRemsise = (int(quantity) * float(prixUnitaire)) * (int(remise) / 100)
    totaleHTProduct = (int(quantity) * float(prixUnitaire)) + tMarge - tRemsise
    totaleTTCProduct = totaleHTProduct * 1.19

    productStep4 = session.query(OffresStep4).filter(and_(OffresStep4.idOffre == idOffre,OffresStep4.referenceProduit== referenceProduit)).first()
    productStep4.nomProduit = nomProduit
    productStep4.prixUnitaire = prixUnitaire
    productStep4.quantity = quantity
    productStep4.marge = marge
    productStep4.remise = remise
    productStep4.totaleApresMarge = tMarge
    productStep4.totaleApresRemise = tRemsise
    productStep4.totaleHT = totaleHTProduct
    session.commit()

def deleteAnWorkerFromOffreStep4UsingDB(idOffre,referenceProduit):
    productForDel = session.query(OffresStep4).filter(and_(OffresStep4.idOffre==idOffre,OffresStep4.referenceProduit==referenceProduit)).first()
    if(not productForDel):
        print("You can do anything is empty")
    else:
        session.delete(productForDel)
        session.commit()
        print("Sucess delete this worker from the offre")
    return 1

def calculPhase4OffreFromDB(idOffreSend):
    selectRequette = []
    selRequette = []
    selectRequette4 = []
    selectRequette5 = []
    priceRevient = 0

    qry = session.query(func.sum(OffresStep4.quantity), 
        func.sum(OffresStep4.totaleHT),
        func.sum(OffresStep4.totaleTTC),
        ).filter(OffresStep4.idOffre==idOffreSend).group_by(OffresStep4.idOffre)

    for _res in qry.all():
        selectRequette.append(int(_res[0]))
        selectRequette.append(_res[1])
        selectRequette.append(_res[2])

    if(not selectRequette):
        print("Is empty !!!")
        pS4 = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend)
        for i in pS4:
            valProp = i.globalProposition

        productStep4 = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend).first()
        productStep4.globalPropositionStPr = valProp
        print(productStep4.globalPropositionStPr)
        print(valProp)
        productStep4.totaleFinalHT = 0
        productStep4.totaleFinalTTC = 0
        session.commit()

        glob = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend).first()
        print(glob.globalMargeNete)
        mageNetFinale = glob.globalMargeNete

        print("Marge Finale")
        print(mageNetFinale)
        nego2 = session.query(Negotiation).filter(Negotiation.idOffre==idOffreSend)  
        nego2.globalMargeNetteStPrWR = mageNetFinale
        session.commit()
        
    else:
        pS4 = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend)
        for i in pS4:
            valProp = i.globalProposition

        print("Hhhhhhhhhhhhhhh")
        print(selectRequette[1])
        print(valProp)
        
        productStep4 = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend).first()
        productStep4.globalPropositionStPr = valProp + selectRequette[1]
        print(productStep4.globalPropositionStPr)
        print(valProp + selectRequette[1])
        productStep4.totaleFinalHT = selectRequette[1]
        productStep4.totaleFinalTTC = selectRequette[2]
        session.commit()

        glob = session.query(GlobalOffre).filter(GlobalOffre.idOffre == idOffreSend).first()
        print(glob.globalMargeNete)
        mageNetFinale = glob.globalMargeNete

        print("Marge Finale")
        print(mageNetFinale)
        nego2 = session.query(Negotiation).filter(Negotiation.idOffre==idOffreSend)  
        nego2.globalMargeNetteStPrWR = mageNetFinale
        session.commit()

    

    