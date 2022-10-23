from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/pagina')
def recebe_parametros_get():
    nome = request.args.get("nome")
    idade = request.args.get("idade")
    return f"O nome informado é: {nome} e a idade é: {idade}"

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

app.run(debug=True)
