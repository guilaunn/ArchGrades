import logging

from fastapi import FastAPI

from app.api import status
from app.api import insert_notas
from app.database.database_session import global_init

log = logging.getLogger("uvicorn")

#Criação das rotas da api
def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(
        status.router,
        tags=["Hello"],
        prefix="/api/v1"
    )
    application.include_router(
        insert_notas.router
    )
    return application


app = create_application()

#iniciando a api e chamando o método para criação do banco
@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    global_init()
