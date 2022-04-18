# Import the required modules
import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\DB')
from DBConnexion import *
from Company import *
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
        selectRequette.append(comp.phoneNumberClientCompany)
        selectRequette.append(comp.webSite)
        selectRequette.append(comp.firstNameCEO)
        selectRequette.append(comp.lastNameCEO)
    return selectRequette

def EditInformationOfCompanyDB(phoneUserNumber,nameCompanySend,telePhoneSend,cellNumberSend,webSiteSend,firstNameProfileSend,lastNameProfileSend,
emailUserCompanySend,citySend,zipCodeSend,logoCompanySend,addressCompanySend,taxRegNumSend):
    
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

    session.commit()

    print("Sucess Update into table company !")