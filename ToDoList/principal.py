from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
from modelo import*
from data_acess_object import*


app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "cimento1"
app.config['MYSQL_DB'] = "TODO"
app.config['MYSQL_PORT'] = 3306
app.secret_key = 'cimento1' #ela é essencial para deletar dados do banco
db = MySQL(app)
atividade_dao = DAO(db)

@app.route("/",methods=['GET','POST'])
def teste():
    lista = atividade_dao.listar()
    return render_template('index.html',lista=lista)


@app.route('/deletar/<int:ide>')
def deletar(ide):
    atividade_dao.apagar(ide)
    flash("A tarefa foi removida com sucesso")
    return redirect(url_for('teste'))

@app.route('/editar/<int:ide>')
def editar(ide):
    lista = atividade_dao.busca_por_id(ide)
    return render_template('edita_todolista.html', lista=lista)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    tarefa = request.form['atividade']
    status = request.form['status']
    lista = Modelagem(tarefa,status,ide=request.form['ide'])
    atividade_dao.salvar(lista)
    return redirect(url_for('teste'))

@app.route('/criar', methods=['POST',])
def criar():
    tarefa = request.form['atividade']
    print(tarefa)
    status = request.form['status']
    lista = Modelagem(tarefa,status)
    atividade_dao.salvar(lista)
    return redirect(url_for('teste'))

if __name__=="__main__":
    app.run(debug=True)
