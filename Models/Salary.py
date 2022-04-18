import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
sys.path.append('D:\Xenophon-IT\ButGitizi-Xenophon-IT\Budgetizi-BackEnd-ButGitizi-BackEnd-01\DB')  
from DBConnexion import *
from WorkerCompany import *

class Salary(Base):
    __tablename__ = 'Salary'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idWorker = Column(Integer, ForeignKey(WorkerCompany.idWorker), nullable=True)
    salary = Column(Float, nullable=True)
    H_jCostsOnCompany = Column(Float, nullable=True)
    H_jCostsOnSite = Column(Float, nullable=True)
    HCostsOnCompany = Column(Float, nullable=True)
    HCostsOnSite = Column(Float, nullable=True)

Base.metadata.create_all(engine)