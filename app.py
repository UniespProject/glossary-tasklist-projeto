import os
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente
app.debug = os.environ.get('FLASK_DEBUG') == 'True'


# Teste de Glossário

class Termo:
    def __init__(self, termo, definicao):
        self.termo = termo
        self.definicao = definicao


glossario = [
    Termo('Internet', 'Acessar internet'),
    Termo('Java', 'Pior linguagem de Programação'),
    Termo('Python', 'Melhor linguagem'),
    Termo('Test', 'Deu certo'),
]


@app.route('/', methods=['GET', 'POST'])
def ola():
    if request.method == 'POST':
        termo = request.form['termo']
        definicao = request.form['definicao']
        glossario.append(Termo(termo, definicao))
        return redirect(url_for('ola'))

    return render_template('index.html', glossario=glossario)


@app.route('/sobre-equipe')
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    app.run()
