import sys         
sys.path.append('D:\Xenophon-IT\ButGitizi\Partie-BackEnd\DB')  
from DBConnexion import *
from GlobalOffre import *
from WorkerCompany import *

class workCGOffreForStep2Model():
    def __init__(self,profileWork,idWorker,fullName,hoursWorkCompany,hoursWorkOutCompany,FG,CostsByWorker,tPropositionByWorker,tRevientByWorker,tMargeBrute,tMargeNet,tMargeNetPC):
        self.profileWork = profileWork
        self.idWorker = idWorker
        self.fullName = fullName
        self.hoursWorkCompany = hoursWorkCompany
        self.hoursWorkOutCompany = hoursWorkOutCompany
        self.FG = FG
        self.CostsByWorker = CostsByWorker
        self.tPropositionByWorker = tPropositionByWorker
        self.tRevientByWorker = tRevientByWorker
        self.tMargeBrute = tMargeBrute
        self.tMargeNet = tMargeNet
        self.tMargeNetPC = tMargeNetPC

class workCGOffreFinalModelStep2():
    def __init__(self,idWorker,idOffre,hoursWorkCompany,hoursWorkOutCompany,FG,CostsByWorker,tPropositionByWorker,tRevientByWorker,tMargeBrute,tMargeNet,tMargeNetPC,profileWork,fullName):
        self.idWorker = idWorker
        self.idOffre = idOffre
        self.hoursWorkCompany = hoursWorkCompany
        self.hoursWorkOutCompany = hoursWorkOutCompany
        self.FG = FG
        self.CostsByWorker = CostsByWorker
        self.tPropositionByWorker = tPropositionByWorker
        self.tRevientByWorker = tRevientByWorker
        self.tMargeBrute = tMargeBrute
        self.tMargeNet = tMargeNet
        self.tMargeNetPC = tMargeNetPC
        self.profileWork = profileWork
        self.fullName = fullName

class workCGOffreForStep2(Base):
    __tablename__ = 'workCGOffreForStep2'
    idWorker = Column(Integer, ForeignKey(WorkerCompany.idWorker))
    idOffre = Column(String(255), ForeignKey(GlobalOffre.idOffre))
    hoursWorkCompany = Column(Integer, nullable=True)
    hoursWorkOutCompany = Column(Integer, nullable=True)
    FG = Column(Integer, nullable=True)
    CostsByWorker = Column(Float,nullable=True)
    tPropositionByWorker = Column(Float, nullable=True)
    tRevientByWorker = Column(Float, nullable=True)
    tMargeBrute = Column(Float, nullable=True)
    tMargeNet = Column(Float, nullable=True)
    tMargeNetPC = Column(Float, nullable=True)
    PrimaryKeyConstraint(idWorker,idOffre)

Base.metadata.create_all(engine)