from flask import Flask, render_template
from pessoa import Pessoa

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def erro404(e):
    return render_template('erro.html'), 404

@app.route('/exemplo1')
def exemplo1():
    return render_template('exemplo1.html', nome_aluno='Maria', matricula=4456)

@app.route('/exemplo2')
def exemplo2():
    pessoa = {"nome": "Maria dos Santos", "matricula":8899, "curso":"Análise e Desenvolvimento de Sistemas"}
    return render_template('exemplo2.html', dados=pessoa)

@app.route('/exemplo3')
def exemplo3():
    pessoa = Pessoa("Maria dos Santos", 8899)
    return render_template('exemplo3.html', objeto=pessoa)

@app.route('/exemplo4')
def exemplo4():
    return render_template('exemplo4.html', nome_aluno='Rafael', matricula=123456, nota=7.5)

@app.route('/exemplo5')
def exemplo5():
    disciplina = 'Desenvolvimento Web'
    alunos = ['Ana Lúcia', 'Bia Santos', 'Carlos Eduardo', 'Daniel Silva', 'Eduardo Silva']
    return render_template('exemplo5.html', disc=disciplina, lista_alunos=alunos)

app.run(debug=True)
