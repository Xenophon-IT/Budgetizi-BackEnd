from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

import sys         
# sys.path.append('D:\Dali\B.IZI.V.Alfa\ButGitizi\Partie-BackEnd\ScriptsBack-End')
sys.path.append('D:\Xenophon-IT\ButGitizi\Budgetizi-BackEnd\ScriptsBack-End')

from Clients import *
from Companies import *
from WorkerCompanys import *
from OffreStep1 import *
from OffreStep2 import *
from OffreStep3 import *
from OffreStep4 import *
from OffreFinaleStep import *
from ArchivesOffres import *
from PrintOffres import *

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:4300",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from ServerClients import *
from ServerCompany import *
from ServerWorker import *
from ServerStep1Offre import *
from ServerStep2Offre import *
from ServerStep3Offre import *
from ServerStep4Offre import *
from ServerFinalOffre import *
from ServerArchivesOffres import *
from ServerPrintOffres import *

if __name__ == "__main__":
    uvicorn.run("ServerMain:app", host="localhost", port=5050, reload=True)