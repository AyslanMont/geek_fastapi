from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from src.secao03.models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 89
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 110,
        "horas": 76
    },
}

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    
@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    curso_id = len(cursos) + 1
    curso.id = curso_id
    cursos[curso_id] = curso 

    return curso