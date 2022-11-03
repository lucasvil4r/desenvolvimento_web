from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pagina.html')

@app.route('/cursos')
def cursos():
    valor = "Thiago"
    return render_template('cursos.html', nome=valor)

app.run(debug=True)
