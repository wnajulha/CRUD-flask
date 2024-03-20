from flask import Blueprint, render_template,request,redirect
from models import Usuario
from database import db

bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates")


@bp_usuarios.route('/create',methods=['GET', 'POST'])
def create():
  if request.method=='GET':
    return render_template('usuarios_create.html')
  
  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    csenha = request.form.get('csenha')
   
  
    U = Usuario(nome, email, senha)
    db.session.add(U)
    db.session.commit()
    return 'dados cadastrados com sucesso'

@bp_usuarios.route('/recovery')
def recovery():
  usuarios = Usuario.query.all()
  return render_template('usuarios_recovery.html', usuarios=usuarios)


@bp_usuarios.route('/update/<int:id>',methods=['GET', 'POST'])
def update(id):
  U = Usuario.query.get(id)

  if request.method=='GET':
    return render_template('usuarios_update.html', U = U)
  
  if request.method=='POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    U.nome = nome
    U.email = email
    db.session.add(U)
    db.session.commit()
    return redirect('/usuarios/recovery')
    

@bp_usuarios.route('/delete/<int:id>',methods=['GET', 'POST'])
def delete(id):
  U = Usuario.query.get(id)

  if request.method=='GET':
    return render_template('usuarios_delete.html', U = U)
  
  if request.method=='POST':
    db.session.delete(U)
    db.session.commit()
    return "Dados excluidos com sucesso!"
    