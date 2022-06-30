from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from typing import Optional
import psycopg2
from app.config import Settings, get_settings
import os

router = APIRouter()
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

class Notas(BaseModel):
    id: Optional[int]
    idaluno: Optional[int]
    n1: int
    n2: int
    n3: int
    n4: int

#Rota para a inserção de notas
@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(nota: Notas, idaluno: int, n1: int, n2: int, n3: int, n4: int, settings: Settings = Depends(get_settings)):
    con = psycopg2.connect(host="localhost", database="ArchDB", user="admin", password="admin")
    cur = con.cursor()
    insert_notas = f"insert into notas values (default,{idaluno}, {n1}, {n2}, {n3}, {n4} )"
    cur.execute(insert_notas)
    con.commit()
    con.close()
    if idaluno and n1 and n2 and n3 and n4:
        return {
            "id": nota.id,
            "idaluno": idaluno,
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "n4": n4
        }