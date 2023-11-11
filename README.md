# glossary-tasklist-projeto
Projeto da uniesp de Introdução a programação do prof Messias 


-> Man - Principal 

-> Developer  - Branch de desenvolvimento


convenção de commits 

feat- Commits do tipo feat indicam que seu trecho de código está incluindo um novo recurso (se relaciona com o MINOR do versionamento semântico).

fix - Commits do tipo fix indicam que seu trecho de código commitado está solucionando um problema (bug fix), (se relaciona com o PATCH do versionamento semântico).

docs - Commits do tipo docs indicam que houveram mudanças na documentação, como por exemplo no Readme do seu repositório. (Não inclui alterações em código).

test - Commits do tipo test são utilizados quando são realizadas alterações em testes, seja criando, alterando ou excluindo testes unitários. (Não inclui alterações em código)

# Repositório de Aprendizado sobre Git e Versionamento 

Este repositório é destinado a ajudar iniciantes a entender e praticar conceitos fundamentais de controle de versão, como branches, padrões de commits e versionamento. Aqui, você encontrará informações e recursos para melhorar seu conhecimento nesses tópicos.

## Branches

### O que são branches?

Branches são ramificações dentro do repositório que permitem o desenvolvimento paralelo de diferentes recursos ou correções de bugs. Eles são úteis para isolar o trabalho em progresso e evitar conflitos durante o desenvolvimento.
são caminhos alternativos no desenvolvimento de um projeto, permitindo que você trabalhe em diferentes recursos ou correções independentemente.

### Como criar um novo branch?

Você pode criar um novo branch usando o comando Git `git checkout -b nome-do-branch`, substituindo "nome-do-branch" pelo nome que você escolher.

### Como alternar entre branches?

Use `git checkout nome-do-branch` para alternar entre branches existentes.

## Padrões de Commits

### O que são padrões de commits? 

Padrões de commits são diretrizes para escrever mensagens de commit significativas e consistentes. Eles ajudam a entender as alterações introduzidas em um commit e a manter um histórico de alterações limpo e organizado.

### Exemplo de uma mensagem de commit com padrão:


## Versionamento Semântico

### O que é versionamento semântico?

O versionamento semântico é um sistema para atribuir significado a números de versão de software. Ele segue a seguinte convenção: `MAJOR.MINOR.PATCH`. Por exemplo, `1.2.3`.

- MAJOR: Versões incompatíveis que exigem alterações significativas.
- MINOR: Adições de funcionalidade compatíveis com versões anteriores.
- PATCH: Correções de bugs compatíveis com versões anteriores.

### Como usar o versionamento semântico?

Ao criar tags de versão em seu repositório, siga o padrão de versionamento semântico para indicar as mudanças introduzidas em uma versão específica.

## Recursos Adicionais

- [Documentação oficial do Git](https://git-scm.com/doc)
- [Guia do Versionamento Semântico](https://semver.org/)

Este repositório é um espaço de aprendizado e prática. Sinta-se à vontade para experimentar e aprimorar suas habilidades com Git e versionamento. Boa sorte!
