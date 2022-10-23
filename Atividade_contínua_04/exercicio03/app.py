'''
Considere os seguintes arquivos: "produto.py",
que contém uma classe que modela um Produto,
"app.py" que implementa uma pequena aplicação em Flask,
e "/templates/produtos.html" que implementa uma listagem de produtos através de uma tabela.
Qual alternativa contém os trechos de código que completam corretamente as lacunas no arquivo "/templates/produtos.html"?
'''

from flask import Flask, render_template
from produto import Produto

app = Flask(__name__)

@app.route('/produtos')
def produtos():
    prod1 = Produto('ABC', 'XZ123' , 8000, 6)
    prod2 = Produto('XYZ', 'Mobile3' , 3500, 30)
    prod3 = Produto('TECVIZION', 'LV5000' , 6000, 85)
    lista = [prod1, prod2, prod3]
    return render_template('produtos.html', listas_produtos=lista)

app.run(debug=True)
