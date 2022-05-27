import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
from DBConnexion import *
from GlobalOffre import *

class OffresStep1Model():
    def __init__(self,idOffre,CostsGlobale,totaleProposition,totaleRevient,totaleQtyWork,totaleMargeBrute,totaleMargeNet,totaleMargeNetPC):
        self.idOffre = idOffre
        self.CostsGlobale = CostsGlobale
        self.totaleProposition = totaleProposition
        self.totaleRevient = totaleRevient
        self.totaleQtyWork = totaleQtyWork
        self.totaleMargeBrute = totaleMargeBrute
        self.totaleMargeNet = totaleMargeNet
        self.totaleMargeNetPC = totaleMargeNetPC


class OffresStep1(Base):
    __tablename__ = 'OffresStep1'
    idOffre = Column(String(255), ForeignKey(GlobalOffre.idOffre), primary_key=True)
    CostsGlobale = Column(Float, nullable=True)
    totaleProposition = Column(Float, nullable=True)
    totaleRevient = Column(Float, nullable=True)
    totaleQtyWork = Column(Float, nullable=True)
    totaleMargeBrute = Column(Float, nullable=True)
    totaleMargeNet = Column(Float, nullable=True)
    totaleMargeNetPC = Column(Float, nullable=True)

Base.metadata.create_all(engine)