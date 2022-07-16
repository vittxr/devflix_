# Inicio import bibliotecas
from app import db
from email.policy import default
from flask import jsonify

from faker import Faker
from app import db, login_manager
from datetime import datetime, timedelta
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# Termino import biblioteca

class User(db.Model): # Classe com ORM - criar tabela usuário
    __tablename__="users" # Cria nome da tabela users
   
    # Inicio colunas  
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(64),unique=True, nullable=False)
    senha = db.Column(db.String(64), nullable=False)
    criado_em = db.Column(db.DateTime, nullable=False)
    # modificado_em = db.column(db.DateTime, nullable=False)
    ativo = db.Column(db.Boolean, default = True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id")) # Coluna de papeis - chave estrangeira de Role()
    cartoes = db.relationship('Cartao', backref="titular")
    # Término colunas tabela

    def __init__(self) -> None: # Método cria data/hora automático
        self.criado_em = datetime.now() 

class Role(db.Model): # Classe cria tabela de papeis
    __tablename__= "roles" # Cria nome da tabela roles

    # Inicio colunas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(16), nullable= False)
    users = db.relationship("User", backref="role") # Cria relacionamento com User()
    # Término colunas 

class Video(db.Model): #Classe cria tabela com as informações dos vídeos (caminhos, nome, etc)
    __tablename__ = "videos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(128), nullable=False)
    descricao = db.Column(db.String(256), nullable=False)
    formatos = db.Column(db.String(64), nullable=False)
    habilitado = db.Column(db.Boolean, nullable=False, default=True)
      #formatos é uma coluna que conterá o tipo da image e do vídeo. 
      #Não estamos guardando o path (caminho) para o arquivo, pq não precisa. Todos vídeos e imagens upados serão renomeados para ter o titulo como nome de arquivo. Assim, o path será uma junção de titulo + formato.

    #data_upload #como fazer uma coluna que contenha a data de upload?

class Cartao(db.Model):
    _tablename_ = 'cartoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome =db.Column(db.String(64), nullable=False)
    bandeira = db.Column(db.String(16))
    numero = db.Column(db.String(64), unique=True)
    validade = db.Column(db.Date)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self):
        return {
            "bandeira": self.bandeira,
            "numero": self.numero,
            "validade": self.validade
        }

    
