from config.conf_db import engine, DBBaseModel ### Configuração do Banco de Dados

import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

async def create_tables() -> None:
    import models.__all_models
    print('Criando as tabelas no banco de dados...')

    async with engine.begin() as conn:
        print(DBBaseModel.metadata.tables.keys()) # Exibir nome da tabela (.\models\curso_model.py)
        await conn.run_sync(DBBaseModel.metadata.drop_all)
        await conn.run_sync(DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
