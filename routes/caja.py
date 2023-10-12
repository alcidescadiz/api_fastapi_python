from fastapi import FastAPI, APIRouter
from controllers.caja_controllers import caja_controllers
from schemas.caja_schema import Caja

app = FastAPI()
    
router = APIRouter()

@router.get("/")
async def getAllCajas():
    rows= caja_controllers.get_all_cajas()
    return {"cajas": rows}

@router.get("/{id}")
async def getOneCaja(id: int):
    rows= caja_controllers.get_one_caja(id)
    return {"caja": rows}

@router.post("/")
async def createCaja(caja: Caja):
    caja_controllers.create_caja(caja)
    return {"caja": caja}