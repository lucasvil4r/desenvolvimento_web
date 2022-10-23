'''
Considerando o código da aplicação em Flask (/app.py) e o template a seguir (/html/aluno.html),
assinale a alternativa que completa as lacunas corretamente para que o template seja utilizado
na rota "/aluno":
'''

from flask import Flask, render_template

app = Flask(__name__, template_folder='html')

@app.route('/aluno')
def uma_funcao ():
    nome = 'Maicon'
    return render_template('aluno.html', aluno=nome)

app.run(debug=True)
