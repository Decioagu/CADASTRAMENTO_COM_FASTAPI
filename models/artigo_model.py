from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.conf_db import DBBaseModel


class ArtigoModel(DBBaseModel):
    __tablename__ = 'artigos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(256), unique=True)
    descricao = Column(String(256))
    url_fonte = Column(String(256))
    usuario_id = Column(Integer, ForeignKey('usuarios.id')) # Chave estrangeira
    criador = relationship("UsuarioModel", back_populates='artigos', lazy='joined') # relacionamento
