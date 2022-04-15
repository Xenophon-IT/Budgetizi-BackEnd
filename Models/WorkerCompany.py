import sys         
sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
from DBConnexion import *
from Company import *

class WorkerCompanyModel():
    def __init__(self, idWorker,fullName,profession,departName,profCoefficient,profileWork,yearCreationCompte,companyId,salary):
        self.idWorker = idWorker
        self.fullName = fullName
        self.profession = profession
        self.departName = departName
        self.profCoefficient = profCoefficient
        self.profileWork = profileWork
        self.yearCreationCompte = yearCreationCompte
        self.companyId = companyId
        self.salary = salary

class WorkerCompany(Base):
    def WorkerCompany(self, idWorker,fullName,profession,departName,profCoefficient,profileWork,yearCreationCompte,companyId,salary):
        self.idWorker = idWorker
        self.fullName = fullName
        self.profession = profession
        self.departName = departName
        self.profCoefficient = profCoefficient
        self.profileWork = profileWork
        self.yearCreationCompte = yearCreationCompte
        self.companyId = companyId
        self.salary = salary

    __tablename__ = 'WorkerCompany'
    idWorker = Column(Integer, primary_key=True, autoincrement=True) 
    fullName  = Column(String(255), nullable=True)
    profession  = Column(String(255), nullable=True)
    departName  = Column(String(255), nullable=True)
    profCoefficient  = Column(Float, nullable=True)
    profileWork  = Column(LargeBinary(length=(2**32)-1), nullable=True)
    yearCreationCompte  = Column(String(255), nullable=True)
    companyId = Column(Integer, ForeignKey(Company.companyId), nullable=True)

Base.metadata.create_all(engine)