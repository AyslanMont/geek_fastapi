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