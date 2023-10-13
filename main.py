from fastapi import FastAPI
from routes.caja import router

app = FastAPI(title='Api Ejemplo con Python',version='0.01',description='Elaborado por Ing. Alcides Cádiz')

app.include_router(router, prefix="/caja", tags=["Caja"])


# LEVANTAR EL SERVIDOR CON:
# env\Scripts\activate  // activar entorno virtual
# uvicorn main:app --reload //  py -m uvicorn main:app