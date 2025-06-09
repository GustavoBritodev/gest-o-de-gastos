import os

#tratar o diretório do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI -> é a configuração da URL de conexão com oo banco
#mysql+pymysql -> protocolo que será usado
#root2 -> usuário do banco
#usbw -> senha do banco
#localhost -> servidor que vai rodar o banco
#test -> base de dados que vai ser utilizada
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/test'