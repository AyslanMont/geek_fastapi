from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from src.secao03.models import Curso

app = FastAPI()

cursos = dict()


@app.get("/cursos/")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int = Path(default=None, title="ID do curso", description="Deve ser 1 ou 2", gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})

        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!")


@app.post("/cursos/{curso_id}", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    curso_id = len(cursos) + 1
    curso.id = curso_id
    cursos[curso_id] = curso

    return curso


@app.put("/cursos/{curso_id}/")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        curso.id = curso_id
        cursos[curso_id] = curso

        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!")


@app.delete("/cursos/{curso_id}/")
async def del_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!")


