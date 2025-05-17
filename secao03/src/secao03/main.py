from fastapi import FastAPI

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
    curso = cursos[curso_id]
    curso.update({"id": curso_id})
    
    return curso