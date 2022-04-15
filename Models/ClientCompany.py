import sys         
sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
from DBConnexion import *

class ClientCompany(Base):
    def __init__(self, clientCompanyId,firstName,lastName,email,phoneNumber,passwordClient,imageClient,lenImageClient,verifNumber):
        self.clientCompanyId = clientCompanyId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.passwordClient = passwordClient
        self.imageClient = imageClient
        self.lenImageClient = lenImageClient
        self.verifNumber = verifNumber

    __tablename__ = 'ClientCompany'
    clientCompanyId = Column(Integer) 
    firstName  = Column(String(255), nullable=True)
    lastName  = Column(String(255), nullable=True)
    email  = Column(String(255), nullable=True)
    phoneNumber = Column(String(255),primary_key=True)
    passwordClient  = Column(String(255), nullable=True)
    imageClient  = Column(LargeBinary(length=(2**32)-1), nullable=True)
    lenImageClient = Column(Integer, nullable=True)
    verifNumber = Column(Integer, nullable=True)

Base.metadata.create_all(engine)
