import os
import csv
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente!!!
app.debug = os.environ.get('FLASK_DEBUG') == 'True'


@app.route('/')
def index():
    glossario_de_termos = []

    with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            glossario_de_termos.append(l)

    lista_de_tarefas = []

    with open('bd_tarefas.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            lista_de_tarefas.append(l)

    tarefas_concluidas = []

    with open('bd_tarefas_concluidas.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            tarefas_concluidas.append(l)

    return render_template('index.html', glossario=glossario_de_termos, tarefas=lista_de_tarefas, concluidos=tarefas_concluidas)


@app.route('/sobre_equipe')
def sobre():
    return render_template('sobre.html')


@app.route('/glossario')
def glossario():
    glossario_de_termos = []

    with open('bd_glossario.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            glossario_de_termos.append(l)

    return render_template('glossario.html', glossario=glossario_de_termos)


@app.route('/novo_termo')
def novo_termo():
    return render_template('adicionar_termo.html')


@app.route('/criar_termo', methods=['POST', ])
def criar_termo():
    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario'))


@app.route('/excluir_termo/<int:termo_id>', methods=['POST'])
def excluir_termo(termo_id):
    with open('bd_glossario.csv', 'r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        linhas = list(reader)

    # Encontrar e excluir o termo com base no ID
    for i, linha in enumerate(linhas):
        if i == termo_id:
            del linhas[i]
            break

    # salvar as alterações de volta no arquivo
    with open('bd_glossario.csv', 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linhas)

    return redirect(url_for('glossario'))


@app.route('/tarefas')
def tarefas():
    lista_de_tarefas = []

    with open('bd_tarefas.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            lista_de_tarefas.append(l)

    tarefas_concluidas = []
    with open('bd_tarefas_concluidas.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            tarefas_concluidas.append(l)

    return render_template('tarefas.html', tarefas=lista_de_tarefas, concluidos=tarefas_concluidas)


@app.route('/nova_tarefa')
def nova_tarefa():
    return render_template('adicionar_tarefa.html')


@app.route('/criar_tarefa', methods=['POST', ])
def criar_tarefa():
    lista = request.form['lista']
    descricao = request.form['descricao']

    with open('bd_tarefas.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([lista, descricao])

    return redirect(url_for('tarefas'))


@app.route('/excluir_tarefa/<int:tarefa_id>', methods=['POST'])
def excluir_tarefa(tarefa_id):
    with open('bd_tarefas.csv', 'r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        linhas = list(reader)

    # Encontrar e excluir o termo com base no ID
    for i, linha in enumerate(linhas):
        if i == tarefa_id:
            del linhas[i]
            break

    # salvar as alterações de volta no arquivo
    with open('bd_tarefas.csv', 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linhas)

    return redirect(url_for('tarefas'))


@app.route('/concluir_tarefa/<int:tarefa_id>', methods=['POST', ])
def concluir_tarefa(tarefa_id):

    lista_de_tarefas = []

    with open('bd_tarefas.csv', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            lista_de_tarefas.append(l)

    tarefa = lista_de_tarefas[tarefa_id]

    with open('bd_tarefas_concluidas.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerows([tarefa])

#excluir

    with open('bd_tarefas.csv', 'r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        linhas = list(reader)

    # Encontrar e excluir o termo com base no ID
    for i, linha in enumerate(linhas):
        if i == tarefa_id:
            del linhas[i]
            break

    # salvar as alterações de volta no arquivo
    with open('bd_tarefas.csv', 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linhas)

    return redirect(url_for('tarefas'))

@app.route('/excluir_tarefa_concluida/<int:tarefa_id>', methods=['POST'])
def excluir_tarefa_concluida(tarefa_id):
    with open('bd_tarefas_concluidas.csv', 'r', newline='') as arquivo:
        reader = csv.reader(arquivo)
        linhas = list(reader)

    # Encontrar e excluir o termo com base no ID
    for i, linha in enumerate(linhas):
        if i == tarefa_id:
            del linhas[i]
            break

    # salvar as alterações de volta no arquivo
    with open('bd_tarefas_concluidas.csv', 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linhas)

    return redirect(url_for('tarefas'))


if __name__ == "__main__":
    app.run()
