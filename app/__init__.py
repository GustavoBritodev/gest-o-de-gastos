from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

#definição do app
app = Flask(__name__)

#chave pra criptografar as senhas do banco
app.secret_key = 'chave_super_secreta'

#configuração do banco
app.config.from_object('config.Config')

#definição do banco
db = SQLAlchemy(app)

from app import routes, models