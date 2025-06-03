# ========================= CAMINHO ARQUIVO SQLite ==============================
from pathlib import Path # Pasta

# Criando uma engine para um banco SQLite (ou pode ser MySQL, PostgreSQL etc.)
caminho_do_arquivo = Path(__file__).parent.parent

# ======================= CONEXÃO BANCO DE DADOS ===============================
from sqlalchemy.ext.declarative import declarative_base

# Definição direta da URL do banco de dados
DB_URL: str = f"sqlite+aiosqlite:///{caminho_do_arquivo}/faculdade.db" # SQLite
# DB_URL: str = 'mysql+aiomysql://root:Enigma.1@localhost:3306/faculdade' # MySQL

# Modelagem Banco de Dados
DBBaseModel = declarative_base()

# ========================= SESSÃO BANCO DE DADOS =============================
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

# conexão do Banco de Dados (ENDEREÇO BANCO DE DADOS)
engine: AsyncEngine = create_async_engine(DB_URL, echo=False)

# Cria sessão de Banco de Dados assíncrono (INTERAÇÃO)
Session: AsyncSession = sessionmaker(
    autocommit=False, # não faz "commit" automaticamente
    autoflush=False, # não executar consulta automáticas 
    expire_on_commit=False, # sessão não aspirá apos "commit"
    class_=AsyncSession, #  sessão assíncrono
    bind=engine # ativa conexão com o banco de dados
)
# ================= SESSÃO COMMIT (ABERTURA E FECHAMENTO) ======================
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

# consulta no Banco de Dados
async def get_session() -> Generator: # type: ignore
    session: AsyncSession = Session()

    try:
        yield session # Abrir sessão
    finally:
        await session.close() # Fechar sessão


# ========================= ROTAS API (RECURSOS) ===============================
from pydantic_settings import BaseSettings

#  Gerenciar configurações de aplicativos
class Settings(BaseSettings):
    
    JWT_SECRET: str = "qS96E1oCfq5gEZH-ngD91NC2qkcl0cffhNTIDGpF4pw" # senha gerada em Token_JWT.py   

    '''
    HS256 (HMAC + SHA-256): define o algoritmo de criptografia utilizado 
    para assinar e verificar os tokens JWT (JSON Web Token).
    
    - HS significa HMAC (Hash-based Message Authentication Code).
    - 256 refere-se ao uso do SHA-256 (Secure Hash Algorithm 256 bits) como função de hash.
    - O HMAC usa uma chave secreta (JWT_SECRET) para assinar e validar o token.
    '''
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # Tempo de acesso ao token

    API_V1_STR: str = '/routes/v1' # anotação rota

    # Define que as variáveis de ambiente no Pydantic devem ser sensíveis a maiúsculas e minúsculas.
    class Config:
        case_sensitive = True

settings = Settings()
