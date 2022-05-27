import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB') 
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  

from DBConnexion import *
from ClientCompany import *

class Company(Base):
    __tablename__ = 'Company'
    companyId = Column(Integer, primary_key=True, autoincrement=True) 
    nameCompany  = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    activity = Column(String(255), nullable=True)
    nbOfWorker = Column(String(255), nullable=True)
    currency = Column(String(255), nullable=True)
    creationDate = Column(Date, nullable=True)
    logoCompany = Column(LargeBinary(length=(2**32)-1), nullable=True)
    telePhone = Column(String(255), nullable=True)
    cellNumber = Column(String(255), nullable=True)
    taxRegNum = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    addressCompany = Column(String(255), nullable=True)
    City = Column(String(255), nullable=True)
    ZIPCode = Column(Integer, nullable=True)
    addressLocal = Column(String(255), nullable=True)
    webSite = Column(String(255), nullable=True)
    firstNameCEO = Column(String(255), nullable=True)
    lastNameCEO = Column(String(255),nullable=True)
    phoneNumberClientCompany = Column(String(255), ForeignKey(ClientCompany.phoneNumber), nullable=True)

Base.metadata.create_all(engine)