from database import db
from flask import Flask
from flask_migrate import Migrate
from usuarios import bp_usuarios

app = Flask(__name__)


conexao = "sqlite:///meubanco.sqlite" #variavel

app.config['SECRET_KEY'] = 'minha-chave' 
app.config['SQLALCHEMY_DATABASE_URI'] = conexao#conectando pela variavel
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) # inicializando o banco 

app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

migrate = Migrate(app, db) #fazendo a relaçao


@app.route('/home')
def index():
  return 'Hello from Flask!'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
