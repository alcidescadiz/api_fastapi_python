from fastapi import FastAPI
from routes.caja import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Api Ejemplo con Python',version='0.01',description='Elaborado por Ing. Alcides Cádiz')
origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:3000",
    "http://localhost"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/", description='Ruta de inicio',tags=["Inicio"])
async def hello():
    return {"inicio": "hola mundo"}

# LEVANTAR EL SERVIDOR CON:
# env\Scripts\activate  // activar entorno virtual
# uvicorn main:app --reload //  py -m uvicorn main:app