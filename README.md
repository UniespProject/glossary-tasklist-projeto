# Documentação do Projeto Flask
Este documento fornece uma documentação detalhada do projeto Flask, explicando a estrutura do código, suas principais funcionalidades e como cada parte do código contribui para a aplicação.

## Estrutura do Projeto
O projeto consiste em um aplicativo web Flask para gerenciamento de glossário e tarefas. A estrutura de pastas e arquivos é a seguinte:

``` projeto_flask
projeto_flask/
│
├── static/
│   ├── images/
│   │   ├── carlos.jpeg
│   │   ├── hallan.jpeg
│   │   ├── jhonatan.jpeg
│   │   └── raissa.jpeg
│
├── templates/
│   ├── adicionar_tarefa.html
│   ├── adicionar_termo.html
│   ├── glossario.html
│   ├── index.html
│   ├── sobre.html
│   └── tarefas.html
│
├── bd_glossario.csv
├── bd_tarefas.csv
├── bd_tarefas_concluidas.csv
├── app.py
└── README.md
 ```


### templates: Contém os modelos HTML utilizados pelo Flask para renderizar as páginas web.
*  bd_glossario.csv: Arquivo CSV para armazenar dados do glossário.
*  bd_tarefas.csv: Arquivo CSV para armazenar dados da lista de tarefas.
*  bd_tarefas_concluidas.csv: Arquivo CSV para armazenar dados de tarefas concluídas.
*  app.py: Arquivo principal que contém o código Flask.
*   README.md: Documentação do projeto.

## Funcionalidades: 

* Página Inicial **(index)**
A função index lê os dados dos arquivos CSV do glossário, tarefas e tarefas concluídas. Em seguida, renderiza a página inicial (index.html) com esses dados.

* Sobre a Equipe **(sobre)**
A função sobre renderiza a página "Sobre a Equipe" (sobre.html), fornecendo informações sobre a equipe envolvida no projeto.

* Glossário **(glossario)**
A função glossario lê os dados do arquivo CSV do glossário e renderiza a página do glossário (glossario.html) com esses dados.

* Adicionar Novo Termo **(novo_termo)**
A função novo_termo renderiza a página para adicionar um novo termo ao glossário (adicionar_termo.html).

* Criar Termo **(criar_termo)**
A função criar_termo é acionada por um formulário na página "Adicionar Novo Termo". Ela extrai os dados do formulário, adiciona um novo termo ao arquivo CSV do glossário e redireciona para a página do glossário.

* Excluir Termo **(excluir_termo)**
A função excluir_termo exclui um termo do glossário com base no ID fornecido, atualizando o arquivo CSV e redirecionando para a página do glossário.

* Lista de Tarefas **(tarefas)**
A função tarefas lê os dados dos arquivos CSV de tarefas e tarefas concluídas e renderiza a página de tarefas (tarefas.html) com esses dados.

* Adicionar Nova Tarefa **(nova_tarefa)**
A função nova_tarefa renderiza a página para adicionar uma nova tarefa (adicionar_tarefa.html).

* Criar Tarefa **(criar_tarefa)**
A função criar_tarefa é acionada por um formulário na página "Adicionar Nova Tarefa". Ela extrai os dados do formulário, adiciona uma nova tarefa ao arquivo CSV de tarefas e redireciona para a página de tarefas.

* Excluir Tarefa **(excluir_tarefa)**
A função excluir_tarefa exclui uma tarefa com base no ID fornecido, atualizando o arquivo CSV de tarefas e redirecionando para a página de tarefas.

* Concluir Tarefa **(concluir_tarefa)**
A função concluir_tarefa move uma tarefa da lista de tarefas para a lista de tarefas concluídas, atualizando ambos os arquivos CSV e redirecionando para a página de tarefas.

* Executando o Projeto
Para executar o projeto, certifique-se de ter o ambiente Flask configurado. Execute o arquivo app.py e acesse o aplicativo através do navegador.