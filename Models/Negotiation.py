import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
from DBConnexion import *
from GlobalOffre import *

class Negotiation(Base):
    __tablename__ = 'Negotiation'
    idOffre = Column(String(255), ForeignKey(GlobalOffre.idOffre), primary_key=True)
    nomNegociateur = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)
    remisePercent = Column(INTEGER, nullable=True)
    globalPropositionStPrWR = Column(Float, nullable=True)
    globalMargeNetteStPrWR = Column(Float, nullable=True)
    description = Column(String(255), nullable=True)
Base.metadata.create_all(engine)