from passlib.context import CryptContext

'''
Criptografa senha enviada por usuário
Compara senha do usuário com senha criptografada no Banco de dados
'''

# Configuração do hash de senha
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Função para verificar senha (COMPARA SENHA (CRIPTOGRAFA SENHA) COM A DO USUÁRIO)
def verificar_senha(senha: str, hash_senha: str) -> bool:
    return CRIPTO.verify(senha, hash_senha)

# Função para obter hash de senha (CRIPTOGRAFA SENHA)
def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)
