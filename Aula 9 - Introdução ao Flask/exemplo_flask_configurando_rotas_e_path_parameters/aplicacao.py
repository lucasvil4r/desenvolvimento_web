from flask import Flask

app = Flask(__name__)

@app.route('/')
def ola():
    s = "<h1>Título da página de teste</h1>"
    s += "<p>Parágrafo bla bla bla bla bla bla</p>"
    return s

@app.route('/alunos')
def lista_alunos():
    s = "<h1>Lista de alunos de ADS2BN</h1>"
    s += "<ul>"
    s += "<li>Miguel</li>"
    s += "<li>Guilherme</li>"
    s += "<li>Miguel</li>"
    s += "</ul>"
    return s

@app.route('/disciplina/<nome_disc>')  # <nome_disc> é um "slug"
def disciplina(nome_disc):
    if nome_disc == 'devweb':
        return "Essa é a página de Desenvolvimento Web"
    elif nome_disc == 'poo':
        return "Essa é a página de Programação Orientada a Objetos"
    else:
        return "Curso inexistente"

@app.route('/turma/<nome>/<float:numero>')
def turma(nome, numero):
    return "Essa é a página da turma {0} de número {1}".format(nome, numero)

app.run(debug=True)
