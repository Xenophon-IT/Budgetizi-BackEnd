import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\DB')
from DBConnexion import *
from ClientCompany import *
import jwt
import base64

#Function for signup of each user of our application
def sginUpClient(firstName,lastName,emailUser,phoneUser,passwordUser,imageUser):
    checkEmail = []
    resultSignUp = 0
    #We use JWT to encode the password in database
    print(passwordUser)
    passwordOnJWT = jwt.encode({"passwordClient": passwordUser}, "xenophon-IT_ButGitizi", algorithm="HS256")
    lenImage = len(imageUser)
    rowsInClCom = session.query(ClientCompany).count()
    profileImageChange = imageUser.encode('ascii')
    profileImageBin = base64.b64encode(profileImageChange)
    # print(profileImageBin)

    #In this bloc we check if the email is use it and also the phone of user
    try:
        clCom = session.query(ClientCompany).filter(ClientCompany.email==str(emailUser))
        for i in clCom:
            checkEmail.append(i.email)
        if(checkEmail):
            print(clCom)
            print("The email is use it")
            resultSignUp = 0
        else:
            try:
                print(phoneUser)
                session.add(ClientCompany(clientCompanyId=rowsInClCom+1,firstName=firstName,lastName=lastName,email=emailUser,phoneNumber=phoneUser,passwordClient=passwordOnJWT,imageClient=profileImageBin,lenImageClient=lenImage,verifNumber=6521))
                session.commit()
                resultSignUp = 1
            except:
                print("The phone number is use it")
                resultSignUp = 0
    except:
        print("It's a problem in the bloc of signup of client")
        resultSignUp = 0
    
    return resultSignUp


#Function for signin of our user
def signInWithEmailAndPassword(emailAdress,passwordUser):
    selectRequette=[]
    passwordOnJWT = jwt.encode({"passwordClient": passwordUser}, "xenophon-IT_ButGitizi", algorithm="HS256")
    
    clientCompany = session.query(ClientCompany).filter(and_(ClientCompany.email == emailAdress, ClientCompany.passwordClient == passwordOnJWT))

    for cC in clientCompany:
        selectRequette.append(cC.clientCompanyId)
        phoneNumber = jwt.encode({"phoneNumber": cC.phoneNumber}, "xenophon-IT_ButGitizi", algorithm="HS256")
        selectRequette.append(phoneNumber)

    print(selectRequette[1])
    return(selectRequette)

#Function for check the code of sms
def checkTheCodeFromDB(emailAdress,codeNotif):
    selectRequette=""
    clientCompany = session.query(ClientCompany).filter(or_(ClientCompany.verifNumber == codeNotif, ClientCompany.email == emailAdress))
    for cC in clientCompany:
        selectRequette = cC.verifNumber
    return selectRequette

#Function for get all the information of our user
def getInformationClientFromDB(emailAdress):
    selectRequette = []
    clientCompany = session.query(ClientCompany).filter(ClientCompany.email == emailAdress)
    for cC in clientCompany:
        selectRequette.append(cC.clientCompanyId)
        selectRequette.append(cC.firstName)
        selectRequette.append(cC.lastName)
        selectRequette.append(cC.email)
        phoneNumber = jwt.encode({"phoneNumber": cC.phoneNumber}, "xenophon-IT_ButGitizi", algorithm="HS256")
        selectRequette.append(phoneNumber)
        selectRequette.append(jwt.decode(cC.passwordClient, "xenophon-IT_ButGitizi", algorithms=["HS256"])['passwordClient'])
        # print(base64.b64decode(cC.imageClient.decode('ascii')))
        selectRequette.append(base64.b64decode(cC.imageClient.decode('ascii')).decode("utf-8"))
        selectRequette.append(cC.lenImageClient)
        selectRequette.append(cC.verifNumber)
    
    return selectRequette


#Function for get all the information of our user with phone number
def getInformationClientDB(phoneUserNumber):
    selectRequette = []
    clientCompany = session.query(ClientCompany).filter(ClientCompany.phoneNumber == phoneUserNumber)
    for cC in clientCompany:
        selectRequette.append(cC.clientCompanyId)
        selectRequette.append(cC.firstName)
        selectRequette.append(cC.lastName)
        selectRequette.append(cC.email)
        phoneNumber = jwt.encode({"phoneNumber": cC.phoneNumber}, "xenophon-IT_ButGitizi", algorithm="HS256")
        selectRequette.append(phoneNumber)
        selectRequette.append(jwt.decode(cC.passwordClient, "xenophon-IT_ButGitizi", algorithms=["HS256"])['passwordClient'])
        selectRequette.append(base64.b64decode(cC.imageClient.decode('ascii')))
        selectRequette.append(cC.lenImageClient)
        selectRequette.append(cC.verifNumber)

    return selectRequette


#Function for edit the information of Client Company
def EditInformationOfClientCompanyDB(phoneUserNumber,userProfileImageToDB,FirstNameToDB,LastNameToDB,emailProfileToDB,passwordProfileToDB):

    profileImageChange = userProfileImageToDB.encode('ascii')
    profileImageBin = base64.b64encode(profileImageChange)

    #We use JWT to encode the password in database
    passwordOnJWT = jwt.encode({"passwordClient": passwordProfileToDB}, "xenophon-IT_ButGitizi", algorithm="HS256")

    company = session.query(ClientCompany).filter(ClientCompany.phoneNumber==phoneUserNumber).first()
    company.firstName = FirstNameToDB
    company.lastName = LastNameToDB
    company.email = emailProfileToDB
    company.passwordClient = passwordOnJWT
    company.imageClient = profileImageBin

    session.commit()

    print("Sucess Update into table Client Company !")
    return 1


# getInformationClientDB("+21653786397")
# getInformationClientFromDB("meddalijaziri@gmail.com")
