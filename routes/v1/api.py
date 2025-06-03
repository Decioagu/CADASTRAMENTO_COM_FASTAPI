import sys
import os
# Aponta caminho pasta atual do arquivo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__)))) 
from endpoints import artigo
from endpoints import usuario

from fastapi import APIRouter
api_router = APIRouter() # roteador

api_router.include_router(artigo.router, prefix='/artigos', tags=['artigos']) # rota
api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios']) # rota
