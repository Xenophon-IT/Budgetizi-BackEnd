import sys         
sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
from DBConnexion import *
from Company import *

class GlobalOffreModel():
    def __init__(self,idOffre,globalDaysOfWork,globalProposition,globalRevient,globalRevientAndFG,globalMargeBrute,globalMargeNete,globalFinaleMarge,companyId):
        self.idOffre = idOffre
        self.globalDaysOfWork  = globalDaysOfWork
        self.globalProposition = globalProposition
        self.globalRevient = globalRevient
        self.globalRevientAndFG = globalRevientAndFG
        self.globalMargeBrute = globalMargeBrute
        self.globalMargeNete = globalMargeNete
        self.globalFinaleMarge = globalFinaleMarge
        self.companyId = companyId

class GlobalOffre(Base):
    __tablename__ = 'GlobalOffre'
    idOffre = Column(String(255), primary_key=True)
    globalDaysOfWork  = Column(Integer, nullable=True)
    globalProposition = Column(Float, nullable=True)
    globalRevient = Column(Float, nullable=True)
    globalRevientAndFG = Column(Float, nullable=True)
    globalMargeBrute = Column(Float, nullable=True)
    globalMargeNete = Column(Float, nullable=True)
    globalFinaleMarge = Column(Float, nullable=True)
    companyId = Column(Integer, ForeignKey(Company.companyId),nullable=True)

Base.metadata.create_all(engine)
