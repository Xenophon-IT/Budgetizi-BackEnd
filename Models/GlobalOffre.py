import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
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


class GlobalOffreFinal():
    def __init__(self,idOffre,globalDaysOfWork,globalProposition,globalRevient,globalRevientAndFG,globalMargeBrute,globalMargeNete,globalFinaleMarge,totaleFinalHT,totaleFinalTTC,companyId):
        self.idOffre = idOffre
        self.globalDaysOfWork  = globalDaysOfWork
        self.globalProposition = globalProposition
        self.globalRevient = globalRevient
        self.globalRevientAndFG = globalRevientAndFG
        self.globalMargeBrute = globalMargeBrute
        self.globalMargeNete = globalMargeNete
        self.globalFinaleMarge = globalFinaleMarge
        self.totaleFinalHT = totaleFinalHT
        self.totaleFinalTTC = totaleFinalTTC
        self.companyId = companyId


class AllOffres():
    def __init__(self,idOffre,globalPropositionStPrWR,globalMargeNete,totaleFinalHT,dateCreation,nomNegociateur,status,remisePercent,description):
        self.idOffre = idOffre
        self.globalPropositionStPrWR = globalPropositionStPrWR
        self.globalMargeNete = globalMargeNete
        self.totaleFinalHT = totaleFinalHT
        self.dateCreation = dateCreation
        self.nomNegociateur = nomNegociateur
        self.status = status
        self.remisePercent = remisePercent
        self.description = description

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
    globalPropositionStPr = Column(Float, nullable=True)
    totaleFinalHT = Column(Float, nullable=True)
    totaleFinalTTC = Column(Float, nullable=True)
    dateCreation = Column(String(255), nullable=True)
    companyId = Column(Integer, ForeignKey(Company.companyId),nullable=True)

Base.metadata.create_all(engine)
