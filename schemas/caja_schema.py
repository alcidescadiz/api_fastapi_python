from pydantic import BaseModel

class Caja(BaseModel):
    fecha: str
    tipo: str
    descripcion: str
    ingreso: float
    egreso: float