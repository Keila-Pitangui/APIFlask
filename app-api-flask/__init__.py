from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criando a instância do banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config.from_object('app.config.Config')

    # Inicializando a extensão do banco
    db.init_app(app)

    # Registrando as rotas da aplicação
    from app.routes import main
    app.register_blueprint(main)

    return app
