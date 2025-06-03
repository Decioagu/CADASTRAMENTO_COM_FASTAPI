from fastapi import FastAPI

import sys
import os
# Adiciona o diretório atual ao sys.path para importar módulos locais
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from config.conf_db import settings
from routes.v1.api import api_router 

app: FastAPI = FastAPI(title='Curso API - FastAPI SQL Model')

# rota (home)
@app.get('/', description='Retorna uma mensagem', summary='Documento', tags=["Documentação"])
async def index(): # recurso GET
   return {"http://127.0.0.1:8000/docs"}

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn main:app --reload

'''
Observação, o uso de "sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))",
consistem em adicionar o caminho absoluto do diretório atual ao sys.path:

Caso o projeto seja executado fora do diretório do projeto:
    Exemplo: "uvicorn CADASTRAMENTO_COM_FASTAPI.main.py.main:app --reload".

Caso execute o "uvicorn main:app --reload" dentro da pasta CADASTRAMENTO_COM_FASTAPI 
não ocorrera erro de caminho de diretório.

REPOSITORIO/
├── CADASTRAMENTO_COM_FASTAPI/
│   └── main.py
│   templates/
│   └── index.html
│   └── servico.html 
'''