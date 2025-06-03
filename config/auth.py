from pytz import timezone # manipular fusos horários em Python

from typing import Optional
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer # Autorização em APIs

from sqlalchemy.future import select # Consultas assíncronas
from sqlalchemy.ext.asyncio import AsyncSession #  Interação Bancos de Dados assíncrona

from jose import jwt # Autorização (JSON Web Token)

from pydantic import EmailStr # Permitindo a validação automática de endereços de e-mail validos

# Meus módulos
from models.usuario_model import UsuarioModel
from config.conf_db import settings
from config.security import verificar_senha

# Endpoint para autenticação token (rota)
oauth2_schema = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/usuarios/login")

# Autentica senha e usuário por e-mail
async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email) # Filtra
        result = await session.execute(query) # Executa Banco de Dados
        usuario: UsuarioModel = result.scalars().unique().one_or_none() # Extrai

        # Se usuário não existir
        if not usuario:
            return None

        # Se senha não existir |  verificar_senha(senha envia, senha do banco)
        if not verificar_senha(senha, usuario.senha): # security
            return None

        return usuario

# Função (CRIAR TOKEN JWT)
def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    
    payload = {} # O payload é um dicionário que contém informações sobre o token, de acordo com o padrão JWT

    sp = timezone('America/Sao_Paulo') # Horário Global de São Paulo

    # expira = hora SP + conf_db.py(ACCESS_TOKEN_EXPIRE_MINUTES)
    expira = datetime.now(tz=sp) + tempo_vida

    # Campo de autenticação (https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3)

    payload["type"] = tipo_token # Pode ser "access" (token de acesso) ou "refresh" (token de renovação).

    payload["exp"] = expira # Define a data e hora de expiração do token.

    payload["iat"] = datetime.now(tz=sp) # Representa o horário que o token foi criado

    payload["sub"] = str(sub) # Define o identificador do usuário (geralmente o ID ou nome do usuário autenticado)

    
    # biblioteca(Dicionário, conf_db.py(JWT_SECRET), algorithm=conf_db.py(ALGORITHM))
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM) # Codificar autenticação JWT

# Gerar Token de acesso (Execução)
def criar_token_acesso(sub: str) -> str:
    """
    https://jwt.io
    """
    # Função (CRIAR TOKEN JWT)
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
