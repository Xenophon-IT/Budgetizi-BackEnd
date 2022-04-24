import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  
from DBConnexion import *
from GlobalOffre import *

class OffresStep4Model():
    def __init__(self,idOffre,referenceProduit,nomProduit,prixUnitaire,quantity,marge,remise,totaleApresMarge,totaleApresRemise,totaleHT,totaleTTC):
        self.idOffre = idOffre
        self.referenceProduit = referenceProduit
        self.nomProduit = nomProduit
        self.prixUnitaire = prixUnitaire
        self.quantity = quantity
        self.marge = marge
        self.remise = remise
        self.totaleApresMarge = totaleApresMarge
        self.totaleApresRemise = totaleApresRemise
        self.totaleHT = totaleHT
        self.totaleTTC = totaleTTC

class OffresStep4(Base):
    __tablename__ = 'OffresStep4'
    idOffre = Column(String(255), ForeignKey(GlobalOffre.idOffre))
    referenceProduit = Column(String(255), nullable=True)
    nomProduit = Column(String(255), nullable=True)
    prixUnitaire = Column(Float, nullable=True)
    quantity = Column(Integer, nullable=True)
    marge = Column(Integer, nullable=True)
    remise = Column(Integer, nullable=True)
    totaleApresMarge = Column(Float, nullable=True)
    totaleApresRemise = Column(Float, nullable=True)
    totaleHT = Column(Float, nullable=True)
    totaleTTC = Column(Float, nullable=True)
    description = Column(String(255), nullable=True)
    PrimaryKeyConstraint(idOffre,referenceProduit)

Base.metadata.create_all(engine)