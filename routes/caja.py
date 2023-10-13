from fastapi import FastAPI, APIRouter,HTTPException
from controllers.caja_controllers import caja_controllers
from schemas.caja_schema import Caja

app = FastAPI()
    
router = APIRouter()

@router.get("/", description='Obtener todas las cajas')
async def getAllCajas():
    rows= caja_controllers.get_all_cajas()
    return {"cajas": rows}

@router.get("/{id}", description='Obtener una caja por su Id')
async def getOneCaja(id: int):
    rows= caja_controllers.get_one_caja(id)
    return {"caja": rows}

@router.post("/", description='Añadir una caja a la tabla')
async def createCaja(caja: Caja):
    #fecha, tipo, descripcion, ingreso, egreso = caja
    #print(fecha, descripcion, ingreso, egreso)
    row = caja_controllers.create_caja(caja)
    if row == 0:
        raise HTTPException(
            status_code=404,
            detail="Caja no se ha podido añadir",
            headers={"X-Error": "Error encontrado"},
        )
    return {"caja": caja}
    
@router.put("/{id}", description='Editar una caja en la tabla dado su id')
async def editCaja(id: int,caja: Caja):
    row = caja_controllers.edit_caja(caja,id)
    if row == 0:
        raise HTTPException(
            status_code=404,
            detail="Caja no encontrada para editar",
            headers={"X-Error": "Error encontrado"},
        )
    return {"caja": caja}

@router.delete("/{id}", description='Eliminar una caja por su Id')
async def deleteOneCaja(id: int):
    row= caja_controllers.delete_one_caja(id)
    if row == 0:
        raise HTTPException(
            status_code=404,
            detail="Caja no encontrada",
            headers={"X-Error": "Error encontrado"},
        )
    return {"info": f"ha sido eliminado la caja de id {id}"}
