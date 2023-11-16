import os
from flask import Flask, render_template, request, url_for, redirect
import csv

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

 @classmethod
 def from_csv(cls, row):
     return cls(row[0], row[1])

 def to_csv(self):
     return [self.termo, self.definicao]

# Inicializando o glossario

def save_glossario_to_csv(glossario):
 with open('glossario.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     for termo in glossario:
         writer.writerow(termo.to_csv())

def load_glossario_from_csv():
 glossario = []
 if os.path.exists('glossario.csv'):
   with open('glossario.csv', 'r') as file:
     reader = csv.reader(file)
     for row in reader:
         glossario.append(Termo.from_csv(row))
 return glossario
glossario = load_glossario_from_csv()

@app.route('/', methods=['GET', 'POST'])
def ola():
 if request.method == 'POST':
     termo = request.form['termo']
     definicao = request.form['definicao']
     glossario.append(Termo(termo, definicao))
     save_glossario_to_csv(glossario)
     return redirect(url_for('ola'))

 return render_template('index.html', glossario=glossario)



@app.route('/sobre-equipe')
def sobre():
   return render_template('sobre.html')

if __name__ == "__main__":
   app.run()
