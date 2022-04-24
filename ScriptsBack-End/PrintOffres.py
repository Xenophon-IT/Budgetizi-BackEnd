import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\DB')  
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\Models')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\DB')  

from DBConnexion import *
from Companies import *
from GlobalOffre import *

def checkCompleteOffreDB(idOffreSend,phoneNumber):
    selectRequette = []
    selectRequette2 = []
    compan = session.query(Company).filter(Company.phoneNumberClientCompany == phoneNumber)
    for cp in compan:
        selectRequette.append(cp.companyId)

    globOff = session.query(GlobalOffre).filter(and_(GlobalOffre.idOffre==idOffreSend,GlobalOffre.companyId==selectRequette[0]))
    for gO in globOff:
        selectRequette2.append(gO.globalPropositionStPr)

    print(selectRequette2)
    if(not selectRequette2):
        return 0
    else:
        if(selectRequette2[0]==0):
            return 0
        return 1