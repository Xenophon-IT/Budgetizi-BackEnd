# Import the required modules
import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
from DBConnexion import *
from Company import *
from GlobalOffre import *
from Negotiation import *
from OffresStep1 import *
from OffresStep2 import *
from OffresStep3 import *
from OffresStep4 import *
import base64
#import jwt
from datetime import date

def sginUpCompany(nameCompany,companAct,country,currency,phoneUser):
    resultSignUp = 0
    selectRequette=""
    logoCompanyInLocal="D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\Images\ButGitizi-01.png"
    # Open a file in binary mode

    with open(logoCompanyInLocal, "rb") as img_file:
        file = base64.b64encode(img_file.read())
    logoBinnary = file.decode('utf-8')

    profileImageChange = logoBinnary.encode('ascii')
    logoBinnary2 = base64.b64encode(profileImageChange)

    # print(logoBinnary2)
    # resultSignUp = 1
    company = session.query(Company).filter(Company.nameCompany == nameCompany)
    for comp in company:
        selectRequette = comp.nameCompany
        
    if(not selectRequette):
        creationDate = date.today()
        print(nameCompany)
        print(country)
        print(companAct)
        print(currency)
        print(creationDate)
        print(len(logoBinnary2))
        print(phoneUser)

        session.add(Company(nameCompany=nameCompany,country=country,activity=companAct,currency=currency,creationDate=creationDate,logoCompany=logoBinnary2,phoneNumberClientCompany=phoneUser))
        session.commit()
        resultSignUp = 1
        print("Sucess in table Company") 

    else:
        resultSignUp = 0
        print("The name company is use it")

    return resultSignUp

def getInformationCompanyDB(phoneUserNumber):
    print(phoneUserNumber)
    selectRequette=[]
    company = session.query(Company).filter(Company.phoneNumberClientCompany == phoneUserNumber)
    for comp in company:
        selectRequette.append(comp.companyId)
        selectRequette.append(comp.nameCompany)
        selectRequette.append(comp.country)
        selectRequette.append(comp.activity)
        selectRequette.append(comp.nbOfWorker)
        selectRequette.append(comp.currency)
        selectRequette.append(comp.creationDate)
        print(len(comp.logoCompany.decode('ascii')))
        if(len(comp.logoCompany.decode('ascii'))==5744):
            selectRequette.append("data:image/jpeg;base64,"+(base64.b64decode(comp.logoCompany.decode('ascii'))).decode("utf-8") )
        else:
            selectRequette.append(base64.b64decode(comp.logoCompany.decode('ascii')))
        selectRequette.append(comp.telePhone)
        selectRequette.append(comp.cellNumber)
        selectRequette.append(comp.taxRegNum)
        selectRequette.append(comp.email) 
        selectRequette.append(comp.addressCompany)
        selectRequette.append(comp.City)
        selectRequette.append(comp.ZIPCode)
        selectRequette.append(comp.addressLocal)
        selectRequette.append(comp.phoneNumberClientCompany)
        selectRequette.append(comp.webSite)
        selectRequette.append(comp.firstNameCEO)
        selectRequette.append(comp.lastNameCEO)
    return selectRequette

def EditInformationOfCompanyDB(phoneUserNumber,nameCompanySend,telePhoneSend,cellNumberSend,webSiteSend,firstNameProfileSend,lastNameProfileSend,
emailUserCompanySend,citySend,zipCodeSend,addressLocal,logoCompanySend,addressCompanySend,taxRegNumSend):
    
    logoChange = logoCompanySend.encode('ascii')
    logoCompanyBin = base64.b64encode(logoChange)

    company = session.query(Company).filter(Company.phoneNumberClientCompany==phoneUserNumber).first()
    company.nameCompany = nameCompanySend
    company.telePhone = telePhoneSend
    company.cellNumber = cellNumberSend
    company.webSite = webSiteSend
    company.firstNameCEO = firstNameProfileSend
    company.lastNameCEO = lastNameProfileSend
    company.email = emailUserCompanySend
    company.City = citySend
    company.logoCompany =logoCompanyBin
    company.addressCompany = addressCompanySend
    company.taxRegNum = taxRegNumSend
    company.ZIPCode = zipCodeSend
    company.addressLocal = addressLocal

    session.commit()

    print("Sucess Update into table company !")

def getAllNesscaryInformationDB(idOffreSend,phoneNumber):
    print(idOffreSend, phoneNumber)

    selectRequette = []
    selectRequette2 = []
    selectRequette3 = []
    selectRequette4 = []
    selectRequette5 = []
    selectRequette6 = []
    company = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumber)
    for comp in company:
        selectRequette.append(comp.companyId)
        selectRequette.append(comp.nameCompany)
        selectRequette.append(comp.country)
        print(len(comp.logoCompany.decode('ascii')))
        if(len(comp.logoCompany.decode('ascii'))==5744):
            selectRequette.append("data:image/jpeg;base64,"+(base64.b64decode(comp.logoCompany.decode('ascii'))).decode("utf-8") )
        else:
            selectRequette.append(base64.b64decode(comp.logoCompany.decode('ascii')))
        selectRequette.append(comp.telePhone)
        selectRequette.append(comp.cellNumber)
        selectRequette.append(comp.email) 
        selectRequette.append(comp.addressCompany)
        selectRequette.append(comp.City)
        selectRequette.append(comp.addressLocal)
        selectRequette.append(comp.ZIPCode)


    offreStepGlobalOffre = session.query(OffresStep1,GlobalOffre).filter(and_(OffresStep1.idOffre==GlobalOffre.idOffre,OffresStep1.idOffre==idOffreSend,GlobalOffre.companyId==selectRequette[0]))

    for oS1, glOff in offreStepGlobalOffre:
        selectRequette2.append(OffresStep1Model(glOff.idOffre,oS1.CostsGlobale,oS1.totaleProposition,oS1.totaleRevient,oS1.totaleQtyWork,oS1.totaleMargeBrute,oS1.totaleMargeNet,oS1.totaleMargeNetPC))

    offreStepGlobalOffre = session.query(OffresStep2,GlobalOffre).filter(and_(OffresStep2.idOffre==GlobalOffre.idOffre,OffresStep2.idOffre==idOffreSend,GlobalOffre.companyId==selectRequette[0]))

    for oS1, glOff in offreStepGlobalOffre:
        selectRequette3.append(OffresStep2Model(glOff.idOffre,oS1.CostsGlobale,oS1.totaleProposition,oS1.totaleRevient,oS1.totaleQtyWork,oS1.totaleMargeBrute,oS1.totaleMargeNet,oS1.totaleMargeNetPC))

    offreStepGlobalOffre = session.query(OffresStep3,GlobalOffre).filter(and_(OffresStep3.idOffre==GlobalOffre.idOffre,OffresStep3.idOffre==idOffreSend,GlobalOffre.companyId==selectRequette[0]))

    for oS1, glOff in offreStepGlobalOffre:
        selectRequette4.append(OffresStep3Model(glOff.idOffre,oS1.CostsGlobale,oS1.totaleProposition,oS1.totaleRevient,oS1.totaleQtyWork,oS1.totaleMargeBrute,oS1.totaleMargeNet,oS1.totaleMargeNetPC))

    globalOffre = session.query(GlobalOffre).filter(GlobalOffre.idOffre==idOffreSend)      
    for go in globalOffre:
        selectRequette5.append(go.globalPropositionStPr)
        selectRequette5.append(go.totaleFinalHT)
        selectRequette5.append(go.totaleFinalTTC)


    gONeg = session.query(GlobalOffre,Negotiation).filter(and_(GlobalOffre.idOffre==idOffreSend,GlobalOffre.idOffre==Negotiation.idOffre))      
    for go,neg in gONeg:
        selectRequette6.append(AllOffres(go.idOffre,neg.globalPropositionStPrWR,go.globalMargeNete,go.totaleFinalHT
        ,go.dateCreation,neg.nomNegociateur,neg.status,neg.remisePercent,neg.description))

    return (selectRequette,selectRequette2,selectRequette3,selectRequette4,selectRequette5,selectRequette6)


# print(getAllNesscaryInformationDB("JustGroup-01","+21653786397"))

def checkTheCurrentCompte(phoneUser,emailProfile):
    lisOfCltComapnies = []
    cltCompany = session.query(ClientCompany).filter(and_(ClientCompany.phoneNumber==phoneUser,ClientCompany.email == emailProfile)).first()
    lisOfCltComapnies.append(cltCompany.phoneNumber)
    if(not lisOfCltComapnies):
        return 0
    else:
        return 1