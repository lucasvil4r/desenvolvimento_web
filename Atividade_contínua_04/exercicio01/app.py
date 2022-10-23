# Imagine a seguinte configuração de rotas no Flask. Marque a única URL que NÃO redireciona para nenhum Controller:

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/cursos/<siglas>')
def curso(sigla):
    return render_template('cursos.html', nome=sigla)

@app.route('/cursos/<siglas>/disc')
def disciplinas(sigla):
    return render_template('disciplinas.html', disc=sigla)

@app.route('/cursos/<siglas>/disc/<int:id>')
def cursos_com_sigla_id(sigla, id):
    return render_template('curso2.html', nome_curso=sigla, cod_curso=id)

app.run(debug=True)
