import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Servers')

from ServerMain import *

#This request post for signup Client
@app.post("/client/signupClient")
async def signUpClient(request: Request):
    req = await request.json()
    dataSend = req['dataSend']
    #This is input of the dataSend object request
    imageUser = req['imageUser']
    firstName = dataSend["firstName"]
    lastName = dataSend["lastName"]
    emailUser = dataSend["emailUser"]
    phoneNumber = dataSend["phoneUser"]
    passwordUser = dataSend["passwordUser"]


    #This function is for register of our client and you find it in the file named by BackendScript
    resultSignUp = sginUpClient(firstName,lastName,emailUser,phoneNumber,passwordUser,imageUser)

    return {
        "resultSignUp": resultSignUp # 0: the phone number is use it | 1: ok ok
    }

#This request post for signup Client
@app.post("/client/signIn")
async def signInClient(request: Request):
    req = await request.json()
    dataSend = req['dataSend']
    #This is input of the dataSend object request
    emailAdress = dataSend["emailAdress"]
    passwordUser = dataSend["passwordUser"]

    resultLogin = signInWithEmailAndPassword(emailAdress,passwordUser)
    if(not resultLogin):
        variableLogin = 0
        print("Login not sucess")
    else:
        variableLogin = 1
        print("Login sucess")

    return {
        "resultLogin" : resultLogin,
        "variableLogin" : variableLogin
    }

#This request post for check the code sms
@app.post("/client/checkCodeNotif")
async def checkCodeNotif(request: Request):
    req = await request.json()
    dataSend = req['dataSend']
    dataSend2 = req['dataSend2']
    codeNotif = dataSend['codeNotif']
    emailAdress = dataSend2['emailAdress']

    resutFunction = checkTheCodeFromDB(emailAdress,codeNotif)

    print(resutFunction)
    if(not resutFunction):
        variableCodeCheck = 0
        print("There's not code !")
    else:
        variableCodeCheck = 1
        print("The code it's right !")

    return {
        "variableCodeCheck": variableCodeCheck
    }


#This request post for get all the informations of our user
@app.post("/client/getInformationClient")
async def getInformationClient(request: Request):
    req = await request.json()
    dataSend2 = req['dataSend2']
    emailAdress = dataSend2['emailAdress']

    resutFunction = getInformationClientFromDB(emailAdress)

    return {
        "resutFunction" : resutFunction
    }

#This request post for get the informations of user companys 
@app.post("/client/ClientCompany")
async def getInformationFromClientDB(request: Request):
    req = await request.json()
    phoneNumber = req['phoneNumber']

    resutFunction = getInformationClientDB(phoneNumber)

    return {
        "resutFunction" : resutFunction
    }

#This request post for edit the informations of user companys 
@app.post("/client/updateInfoClientCompany")
async def editInfoClientCompany(request: Request):
    req = await request.json()
    phoneNumber = req['phoneNumber']
    userProfileImageToDB = req['userProfileImageToDB']
    FirstNameToDB = req['FirstNameToDB']
    LastNameToDB = req['LastNameToDB']
    emailProfileToDB = req['emailProfileToDB']
    passwordProfileToDB = req['passwordProfileToDB']
    
    resutFunction = EditInformationOfClientCompanyDB(phoneNumber,userProfileImageToDB,FirstNameToDB,LastNameToDB,emailProfileToDB,passwordProfileToDB)

    return {
        "resutFunction" : resutFunction
    }