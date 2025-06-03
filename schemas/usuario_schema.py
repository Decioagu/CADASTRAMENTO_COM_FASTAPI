from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    '''
    O atributo orm_mode = True permite que o Pydantic converta objetos do 
    Banco de Dados no modelos do SQLAlchemy em dicionários compatíveis com JSON.
    '''
    class Config:
        from_attributes = True

# Senha do usuário
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

# Artigos do usuário (RELACIONAMENTO)
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]

# Atualizar usuário
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    eh_admin: Optional[bool] = None
