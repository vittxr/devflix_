# Inicio Import bibliotecas do flask

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager
# Termino import bibliotecas do flask

# Scripts para futura utilização
#from flask_login import LoginManager
#login_manager = LoginManager()
#login_manager.login_view = 'auth/login'


db = SQLAlchemy()  # Instanciando o Banco de Dados do sqlAlchemy

def create_app(config_name): # Método cria app
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # Seleciona o ambiente de desenvolvimento

    db.init_app(app) # Iniciando o Banco de Dados
    #login_manager.init_app(app)   

    # Inicio import/registro Blueprint
    from app.auth import auth as auth_bp
    from app.main import main as main_bp
    from app.video import video as video_bp
    from app.financeiro import financeiro as financeiro_bp
     
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp) #, url_prefix ='/auth') 
    app.register_blueprint(video_bp, url_prefix="/video") #, url_prefix ='/video') 
    app.register_blueprint(financeiro_bp, url_prefix="/planos")
    # Termino import/registro Blueprint

    return app


