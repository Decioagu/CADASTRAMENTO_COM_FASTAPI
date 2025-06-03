from typing import Optional

from pydantic import BaseModel, HttpUrl


class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int] = None

    '''
    O atributo orm_mode = True permite que o Pydantic converta objetos do 
    Banco de Dados no modelos do SQLAlchemy em dicionários compatíveis com JSON.
    '''
    class Config:
        from_attributes = True

class ArtigoSemIdSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    url_fonte: Optional[HttpUrl] = None
    usuario_id: Optional[int] = None
    class Config:
        from_attributes = True